#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <algorithm>

#include "TString.h"

#include "MvaFactory.h"
#include "MvaTreeHandler.h"
#include "MvaTreeAnalyzer.h"
#include "MvaWeights2d.h"
#include "mvaSetup.h"
#include "higgsUtils.h"
#include "../../diLeptonic/src/sampleHelpers.h"
#include "../../diLeptonic/src/CommandLineParameters.h"
#include "../../diLeptonic/src/utils.h"





/// The MVA input base folder
constexpr const char* MvaInputDIR = "mvaInput";

/// The MVA output base folder
constexpr const char* MvaOutputDIR = "mvaOutput";

/// The MVA output sub-folder for weights (1D and 2D weights)
constexpr const char* MvaWeightFileDIR = "weights";



/// Input base for the file lists containing the samples to be processed
constexpr const char* FileListBASE = "FileLists_mva/HistoFileList_";



/// The output file name for the control and separation power plots
constexpr const char* PlotOutputFILE = "plots.root";

/// The output file name for the MVA weights histograms (2D)
constexpr const char* WeightsOutputFILE = "weights2d.root";





void trainBdtTopSystemJetAssignment(const std::vector<Channel::Channel>& v_channel,
                                    const std::vector<Systematic::Systematic>& v_systematic,
                                    const std::vector<std::string>& v_mode)
{
    // Access all MVA input file names for all systematics and channels
    tth::mvaHelpers::SystematicChannelFileNames m_systematicChannelFileNamesTraining =
        tth::mvaHelpers::systematicChannelFileNames(FileListBASE, v_channel, v_systematic);
    tth::mvaHelpers::SystematicChannelFileNames m_systematicChannelFileNamesTesting =
        tth::mvaHelpers::systematicChannelFileNames(FileListBASE, v_channel, v_systematic, false);
    
    // Define MVA sets, i.e. for which merged categories of which step to apply MVA (also separated by channels)
    // First set is for correct combinations, second for swapped combinations
    const std::vector<Channel::Channel> allChannels = {Channel::ee, Channel::emu, Channel::mumu, Channel::combined};
    std::vector<mvaSetup::MvaSet> mvaSets;
    mvaSets.push_back(mvaSetup::MvaSet(
        allChannels,
        "10",
        {0,1},
        {mvaSetup::c1, mvaSetup::c2, mvaSetup::c3},
        {mvaSetup::c1, mvaSetup::c2, mvaSetup::c3}));
    mvaSets.push_back(mvaSetup::MvaSet(
        allChannels,
        "10",
        {2},
        {mvaSetup::c1, mvaSetup::c2, mvaSetup::c3},
        {mvaSetup::c1, mvaSetup::c2, mvaSetup::c3}));
    mvaSets.push_back(mvaSetup::MvaSet(
        allChannels,
        "10",
        {},
        {mvaSetup::c1},
        {mvaSetup::c2, mvaSetup::c3}));
    
    // Loop over all channels and systematics and merge trees
    mvaSetup::SystematicChannelFileNames m_systematicChannelMergedFiles = 
        mvaSetup::mergeTrees(MvaInputDIR,
                             m_systematicChannelFileNamesTraining,
                             m_systematicChannelFileNamesTesting,
                             mvaSets);
    
    // Loop over all channels and systematics and run tools
    for(const auto& systematicChannelMergedFiles : m_systematicChannelMergedFiles){
        const Systematic::Systematic& systematic = systematicChannelMergedFiles.first;
        for(const auto& channelMergedFiles : systematicChannelMergedFiles.second){
            const Channel::Channel& channel = channelMergedFiles.first;
            const TString outputFolder = ttbar::assignFolder(MvaOutputDIR, channel, systematic);
            const TString& fileName = channelMergedFiles.second.at(0);
            
            // Print all separation power plots
            if(std::find(v_mode.begin(), v_mode.end(), "cp") != v_mode.end()){
                TString outputFile = outputFolder;
                outputFile.Append(PlotOutputFILE);
                MvaTreeHandler mvaTreeHandler("", {});
                mvaTreeHandler.importTrees(fileName.Data(), "training");
                MvaTreeAnalyzer mvaTreeAnalyzer(mvaTreeHandler.stepMvaVariablesMap(), true);
                mvaTreeAnalyzer.plotVariables(outputFile.Data());
            }
            
            // Produce MVA weights
            if(std::find(v_mode.begin(), v_mode.end(), "mva") != v_mode.end()){
                
                // Clean the MVA sets in case they are not selected for training
                std::vector<mvaSetup::MvaSet> cleanSets = mvaSetup::cleanForChannel(mvaSets, channel);
                
                // Run the MVA training for correct and swapped combinations
                MvaFactory mvaFactory(outputFolder, MvaWeightFileDIR,
                                      cleanSets, fileName);
                
                // Build 2D histograms of MVA weights for correct and swapped combinations
                MvaTreeHandler mvaTreeHandler("", {});
                mvaTreeHandler.importTrees(fileName.Data(), "training");
                TString weightsFolder(outputFolder);
                weightsFolder.Append(MvaWeightFileDIR).Append("/");
                TString outputFile = weightsFolder;
                outputFile.Append(WeightsOutputFILE);
                MvaWeights2d mvaWeights2d(mvaTreeHandler.stepMvaVariablesMap(),
                                          weightsFolder.Data(), mvaSets, true);
                mvaWeights2d.plotVariables(outputFile.Data());
            }
        }
    }
    
    std::cout<<"MVA program successfully finished";
}



int main(int argc, char** argv)
{
    CLParameter<std::string> opt_channel("c", "Specify channel(s), valid: emu, ee, mumu, combined. Default: combined", false, 1, 4,
        ttbar::makeStringCheck(Channel::convertChannels(Channel::allowedChannelsPlotting)));
    CLParameter<std::string> opt_systematic("s", "Systematic variation - default is Nominal", false, 1, 100,
        ttbar::makeStringCheck({"Nominal", ""}));
    CLParameter<std::string> opt_mode("m", "Mode: separation plots (cp), run MVA (mva). Default is cp", false, 1, 2,
        //[](const std::string& m){return m=="" || m=="cp" || m=="mva";});
        ttbar::makeStringCheck({"", "cp", "mva"}));
    CLAnalyser::interpretGlobal(argc, argv);
    
    // Set up channels
    std::vector<Channel::Channel> v_channel({Channel::combined});
    if(opt_channel.isSet()) v_channel = Channel::convertChannels(opt_channel.getArguments());
    std::cout << "Processing channels: ";
    for (auto channel : v_channel)std::cout << Channel::convertChannel(channel) << " ";
    std::cout << "\n\n";
    
    // Set up systematics
    std::vector<Systematic::Systematic> v_systematic({Systematic::nominal});
    if(opt_systematic.isSet()) v_systematic = Systematic::convertSystematics(opt_systematic.getArguments());
    std::cout << "Processing systematics: "; 
    for (auto systematic : v_systematic) std::cout << Systematic::convertSystematic(systematic) << " ";
    std::cout << "\n\n";
    
    // Set up modes
    const std::vector<std::string> v_mode = opt_mode.isSet() ? opt_mode.getArguments() : std::vector<std::string>{"cp"};
    std::cout << "Running following modes: ";
    for (auto mode : v_mode)std::cout << mode << " ";
    std::cout << "\n\n";
    
    trainBdtTopSystemJetAssignment(v_channel, v_systematic, v_mode);
}





