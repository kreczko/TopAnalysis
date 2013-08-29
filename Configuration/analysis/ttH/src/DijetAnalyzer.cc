#include <iostream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <sstream>

#include <TTree.h>
#include <TSystem.h>
#include <TH1.h>
#include <TH2.h>
#include <TFile.h>
#include <TString.h>
#include <Math/VectorUtil.h>
#include <TSelectorList.h>
#include <Rtypes.h>

#include "DijetAnalyzer.h"
#include "analysisStructs.h"
#include "higgsUtils.h"
#include "../../diLeptonic/src/analysisObjectStructs.h"
#include "../../diLeptonic/src/analysisUtils.h"
#include "../../diLeptonic/src/classes.h"


DijetAnalyzer::DijetAnalyzer(const std::vector<TString>& selectionStepsNoCategories,
                             const std::vector<TString>& stepsForCategories,
                             const JetCategories* jetCategories):
AnalysisHistogramsBase(selectionStepsNoCategories, stepsForCategories, jetCategories)
{
    std::cout<<"--- Beginning setting up dijet analyzer\n";
    std::cout<<"=== Finishing setting up dijet analyzer\n\n";
}



void DijetAnalyzer::fill(const RecoObjects& recoObjects, const CommonGenObjects& commonGenObjects,
                         const TopGenObjects& topGenObjects, const HiggsGenObjects& higgsGenObjects,
                         const KinRecoObjects& kinRecoObjects,
                         const tth::GenObjectIndices& genObjectIndices, const tth::RecoObjectIndices& recoObjectIndices,
                         const double& weight, const TString& stepShort)
{
    // Number of selected jets and bjets
    const int numberOfJets = recoObjectIndices.jetIndices_.size();
    const int numberOfBjets = recoObjectIndices.bjetIndices_.size();

    // Set up step name and check if step exists
    const bool stepInCategory = stepShort.Contains("_cate");
    const TString step = stepInCategory ? stepShort : this->stepName(stepShort);
    const bool stepExists(this->checkExistence(step));
    if(!stepInCategory && jetCategories_){
        // Here check the individual jet categories
        const int categoryId = jetCategories_->categoryId(numberOfJets, numberOfBjets);
        const TString fullStepName = this->stepName(stepShort, categoryId);
        this->fill(recoObjects, commonGenObjects, topGenObjects, higgsGenObjects, kinRecoObjects,
                   genObjectIndices, recoObjectIndices, weight, fullStepName);
    }
    if(!stepExists) return;
    std::map<TString, TH1*>& m_histogram = m_stepHistograms_[step].m_histogram_;



    // Extracting input data to more comfortable variables
    const VLV& allJets = *recoObjects.jets_;
    const LV& lepton = recoObjects.allLeptons_->at(recoObjectIndices.leptonIndex_);
    const LV& antilepton = recoObjects.allLeptons_->at(recoObjectIndices.antiLeptonIndex_);
    const LV& met = *recoObjects.met_;
    const std::vector<int>& jetsId = recoObjectIndices.jetIndices_;           // Selected jets (point to jets from allJets)
    const std::vector<int>& bJetsId = recoObjectIndices.bjetIndices_;         // B-tagged jets (point to jets from allJets)
    std::vector<int> topJetsId;                                               // Jets from ttbar by KinReco (Point to jets from allJets)
    if(kinRecoObjects.valuesSet_) {
        if(kinRecoObjects.HypJet0index_) topJetsId.push_back(kinRecoObjects.HypJet0index_->at(0));
        if(kinRecoObjects.HypJet1index_) topJetsId.push_back(kinRecoObjects.HypJet1index_->at(0));
    }
    const std::vector<double>& allJetsBtagDiscriminant = *recoObjects.jetBTagCSV_;

    // Setting variables of gen. level if available
    const VLV& genJets = (commonGenObjects.valuesSet_) ? *commonGenObjects.allGenJets_ : VLV(0);
    const std::vector<int>& bHadJetIndex = (topGenObjects.valuesSet_) ? *topGenObjects.genBHadJetIndex_ : std::vector<int>(0);
    const std::vector<int>& bHadFlavour = (topGenObjects.valuesSet_) ? *topGenObjects.genBHadFlavour_ : std::vector<int>(0);
    const std::vector<int>& bHadIndex = (topGenObjects.valuesSet_) ? *topGenObjects.genBHadIndex_ : std::vector<int>(0);
    const std::vector<LV>& bHadPlusMothers = (topGenObjects.valuesSet_) ? *topGenObjects.genBHadPlusMothers_ : std::vector<LV>(0);
    std::vector<int> trueTopAllJetsId;          // Reco jets coming from top (Point to jets from allJets) [Can be any jet]
    std::vector<int> trueTopJetsId;             // Reco jets coming from top (Point to jets from allJets) [Only selected jets]
    std::vector<int> trueHiggsAllJetsId;        // Reco jets coming from higgs (Point to jets from allJets) [Can be any jet]
    std::vector<int> trueHiggsJetsId;           // Reco jets coming from higgs (Point to jets from allJets) [Only selected jets]
    std::vector<int> trueTopBJetsId;            // Reco jets coming from top (Point to b-tagged jets from allJets) [Only selected jets]
    std::vector<int> trueHiggsBJetsId;          // Reco jets coming from higgs (Point to b-tagged jets from allJets) [Only selected jets]
    std::vector<int> topBJetsId;                // Reco jets comning from top according to KinReco (Point to b-tagged jets from allJets) [Only selected jets]
    // Creating a list of LorentzVectors of the bHadrons
    std::vector<LV> bHadLVs;
    for(const int index : bHadIndex) {
        LV bHadLV = bHadPlusMothers.at(index);
        bHadLVs.push_back(bHadLV);
    }


    // Filling vectors of true reco top jets
    int trueTopBJetId = genObjectIndices.recoBjetFromTopIndex_;
    if(trueTopBJetId >= 0) {
        trueTopAllJetsId.push_back(trueTopBJetId);
        if(isInVector(jetsId, trueTopBJetId)) trueTopJetsId.push_back(trueTopBJetId);
        if(isInVector(bJetsId, trueTopBJetId)) trueTopBJetsId.push_back(trueTopBJetId);
    }
    int trueTopAntiBJetId = genObjectIndices.recoAntiBjetFromTopIndex_;
    if(trueTopAntiBJetId >= 0) {
        trueTopAllJetsId.push_back(trueTopAntiBJetId);
        if(isInVector(jetsId, trueTopAntiBJetId)) trueTopJetsId.push_back(trueTopAntiBJetId);
        if(isInVector(bJetsId, trueTopAntiBJetId)) trueTopBJetsId.push_back(trueTopAntiBJetId);
    }

    // Filling vectors of true reco Higgs jets
    int trueHiggsBJetId = genObjectIndices.recoBjetFromHiggsIndex_;
    if(trueHiggsBJetId >= 0) {
        trueHiggsAllJetsId.push_back(trueHiggsBJetId);
        if(isInVector(jetsId, trueHiggsBJetId)) trueHiggsJetsId.push_back(trueHiggsBJetId);
        if(isInVector(bJetsId, trueHiggsBJetId)) trueHiggsBJetsId.push_back(trueHiggsBJetId);
    }
    int trueHiggsAntiBJetId = genObjectIndices.recoAntiBjetFromHiggsIndex_;
    if(trueHiggsAntiBJetId >= 0) {
        trueHiggsAllJetsId.push_back(trueHiggsAntiBJetId);
        if(isInVector(jetsId, trueHiggsAntiBJetId)) trueHiggsJetsId.push_back(trueHiggsAntiBJetId);
        if(isInVector(bJetsId, trueHiggsAntiBJetId)) trueHiggsBJetsId.push_back(trueHiggsAntiBJetId);
    }
    // Getting indices of true gen Higgs jets
    int trueHiggsGenBJetId = genObjectIndices.genBjetFromHiggsIndex_;
    int trueHiggsGenAntiBJetId = genObjectIndices.genAntiBjetFromHiggsIndex_;

    // Filling the dijet mass of true reco jets from Higgs
    if(trueHiggsBJetId >= 0 && trueHiggsAntiBJetId >= 0) {
        LV dijet_trueH = allJets.at(trueHiggsBJetId) + allJets.at(trueHiggsAntiBJetId);
        m_histogram["dijet_mass_trueHiggsJets"]->Fill(dijet_trueH.M(), weight);
    }

    // Filling the dijet mass of true gen jets from Higgs
    if(trueHiggsGenBJetId >= 0 && trueHiggsGenAntiBJetId >= 0) {
        LV dijet_genH = genJets.at(trueHiggsGenBJetId) + genJets.at(trueHiggsGenAntiBJetId);
        m_histogram["dijet_mass_genHiggsJets"]->Fill(dijet_genH.M(), weight);
    }


    int nTopJetsInAllTrue=0;
    int nTopJetsInTrue=0;
    // Selecting b-tagged jets among top jets from KinReco
    for(unsigned int iJet=0, iJetN=topJetsId.size(); iJet<iJetN; iJet++) {
        int iAllJet = topJetsId.at(iJet);
        if(isInVector(trueTopAllJetsId,iAllJet)) nTopJetsInAllTrue++;
        if(isInVector(trueTopJetsId,iAllJet)) nTopJetsInTrue++;
        if(!isInVector(bJetsId,iAllJet)) continue;
        topBJetsId.push_back(iAllJet);
    }


    // Identifying numbers of jets and b-jets
    unsigned int nAllJets = allJets.size();
    unsigned int nJets = jetsId.size();
    unsigned int nBJets = bJetsId.size();
    unsigned int nGenJets = genJets.size();


    // Analyzing selected jets
    int nJetsPtLt30 = 0;
    int nBJetsPtLt30 = 0;
    float bJet_dRmin = 999.9;
    for(unsigned int iJet = 0, iJetN=jetsId.size(); iJet<iJetN; iJet++) {
        unsigned int iAllJet = jetsId.at(iJet);
        LV jet = allJets.at(iAllJet);

        // Filling information about the jets
        m_histogram["jet_pt"]->Fill(jet.Pt(), weight);
        m_histogram["jet_eta"]->Fill(jet.Eta(), weight);
        m_histogram["jet_btagDiscriminator"]->Fill(allJetsBtagDiscriminant.at(iAllJet), weight);

        // Filling information about b-tagged jets
        if(isInVector(bJetsId, iAllJet)) {
            m_histogram["bJet_pt"]->Fill(jet.Pt(), weight);
            m_histogram["bJet_eta"]->Fill(jet.Eta(), weight);
            m_histogram["bJet_btagDiscriminator"]->Fill(allJetsBtagDiscriminant.at(iAllJet), weight);

            // Checking dR between closest pair of reco b-jets
            for(unsigned int iJet2 = 0; iJet2<iJet; iJet2++) {
                unsigned int iAllJet2 = jetsId.at(iJet2);
                if(!isInVector(bJetsId, iAllJet2)) continue;
                LV jet2 = allJets.at(iAllJet2);
                float dR = ROOT::Math::VectorUtil::DeltaR(jet, jet2);
                if(dR<bJet_dRmin) bJet_dRmin = dR;
            }       // End of loop over all other reco b-jets
        }       // End of loop over all reco b-jets


        ////////////////////////////////////////////////////////////////// Analyzing only jets with Pt<30
        if(jet.Pt()>=30) continue;
        nJetsPtLt30++;
        m_histogram["jet_PtLt30_btagDiscriminator"]->Fill(allJetsBtagDiscriminant.at(iAllJet), weight);
        if(isInVector(bJetsId, iAllJet)) {
            nBJetsPtLt30++;
            m_histogram["bJet_PtLt30_btagDiscriminator"]->Fill(allJetsBtagDiscriminant.at(iAllJet), weight);
        }

        // Finding the corresponding genJetId and its flavours
        int genJetId = genJetIdOfRecoJet(jet, genJets);
        std::vector<int> flavJet = bHadFlavoursInGenJet(genJetId, bHadJetIndex, bHadFlavour, true);
        if(!isInVector(bJetsId,iAllJet)) continue;            // Skip jet if it is not b-tagged
        for(unsigned int iFlav = 0, iFlavN = flavJet.size(); iFlav<iFlavN; iFlav++) {
            m_histogram["jet_PtLt30_flavour"]->Fill(flavJet.at(iFlav), weight);
            if(!isInVector(bJetsId, iAllJet)) continue;          // Skip jet if it was assigned to the Top
            m_histogram["bJet_PtLt30_flavour"]->Fill(flavJet.at(iFlav), weight);
        }       // End of loop over flavours of the jet

    }       // End of loop over all reco jets in the event
    m_histogram["bJet_dRmin"]->Fill(bJet_dRmin, weight);


    m_histogram["allJet_multiplicity"]->Fill(nAllJets, weight);
    m_histogram["jet_multiplicity"]->Fill(nJets, weight);
    m_histogram["bJet_multiplicity"]->Fill(nBJets, weight);
    m_histogram["genJet_multiplicity"]->Fill(nGenJets, weight);
    m_histogram["topJet_multiplicity_allTrue"]->Fill(trueTopAllJetsId.size(), weight);
    m_histogram["topJet_multiplicity_true"]->Fill(trueTopJetsId.size(), weight);
    m_histogram["topJet_multiplicity_reco"]->Fill(topJetsId.size(), weight);
    m_histogram["topJet_multiplicity_recoInTrue"]->Fill(nTopJetsInTrue, weight);
    m_histogram["topJet_multiplicity_recoInAllTrue"]->Fill(nTopJetsInAllTrue, weight);
    m_histogram["topBJet_multiplicity_true"]->Fill(trueTopBJetsId.size(), weight);
    m_histogram["topBJet_multiplicity_reco"]->Fill(topBJetsId.size(), weight);
    m_histogram["higgsAllJet_multiplicity_true"]->Fill(trueHiggsAllJetsId.size(), weight);
    m_histogram["higgsJet_multiplicity_true"]->Fill(trueHiggsJetsId.size(), weight);
    m_histogram["higgsBJet_multiplicity_true"]->Fill(trueHiggsBJetsId.size(), weight);
    m_histogram["jet_PtLt30_multiplicity"]->Fill(nJetsPtLt30, weight);
    m_histogram["bJet_PtLt30_multiplicity"]->Fill(nBJetsPtLt30, weight);
    m_histogram["weight"]->Fill(weight, weight);

    // DeltaR between leptons, Met
    m_histogram["topLeptonAntilepton_dR"]->Fill(ROOT::Math::VectorUtil::DeltaR(lepton, antilepton));
    LV dilepton = lepton + antilepton;
    m_histogram["topDiLeptonMet_dR"]->Fill(ROOT::Math::VectorUtil::DeltaR(dilepton, met));


    std::vector<int> emptyVector;

    /////////////////////////////////////////////////////////////////// FILLING DIJET MASS FOR DIFFERENT JET SELECTIONS
    const bool fillAllCombinations = true;
    ///////////////////////////////////////////////////////////////////////////////////////////////// ALL SELECTED JETS
    // Analyzing jet pairs for all jet combinations
    float correctPairFraction_all = correctPairFraction(allJets, jetsId, bJetsId, allJetsBtagDiscriminant, emptyVector, trueHiggsJetsId, weight, m_histogram["dijet_mass_all"], m_histogram["dijet_correctJet_multiplicity_all"], fillAllCombinations);
    m_histogram["dijet_correctPairFraction_all"]->Fill(correctPairFraction_all, weight);

    // Analyzing jet pairs for all jet combinations of jets tagged with CSVM
    std::vector<int> bMJetsId;
    for(int jetId : bJetsId) { if(allJetsBtagDiscriminant.at(jetId)>=0.679) bMJetsId.push_back(jetId); };
    float correctPairFraction_allM = correctPairFraction(allJets, jetsId, bMJetsId, allJetsBtagDiscriminant, emptyVector, trueHiggsJetsId, weight, m_histogram["dijet_mass_allM"], m_histogram["dijet_correctJet_multiplicity_allM"], fillAllCombinations);
    m_histogram["dijet_correctPairFraction_allM"]->Fill(correctPairFraction_allM, weight);

    // Analyzing jet pairs for all jet combinations except true b-jets from top
    float correctPairFraction_trueTopJets = correctPairFraction(allJets, jetsId, bJetsId, allJetsBtagDiscriminant, trueTopJetsId, trueHiggsJetsId, weight, m_histogram["dijet_mass_trueTopJets"], m_histogram["dijet_correctJet_multiplicity_trueTopJets"], fillAllCombinations);
    m_histogram["dijet_correctPairFraction_trueTopJets"]->Fill(correctPairFraction_trueTopJets, weight);

    // Analyzing jet pairs for all jet combinations except reco b-jets from top found by kinematic reconstruction
    float correctPairFraction_recoTopJets = correctPairFraction(allJets, jetsId, bJetsId, allJetsBtagDiscriminant, topJetsId, trueHiggsJetsId, weight, m_histogram["dijet_mass_recoTopJets"], m_histogram["dijet_correctJet_multiplicity_recoTopJets"], fillAllCombinations);
    m_histogram["dijet_correctPairFraction_recoTopJets"]->Fill(correctPairFraction_recoTopJets, weight);


    ///////////////////////////////////////////////////////////////////////////////////////////////// SELECTED JETS [PT>=30]
    // Building list of jets with Pt >= 30
    std::vector<int> jetsIdPtGe30;
    for(int id : jetsId) { if( allJets.at(id).Pt() >= 30.f ) jetsIdPtGe30.push_back(id); }
    // Analyzing jet pairs for all jet combinations
    float correctPairFraction_all_jetPtGe30 = correctPairFraction(allJets, jetsIdPtGe30, bJetsId, allJetsBtagDiscriminant, emptyVector, trueHiggsJetsId, weight, m_histogram["dijet_mass_all_jetPtGe30"], m_histogram["dijet_correctJet_multiplicity_all_jetPtGe30"], fillAllCombinations);
    m_histogram["dijet_correctPairFraction_all_jetPtGe30"]->Fill(correctPairFraction_all_jetPtGe30, weight);

    // Analyzing jet pairs for all jet combinations of jets tagged with CSVM
    float correctPairFraction_allM_jetPtGe30 = correctPairFraction(allJets, jetsIdPtGe30, bMJetsId, allJetsBtagDiscriminant, emptyVector, trueHiggsJetsId, weight, m_histogram["dijet_mass_allM_jetPtGe30"], m_histogram["dijet_correctJet_multiplicity_allM_jetPtGe30"], fillAllCombinations);
    m_histogram["dijet_correctPairFraction_allM_jetPtGe30"]->Fill(correctPairFraction_allM_jetPtGe30, weight);

    // Analyzing jet pairs for all jet combinations except true b-jets from top
    float correctPairFraction_trueTopJets_jetPtGe30 = correctPairFraction(allJets, jetsIdPtGe30, bJetsId, allJetsBtagDiscriminant, trueTopJetsId, trueHiggsJetsId, weight, m_histogram["dijet_mass_trueTopJets_jetPtGe30"], m_histogram["dijet_correctJet_multiplicity_trueTopJets_jetPtGe30"], fillAllCombinations);
    m_histogram["dijet_correctPairFraction_trueTopJets_jetPtGe30"]->Fill(correctPairFraction_trueTopJets_jetPtGe30, weight);

    // Analyzing jet pairs for all jet combinations except reco b-jets from top found by kinematic reconstruction
    float correctPairFraction_recoTopJets_jetPtGe30 = correctPairFraction(allJets, jetsIdPtGe30, bJetsId, allJetsBtagDiscriminant, topJetsId, trueHiggsJetsId, weight, m_histogram["dijet_mass_recoTopJets_jetPtGe30"], m_histogram["dijet_correctJet_multiplicity_recoTopJets_jetPtGe30"], fillAllCombinations);
    m_histogram["dijet_correctPairFraction_recoTopJets_jetPtGe30"]->Fill(correctPairFraction_recoTopJets_jetPtGe30, weight);


    ///////////////////////////////////////////////////////////////////////////////////////////////// SELECTED JETS [PT<30]
    // Building list of jets with Pt < 30
    std::vector<int> jetsIdPtLt30;
    for(int id : jetsId) { if( allJets.at(id).Pt() < 30.f ) jetsIdPtLt30.push_back(id); }
    // Analyzing jet pairs for all jet combinations
    float correctPairFraction_all_jetPtLt30 = correctPairFraction(allJets, jetsIdPtLt30, bJetsId, allJetsBtagDiscriminant, emptyVector, trueHiggsJetsId, weight, m_histogram["dijet_mass_all_jetPtLt30"], m_histogram["dijet_correctJet_multiplicity_all_jetPtLt30"], fillAllCombinations);
    m_histogram["dijet_correctPairFraction_all_jetPtLt30"]->Fill(correctPairFraction_all_jetPtLt30, weight);

    // Analyzing jet pairs for all jet combinations of jets tagged with CSVM
    float correctPairFraction_allM_jetPtLt30 = correctPairFraction(allJets, jetsIdPtLt30, bMJetsId, allJetsBtagDiscriminant, emptyVector, trueHiggsJetsId, weight, m_histogram["dijet_mass_allM_jetPtLt30"], m_histogram["dijet_correctJet_multiplicity_allM_jetPtLt30"], fillAllCombinations);
    m_histogram["dijet_correctPairFraction_allM_jetPtLt30"]->Fill(correctPairFraction_allM_jetPtLt30, weight);

    // Analyzing jet pairs for all jet combinations except true b-jets from top
    float correctPairFraction_trueTopJets_jetPtLt30 = correctPairFraction(allJets, jetsIdPtLt30, bJetsId, allJetsBtagDiscriminant, trueTopJetsId, trueHiggsJetsId, weight, m_histogram["dijet_mass_trueTopJets_jetPtLt30"], m_histogram["dijet_correctJet_multiplicity_trueTopJets_jetPtLt30"], fillAllCombinations);
    m_histogram["dijet_correctPairFraction_trueTopJets_jetPtLt30"]->Fill(correctPairFraction_trueTopJets_jetPtLt30, weight);

    // Analyzing jet pairs for all jet combinations except reco b-jets from top found by kinematic reconstruction
    float correctPairFraction_recoTopJets_jetPtLt30 = correctPairFraction(allJets, jetsIdPtLt30, bJetsId, allJetsBtagDiscriminant, topJetsId, trueHiggsJetsId, weight, m_histogram["dijet_mass_recoTopJets_jetPtLt30"], m_histogram["dijet_correctJet_multiplicity_recoTopJets_jetPtLt30"], fillAllCombinations);
    m_histogram["dijet_correctPairFraction_recoTopJets_jetPtLt30"]->Fill(correctPairFraction_recoTopJets_jetPtLt30, weight);


    // Counting number of gen b-jets
    int nGenBjets = 0;
    int nGenBhads = bHadJetIndex.size();
    int nGenBhadsNoG = 0;
    int nGenBhadsNoT = 0;
    int nGenBhadsT = 0;
    int nGenBhadsH = 0;
    float genBJet_dRmin = 999.9;
    // Finding jets that are matched to b-hadrons
    for(unsigned int iJet=0, nJets=genJets.size(); iJet<nJets; iJet++) {
        if(!isInVector(bHadJetIndex, iJet)) continue;
        nGenBjets++;
        m_histogram["genBJet_pt"]->Fill(genJets.at(iJet).Pt(), weight);
        m_histogram["genBJet_eta"]->Fill(genJets.at(iJet).Eta(), weight);

        // Checking dR between the closest pair of gen b-jets
        for(unsigned int iJet2=0; iJet2<iJet; iJet2++) {
            if(!isInVector(bHadJetIndex, iJet2)) continue;
            float dR = ROOT::Math::VectorUtil::DeltaR(genJets.at(iJet), genJets.at(iJet2));
            if(dR<genBJet_dRmin) genBJet_dRmin = dR;
        }       // End of loop over all other gen b-jets

        float genBJet_recoJet_dRmin = 999.9;
        float genBJet_recoBJet_dRmin = 999.9;
        // Checking dR between each gen b-jet and closest reco jet
        for(unsigned int iJet2 = 0; iJet2<jetsId.size(); iJet2++) {
            unsigned int iAllJet2 = jetsId.at(iJet2);
            LV jet2 = allJets.at(iAllJet2);
            float dR = ROOT::Math::VectorUtil::DeltaR(genJets.at(iJet), jet2);
            if(dR<genBJet_recoJet_dRmin) genBJet_recoJet_dRmin = dR;
            if(!isInVector(bJetsId, iAllJet2)) continue;
            float dR_b = ROOT::Math::VectorUtil::DeltaR(genJets.at(iJet), jet2);
            if(dR_b<genBJet_recoBJet_dRmin) genBJet_recoBJet_dRmin = dR_b;
        }       // End of loop over all reco b-jets
        m_histogram["genBJet_recoJet_dRmin"]->Fill(genBJet_recoJet_dRmin, weight);
        m_histogram["genBJet_recoBJet_dRmin"]->Fill(genBJet_recoBJet_dRmin, weight);

    }       // End of loop over all gen b-jets
    m_histogram["genBJet_dRmin"]->Fill(genBJet_dRmin, weight);

    float bHad_dRmin = 999.9;
    // Getting number of hadrons of different flavours
    for(unsigned int iHad=0, nHads=bHadFlavour.size(); iHad<nHads; iHad++) {
        if(std::abs(bHadFlavour.at(iHad))!=21) nGenBhadsNoG++;
        if(std::abs(bHadFlavour.at(iHad))!=6) nGenBhadsNoT++;
        if(std::abs(bHadFlavour.at(iHad))==6) nGenBhadsT++;
        if(std::abs(bHadFlavour.at(iHad))==25) nGenBhadsH++;
        m_histogram["bHad_flavour"]->Fill(bHadFlavour.at(iHad), weight);

        LV had1 = bHadLVs.at(iHad);
        for(unsigned int iHad2=0; iHad2<iHad; iHad2++) {
            LV had2 = bHadLVs.at(iHad2);
            float dR = ROOT::Math::VectorUtil::DeltaR(had1, had2);
            if(dR<bHad_dRmin) bHad_dRmin = dR;
        }
    }
    m_histogram["bHad_dRmin"]->Fill(bHad_dRmin, weight);

    m_histogram["genBJet_multiplicity"]->Fill(nGenBjets, weight);
    m_histogram["bHad_multiplicity"]->Fill(nGenBhads, weight);
    m_histogram["bHad_top_multiplicity"]->Fill(nGenBhadsT, weight);
    m_histogram["bHad_higgs_multiplicity"]->Fill(nGenBhadsH, weight);
    m_histogram["bHadNoG_multiplicity"]->Fill(nGenBhadsNoG, weight);
    ((TH2*)m_histogram["bHadVsBJet_multiplicity"])->Fill(nGenBhads, nBJets, weight);
    ((TH2*)m_histogram["bHadVsBHadNoT_multiplicity"])->Fill(nGenBhads, nGenBhadsNoT, weight);


    ///////////////////////////////////////////////////////////////////////// COMPARISON OF GEN MATCHING AND dR MATCHING
    // Finding the closest b-hadrons to the b-quarks
    LV* bQt = topGenObjects.GenB_;
    LV* bQat = topGenObjects.GenAntiB_;
    LV* bQh = higgsGenObjects.GenBFromH_;
    LV* bQah = higgsGenObjects.GenAntiBFromH_;
    int bHt_id=-1;
    int bHat_id=-1;
    int bHh_id=-1;
    int bHah_id=-1;
    float dRQHt_min = 999.9;
    float dRQHat_min = 999.9;
    float dRQHh_min = 999.9;
    float dRQHah_min = 999.9;
    int bHt_id_05=-1;
    int bHat_id_05=-1;
    int bHh_id_05=-1;
    int bHah_id_05=-1;
    float dRQHt_min_05 = 0.5;
    float dRQHat_min_05 = 0.5;
    float dRQHh_min_05 = 0.5;
    float dRQHah_min_05 = 0.5;
    std::vector<int> bHt_unique_ids_dR(0);
    std::vector<int> bHh_unique_ids_dR(0);
    std::vector<int> bHth_unique_ids_dR(0);
    std::vector<int> bHt_unique_ids_dR_05(0);
    std::vector<int> bHh_unique_ids_dR_05(0);
    std::vector<int> bHth_unique_ids_dR_05(0);
    std::vector<int> bHt_unique_ids_matched(0);
    std::vector<int> bHh_unique_ids_matched(0);
    std::vector<int> bHth_unique_ids_matched(0);
    std::vector<int> bJt_unique_ids_dR(0);
    std::vector<int> bJh_unique_ids_dR(0);
    std::vector<int> bJth_unique_ids_dR(0);
    std::vector<int> bJt_unique_ids_dR_05(0);
    std::vector<int> bJh_unique_ids_dR_05(0);
    std::vector<int> bJth_unique_ids_dR_05(0);
    std::vector<int> bJt_unique_ids_matched(0);
    std::vector<int> bJh_unique_ids_matched(0);
    std::vector<int> bJth_unique_ids_matched(0);

    // Looping over all b-hadrons in the event to find closest ones
    using ROOT::Math::VectorUtil::DeltaR;
    for(int iHad = 0; iHad < (int)bHadLVs.size(); iHad++ ) {
        LV bHadLV = bHadLVs.at(iHad);
        float dRQHt = bQt?DeltaR(*bQt, bHadLV):1000.f;
        float dRQHat = bQat?DeltaR(*bQat, bHadLV):1000.f;
        float dRQHh = bQh?DeltaR(*bQh, bHadLV):1000.f;
        float dRQHah = bQah?DeltaR(*bQah, bHadLV):1000.f;
        if(dRQHt < dRQHt_min)   {dRQHt_min = dRQHt; bHt_id = iHad;}
        if(dRQHat < dRQHat_min) {dRQHat_min = dRQHat; bHat_id = iHad;}
        if(dRQHh < dRQHh_min)   {dRQHh_min = dRQHh; bHh_id = iHad;}
        if(dRQHah < dRQHah_min) {dRQHah_min = dRQHah; bHah_id = iHad;}
        if(dRQHt < dRQHt_min_05)   {dRQHt_min_05 = dRQHt; bHt_id_05 = iHad;}
        if(dRQHat < dRQHat_min_05) {dRQHat_min_05 = dRQHat; bHat_id_05 = iHad;}
        if(dRQHh < dRQHh_min_05)   {dRQHh_min_05 = dRQHh; bHh_id_05 = iHad;}
        if(dRQHah < dRQHah_min_05) {dRQHah_min_05 = dRQHah; bHah_id_05 = iHad;}

        // Filling multiplicity of unique hadrons and dR to closest quark
        switch(bHadFlavour.at(iHad)) {
            case 6:
                bHt_unique_ids_matched.push_back(iHad);
                if(bQt) m_histogram["bQuarkT_bHad_dRmatched"]->Fill(DeltaR(*bQt, bHadLV), weight);
                if(!isInVector(bHth_unique_ids_matched, iHad)) bHth_unique_ids_matched.push_back(iHad);
                break;
            case -6:
                bHt_unique_ids_matched.push_back(iHad);
                if(bQat) m_histogram["bQuarkT_bHad_dRmatched"]->Fill(DeltaR(*bQat, bHadLV), weight);
                if(!isInVector(bHth_unique_ids_matched, iHad)) bHth_unique_ids_matched.push_back(iHad);
                break;
            case 25:
                bHh_unique_ids_matched.push_back(iHad);
                if(bQh) m_histogram["bQuarkH_bHad_dRmatched"]->Fill(DeltaR(*bQh, bHadLV), weight);
                if(!isInVector(bHth_unique_ids_matched, iHad)) bHth_unique_ids_matched.push_back(iHad);
                break;
            case -25:
                bHh_unique_ids_matched.push_back(iHad);
                if(bQah) m_histogram["bQuarkH_bHad_dRmatched"]->Fill(DeltaR(*bQah, bHadLV), weight);
                if(!isInVector(bHth_unique_ids_matched, iHad)) bHth_unique_ids_matched.push_back(iHad);
                break;
            default:
                break;
        }

        int flavour = bHadFlavour.at(iHad);
        int flavourAbs = std::abs(flavour);

        if(flavourAbs!=6 && flavourAbs!=25 && flavourAbs!=21) continue;

        // Finding the closest gen jet
        int genJetId_matched = bHadJetIndex.at(iHad);
        float dR_min = 999.9;
        float dR_min_05 = 0.5;
        int genJetId_dR = -1;
        int genJetId_dR_05 = -1;
        for(int iJet = 0; iJet < (int)genJets.size(); iJet++) {
            float dR = DeltaR(bHadLV, genJets.at(iJet));
            if(dR<dR_min) {
                dR_min = dR;
                genJetId_dR = iJet;
            }
            if(dR<dR_min_05) {
                dR_min_05 = dR;
                genJetId_dR_05 = iJet;
            }
        }       // End of loop over gen Jets

        // Filling dR to matched and closest jets
        switch(flavourAbs) {
            case 6:
                if(genJetId_dR>=0) {
                    m_histogram["bHadT_genJet_dRmin"]->Fill(dR_min, weight);
                    if(!isInVector(bJt_unique_ids_dR, genJetId_dR)) bJt_unique_ids_dR.push_back(genJetId_dR);
                    if(!isInVector(bJth_unique_ids_dR, genJetId_dR)) bJth_unique_ids_dR.push_back(genJetId_dR);
                    if(flavour<0 && bQat) m_histogram["bQuarkT_genJet_dRmin"]->Fill(DeltaR(*bQat, genJets.at(genJetId_dR))); else
                        if(flavour>0 && bQt) m_histogram["bQuarkT_genJet_dRmin"]->Fill(DeltaR(*bQt, genJets.at(genJetId_dR)));

                    if(isInVector(bHt_unique_ids_dR_05, iHad) && genJetId_dR_05>=0) {
                        if(!isInVector(bJt_unique_ids_dR_05, genJetId_dR_05)) bJt_unique_ids_dR_05.push_back(genJetId_dR_05);
                        if(!isInVector(bJth_unique_ids_dR_05, genJetId_dR_05)) bJth_unique_ids_dR_05.push_back(genJetId_dR_05);
                    }
                }
                if(genJetId_matched>=0) {
                    m_histogram["bHadT_genJet_dRmatched"]->Fill(DeltaR(bHadLV, genJets.at(genJetId_matched)), weight);
                    if(!isInVector(bJt_unique_ids_matched, genJetId_matched)) bJt_unique_ids_matched.push_back(genJetId_matched);
                    if(!isInVector(bJth_unique_ids_matched, genJetId_matched)) bJth_unique_ids_matched.push_back(genJetId_matched);
                    if(flavour<0 && bQat) m_histogram["bQuarkT_genJet_dRmatched"]->Fill(DeltaR(*bQat, genJets.at(genJetId_matched))); else
                        if(flavour>0 && bQt) m_histogram["bQuarkT_genJet_dRmatched"]->Fill(DeltaR(*bQt, genJets.at(genJetId_matched)));
                }
                break;
            case 25:
                if(genJetId_dR>=0) {
                    m_histogram["bHadH_genJet_dRmin"]->Fill(dR_min, weight);
                    if(!isInVector(bJh_unique_ids_dR, genJetId_dR)) bJh_unique_ids_dR.push_back(genJetId_dR);
                    if(!isInVector(bJth_unique_ids_dR, genJetId_dR)) bJth_unique_ids_dR.push_back(genJetId_dR);
                    if(flavour<0 && bQah) m_histogram["bQuarkH_genJet_dRmin"]->Fill(DeltaR(*bQah, genJets.at(genJetId_dR))); else
                        if(flavour>0 && bQh) m_histogram["bQuarkH_genJet_dRmin"]->Fill(DeltaR(*bQh, genJets.at(genJetId_dR)));

                    if(isInVector(bHh_unique_ids_dR_05, iHad) && genJetId_dR_05>=0) {
                        if(!isInVector(bJh_unique_ids_dR_05, genJetId_dR_05)) bJh_unique_ids_dR_05.push_back(genJetId_dR_05);
                        if(!isInVector(bJth_unique_ids_dR_05, genJetId_dR_05)) bJth_unique_ids_dR_05.push_back(genJetId_dR_05);
                    }
                }
                if(genJetId_matched>=0) {
                    m_histogram["bHadH_genJet_dRmatched"]->Fill(DeltaR(bHadLV, genJets.at(genJetId_matched)), weight);
                    if(!isInVector(bJh_unique_ids_matched, genJetId_dR)) bJh_unique_ids_matched.push_back(genJetId_matched);
                    if(!isInVector(bJth_unique_ids_matched, genJetId_dR)) bJth_unique_ids_matched.push_back(genJetId_dR);
                    if(flavour<0 && bQah) m_histogram["bQuarkH_genJet_dRmatched"]->Fill(DeltaR(*bQah, genJets.at(genJetId_matched))); else
                        if(flavour>0 && bQh) m_histogram["bQuarkH_genJet_dRmatched"]->Fill(DeltaR(*bQh, genJets.at(genJetId_matched)));
                }
                break;
            case 21:
                if(genJetId_dR>=0) m_histogram["bHadG_genJet_dRmin"]->Fill(dR_min, weight);
                if(genJetId_matched>=0) m_histogram["bHadG_genJet_dRmatched"]->Fill(DeltaR(bHadLV, genJets.at(genJetId_matched)), weight);
                break;
            default:
                break;
        }

    }       // End of loop over b-hadrons


    if(bHt_id >= 0) {
        if(bQt) m_histogram["bQuarkT_bHad_dRmin"]->Fill(DeltaR(*bQt, bHadLVs.at(bHt_id)), weight);
        if(!isInVector(bHt_unique_ids_dR, bHt_id)) bHt_unique_ids_dR.push_back(bHt_id);
        if(!isInVector(bHth_unique_ids_dR, bHt_id)) bHth_unique_ids_dR.push_back(bHt_id);
    }
    if(bHat_id >= 0) {
        if(bQat) m_histogram["bQuarkT_bHad_dRmin"]->Fill(DeltaR(*bQat, bHadLVs.at(bHat_id)), weight);
        if(!isInVector(bHt_unique_ids_dR, bHat_id)) bHt_unique_ids_dR.push_back(bHat_id);
        if(!isInVector(bHth_unique_ids_dR, bHat_id)) bHth_unique_ids_dR.push_back(bHat_id);
    }
    if(bHh_id >= 0) {
        if(bQh) m_histogram["bQuarkH_bHad_dRmin"]->Fill(DeltaR(*bQh, bHadLVs.at(bHh_id)), weight);
        if(!isInVector(bHh_unique_ids_dR, bHh_id)) bHh_unique_ids_dR.push_back(bHh_id);
        if(!isInVector(bHth_unique_ids_dR, bHh_id)) bHth_unique_ids_dR.push_back(bHh_id);
    }
    if(bHah_id >= 0) {
        if(bQah) m_histogram["bQuarkH_bHad_dRmin"]->Fill(DeltaR(*bQah, bHadLVs.at(bHah_id)), weight);
        if(!isInVector(bHh_unique_ids_dR, bHah_id)) bHh_unique_ids_dR.push_back(bHah_id);
        if(!isInVector(bHth_unique_ids_dR, bHah_id)) bHth_unique_ids_dR.push_back(bHah_id);
    }

    if(bHt_id_05 >= 0) {
        if(!isInVector(bHt_unique_ids_dR_05, bHt_id_05)) bHt_unique_ids_dR_05.push_back(bHt_id_05);
        if(!isInVector(bHth_unique_ids_dR_05, bHt_id_05)) bHth_unique_ids_dR_05.push_back(bHt_id_05);
    }
    if(bHat_id_05 >= 0) {
        if(!isInVector(bHt_unique_ids_dR_05, bHat_id_05)) bHt_unique_ids_dR_05.push_back(bHat_id_05);
        if(!isInVector(bHth_unique_ids_dR_05, bHat_id_05)) bHth_unique_ids_dR_05.push_back(bHat_id_05);
    }
    if(bHh_id_05 >= 0) {
        if(!isInVector(bHh_unique_ids_dR_05, bHh_id_05)) bHh_unique_ids_dR_05.push_back(bHh_id_05);
        if(!isInVector(bHth_unique_ids_dR_05, bHh_id_05)) bHth_unique_ids_dR_05.push_back(bHh_id_05);
    }
    if(bHah_id_05 >= 0) {
        if(!isInVector(bHh_unique_ids_dR_05, bHah_id_05)) bHh_unique_ids_dR_05.push_back(bHah_id_05);
        if(!isInVector(bHth_unique_ids_dR_05, bHah_id_05)) bHth_unique_ids_dR_05.push_back(bHah_id_05);
    }

    // Unique hadrons
    m_histogram["bHadT_unique_multiplicity_dR"]->Fill(bHt_unique_ids_dR.size());
    m_histogram["bHadH_unique_multiplicity_dR"]->Fill(bHh_unique_ids_dR.size());
    m_histogram["bHadTH_unique_multiplicity_dR"]->Fill(bHth_unique_ids_dR.size());

    m_histogram["bHadT_unique_multiplicity_dR_05"]->Fill(bHt_unique_ids_dR_05.size());
    m_histogram["bHadH_unique_multiplicity_dR_05"]->Fill(bHh_unique_ids_dR_05.size());
    m_histogram["bHadTH_unique_multiplicity_dR_05"]->Fill(bHth_unique_ids_dR_05.size());

    m_histogram["bHadT_unique_multiplicity_match"]->Fill(bHt_unique_ids_matched.size());
    m_histogram["bHadH_unique_multiplicity_match"]->Fill(bHh_unique_ids_matched.size());
    m_histogram["bHadTH_unique_multiplicity_match"]->Fill(bHth_unique_ids_matched.size());

    // Unique jets
    m_histogram["genJetT_unique_multiplicity_dR"]->Fill(bJt_unique_ids_dR.size());
    m_histogram["genJetH_unique_multiplicity_dR"]->Fill(bJh_unique_ids_dR.size());
    m_histogram["genJetTH_unique_multiplicity_dR"]->Fill(bJth_unique_ids_dR.size());

    m_histogram["genJetT_unique_multiplicity_dR_05"]->Fill(bJt_unique_ids_dR_05.size());
    m_histogram["genJetH_unique_multiplicity_dR_05"]->Fill(bJh_unique_ids_dR_05.size());
    m_histogram["genJetTH_unique_multiplicity_dR_05"]->Fill(bJth_unique_ids_dR_05.size());

    m_histogram["genJetT_unique_multiplicity_match"]->Fill(bJt_unique_ids_matched.size());
    m_histogram["genJetH_unique_multiplicity_match"]->Fill(bJh_unique_ids_matched.size());
    m_histogram["genJetTH_unique_multiplicity_match"]->Fill(bJth_unique_ids_matched.size());

//     if((int)bHt_unique_ids_dR.size() < 2) printf("nHadrons: %d\tnSelJets: %d\tnColesJets: %d\n", (int)bHt_unique_ids_dR.size(), (int)genJets.size(), (int)bJt_unique_ids_dR.size());


}


void DijetAnalyzer::bookHistos(const TString& step)
{
    constexpr const char* prefix = "dijet_";
    std::map<TString, TH1*>& m_histogram = m_stepHistograms_[step].m_histogram_;
    TString name;

    std::stringstream ss_label;
    TString categoryName = tth::extractJetCategory(step);
    if(categoryName != ""){
        categoryName.ReplaceAll("cate", "");
        int category = atoi(categoryName);
        ss_label<<" ["<<jetCategories_->binLabels().at(category)<<"]";
    }
    const TString label = ss_label.str();


    name = "allJet_multiplicity";
    m_histogram[name] = store(new TH1D(prefix+name+step, "All jet multiplicity;N jets_{all}"+label+";Events",20,0,20));
    name = "jet_multiplicity";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Jet multiplicity;N jets_{reco}"+label+";Events",20,0,20));
    name = "jet_pt";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Jet Pt;jet Pt{reco}"+label+";Jets",30,0,300));
    name = "jet_eta";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Jet Eta;jet #eta{reco}"+label+";Jets",30,-2.6,2.6));
    name = "jet_btagDiscriminator";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Jet btagDiscriminator d;jet d{reco}"+label+";Jets",36,-0.1,1.1));

    name = "bJet_multiplicity";
    m_histogram[name] = store(new TH1D(prefix+name+step, "B-jet multiplicity;N b-jets_{reco}"+label+";Events",20,0,20));
    name = "bJet_pt";
    m_histogram[name] = store(new TH1D(prefix+name+step, "B-jet Pt;bJet Pt{reco}"+label+";Jets",30,0,300));
    name = "bJet_eta";
    m_histogram[name] = store(new TH1D(prefix+name+step, "B-jet Eta;bJet #eta{reco}"+label+";Jets",30,-2.6,2.6));
    name = "bJet_btagDiscriminator";
    m_histogram[name] = store(new TH1D(prefix+name+step, "B-jet btagDiscriminator d;jet d{reco}"+label+";Jets",36,-0.1,1.1));
    name = "bJet_dRmin";
    m_histogram[name] = store(new TH1D(prefix+name+step, "B-jet dRmin;bJet dR_min{reco}"+label+";Events",50,0,3.5));

    name = "genJet_multiplicity";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Gen. jet multiplicity;N jets_{gen}"+label+";Events",50,0,50));
    name = "genBJet_multiplicity";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Gen. b-jet multiplicity;N(b-jet)_{gen}"+label+";Events",15,0,15));
    name = "genBJet_pt";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Gen. b-jet Pt;bJet Pt{gen}"+label+";Jets",30,0,300));
    name = "genBJet_eta";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Gen. b-jet Eta;bJet #eta{gen}"+label+";Jets",30,-2.6,2.6));
    name = "genBJet_dRmin";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Gen. b-jet dRmin;bJet dR_min{gen}"+label+";Events",50,0,3.5));
    name = "genBJet_recoJet_dRmin";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Gen. b-jet - Reco jet dRmin;bJet_{gen}-Jet_{reco} dR_min"+label+";Events",50,0,3.5));
    name = "genBJet_recoBJet_dRmin";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Gen. b-jet - Reco b-jet dRmin;bJet_{gen}-bJet_{reco} dR_min"+label+";Events",50,0,3.5));
    name = "bHad_multiplicity";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Gen. b-had multiplicity;N(b-had)_{gen}"+label+";Events",15,0,15));
    name = "bHad_top_multiplicity";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Gen. b-had multiplicity;N(b-had)_{gen}^{top}"+label+";Events",6,0,6));
    name = "bHad_higgs_multiplicity";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Gen. b-had multiplicity;N(b-had)_{gen}^{higgs}"+label+";Events",6,0,6));
    name = "bHad_flavour";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Gen. b-had flavour;Flavour(b-had)_{gen}"+label+";B-hadrons",60,-30,30));
    name = "bHad_dRmin";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Gen. b-had dRmin;dR_min(b-had)_{gen}"+label+";Jets",50,0,3.5));
    name = "bHadNoG_multiplicity";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Gen. b-had multiplicity (not from gluons);N(b-had NoG)_{gen}"+label+";Events",15,0,15));
    name = "bHadVsBJet_multiplicity";
    m_histogram[name] = store(new TH2D(prefix+name+step, "Gen. b-had/b-jet multiplicity;N(b-had)_{gen}"+label+";N(b-jet)_{reco}",15,0,15,15,0,15));
    name = "bHadVsBHadNoT_multiplicity";
    m_histogram[name] = store(new TH2D(prefix+name+step, "Gen. b-had/b-had^{not t#bar{t}} multiplicity;N(b-had)_{all}"+label+";N(b-had)_{not t#bar{t}}",15,0,15,15,0,15));

    name = "topJet_multiplicity_allTrue";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Top jet multiplicity (true);N jets_{top}^{true} (all)"+label+";Events",5,0,5));
    name = "topJet_multiplicity_true";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Top jet multiplicity (true);N jets_{top}^{true} (sel.)"+label+";Events",5,0,5));
    name = "topJet_multiplicity_reco";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Top jet multiplicity (reco);N jets_{top}^{reco} (sel.)"+label+";Events",5,0,5));
    name = "topJet_multiplicity_recoInAllTrue";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Top jet multiplicity (reco in true);N jets_{top}^{reco} (among all true)"+label+";Events",5,0,5));
    name = "topJet_multiplicity_recoInTrue";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Top jet multiplicity (reco in true);N jets_{top}^{reco} (among sel. true)"+label+";Events",5,0,5));
    name = "topBJet_multiplicity_true";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Top b-jet multiplicity (true);N b-tagged jets_{top}^{true} (sel. b-tagged)"+label+";Events",5,0,5));
    name = "topBJet_multiplicity_reco";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Top b-jet multiplicity (true);N b-tagged jets_{top}^{reco} (sel. b-tagged)"+label+";Events",5,0,5));
    name = "higgsAllJet_multiplicity_true";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Higgs jet multiplicity (true);N jets_{higgs}^{true} (all)"+label+";Events",5,0,5));
    name = "higgsJet_multiplicity_true";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Higgs jet multiplicity (true);N jets_{higgs}^{true} (sel.)"+label+";Events",5,0,5));
    name = "higgsBJet_multiplicity_true";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Higgs b-jet multiplicity (true);N b-tagged jets_{higgs}^{true} (sel. b-tagged)"+label+";Events",5,0,5));

    name = "topLeptonAntilepton_dR";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Top lepton - antiLepton dR;Lepton_{top}-Antilepton_{antitop} dR"+label+";Events",50,0,3.5));
    name = "topDiLeptonMet_dR";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Top diLepton - Met dR;diLepton_{top}-Met_{event} dR"+label+";Events",50,0,3.5));

    name = "dijet_correctJet_multiplicity_all";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Number of correct jets;N jets^{correct} (all)"+label+";Jet pairs",4,0,4));
    name = "dijet_correctJet_multiplicity_allM";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Number of correct jets;N jets^{correct} (all M)"+label+";Jet pairs",4,0,4));
    name = "dijet_correctJet_multiplicity_trueTopJets";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Number of correct jets;N jets^{correct} (trueTopJets)"+label+";Jet pairs",4,0,4));
    name = "dijet_correctJet_multiplicity_recoTopJets";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Number of correct jets;N jets^{correct} (recoTopJets)"+label+";Jet pairs",4,0,4));

    name = "dijet_correctJet_multiplicity_all_jetPtLt30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Number of correct jets;N jets^{correct}_{Pt<30} (all)"+label+";Jet pairs",4,0,4));
    name = "dijet_correctJet_multiplicity_allM_jetPtLt30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Number of correct jets;N jets^{correct}_{Pt<30} (all M)"+label+";Jet pairs",4,0,4));
    name = "dijet_correctJet_multiplicity_trueTopJets_jetPtLt30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Number of correct jets;N jets^{correct}_{Pt<30} (trueTopJets)"+label+";Jet pairs",4,0,4));
    name = "dijet_correctJet_multiplicity_recoTopJets_jetPtLt30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Number of correct jets;N jets^{correct}_{Pt<30} (recoTopJets)"+label+";Jet pairs",4,0,4));

    name = "dijet_correctJet_multiplicity_all_jetPtGe30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Number of correct jets;N jets^{correct}_{Pt>=30} (all)"+label+";Jet pairs",4,0,4));
    name = "dijet_correctJet_multiplicity_allM_jetPtGe30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Number of correct jets;N jets^{correct}_{Pt>=30} (all M)"+label+";Jet pairs",4,0,4));
    name = "dijet_correctJet_multiplicity_trueTopJets_jetPtGe30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Number of correct jets;N jets^{correct}_{Pt>=30} (trueTopJets)"+label+";Jet pairs",4,0,4));
    name = "dijet_correctJet_multiplicity_recoTopJets_jetPtGe30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Number of correct jets;N jets^{correct}_{Pt>=30} (recoTopJets)"+label+";Jet pairs",4,0,4));

    name = "dijet_correctPairFraction_all";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Correct pair fraction;correct/all (all)"+label+";Events",15,-0.3,1.2));
    name = "dijet_correctPairFraction_allM";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Correct pair fraction;correct/all (all M)"+label+";Events",15,-0.3,1.2));
    name = "dijet_correctPairFraction_trueTopJets";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Correct pair fraction;correct/all (trueTopJets)"+label+";Events",15,-0.3,1.2));
    name = "dijet_correctPairFraction_recoTopJets";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Correct pair fraction;correct/all (recoTopJets)"+label+";Events",15,-0.3,1.2));

    name = "dijet_correctPairFraction_all_jetPtLt30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Correct pair fraction;correct/all_{Pt<30} (all)"+label+";Events",15,-0.3,1.2));
    name = "dijet_correctPairFraction_allM_jetPtLt30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Correct pair fraction;correct/all_{Pt<30} (all M)"+label+";Events",15,-0.3,1.2));
    name = "dijet_correctPairFraction_trueTopJets_jetPtLt30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Correct pair fraction;correct/all_{Pt<30} (trueTopJets)"+label+";Events",15,-0.3,1.2));
    name = "dijet_correctPairFraction_recoTopJets_jetPtLt30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Correct pair fraction;correct/all_{Pt<30} (recoTopJets)"+label+";Events",15,-0.3,1.2));

    name = "dijet_correctPairFraction_all_jetPtGe30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Correct pair fraction;correct/all_{Pt>=30} (all)"+label+";Events",15,-0.3,1.2));
    name = "dijet_correctPairFraction_allM_jetPtGe30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Correct pair fraction;correct/all_{Pt>=30} (all M)"+label+";Events",15,-0.3,1.2));
    name = "dijet_correctPairFraction_trueTopJets_jetPtGe30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Correct pair fraction;correct/all_{Pt>=30} (trueTopJets)"+label+";Events",15,-0.3,1.2));
    name = "dijet_correctPairFraction_recoTopJets_jetPtGe30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Correct pair fraction;correct/all_{Pt>=30} (recoTopJets)"+label+";Events",15,-0.3,1.2));

    name = "dijet_mass_all";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Dijet mass;M(dijet) (all)"+label+";Jet pairs",25,0,500));
    name = "dijet_mass_allM";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Dijet mass;M(dijet) (all M)"+label+";Jet pairs",25,0,500));
    name = "dijet_mass_trueTopJets";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Dijet mass;M(dijet) (trueTopJets)"+label+";Jet pairs",25,0,500));
    name = "dijet_mass_recoTopJets";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Dijet mass;M(dijet) (recoTopJets)"+label+";Jet pairs",25,0,500));

    name = "dijet_mass_all_jetPtLt30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Dijet mass;M(dijet)_{Pt<30} (all)"+label+";Jet pairs",25,0,500));
    name = "dijet_mass_allM_jetPtLt30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Dijet mass;M(dijet)_{Pt<30} (all M)"+label+";Jet pairs",25,0,500));
    name = "dijet_mass_trueTopJets_jetPtLt30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Dijet mass;M(dijet)_{Pt<30} (trueTopJets)"+label+";Jet pairs",25,0,500));
    name = "dijet_mass_recoTopJets_jetPtLt30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Dijet mass;M(dijet)_{Pt<30} (recoTopJets)"+label+";Jet pairs",25,0,500));

    name = "dijet_mass_all_jetPtGe30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Dijet mass;M(dijet)_{Pt>=30} (all)"+label+";Jet pairs",25,0,500));
    name = "dijet_mass_allM_jetPtGe30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Dijet mass;M(dijet)_{Pt>=30} (all M)"+label+";Jet pairs",25,0,500));
    name = "dijet_mass_trueTopJets_jetPtGe30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Dijet mass;M(dijet)_{Pt>=30} (trueTopJets)"+label+";Jet pairs",25,0,500));
    name = "dijet_mass_recoTopJets_jetPtGe30";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Dijet mass;M(dijet)_{Pt>=30} (recoTopJets)"+label+";Jet pairs",25,0,500));

    name = "dijet_mass_trueHiggsJets";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Dijet mass;M(dijet)_{H} (true reco)"+label+";Jet pairs",25,0,500));
    name = "dijet_mass_genHiggsJets";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Dijet mass;M(dijet)_{H} (true gen)"+label+";Jet pairs",25,0,500));

    name = "jet_PtLt30_multiplicity";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Jet multiplicity (Pt<30);N jets_{reco}^{Pt<30}"+label+";Events",20,0,20));
    name = "bJet_PtLt30_multiplicity";
    m_histogram[name] = store(new TH1D(prefix+name+step, "B-jet multiplicity (Pt<30);N b-jets_{reco}^{Pt<30}"+label+";Events",20,0,20));
    name = "jet_PtLt30_flavour";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Jet flavour (Pt<30);flavour(jet)_{Pt<30}"+label+";Jets",30,0,30));
    name = "bJet_PtLt30_flavour";
    m_histogram[name] = store(new TH1D(prefix+name+step, "B-jet flavour (Pt<30);flavour(b-jet)_{Pt<30}"+label+";B-tagged jets",30,0,30));
    name = "jet_PtLt30_btagDiscriminator";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Jet btagDiscriminator d (Pt<30);d_{reco}^{Pt<30}"+label+";Jets",20,0,1));
    name = "bJet_PtLt30_btagDiscriminator";
    m_histogram[name] = store(new TH1D(prefix+name+step, "B-jet btagDiscriminator d (Pt<30);d_{reco}^{Pt<30}"+label+";B-tagged jets",20,0,1));

    name = "bQuarkT_bHad_dRmin";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Min. dR b-quark_{tt} ^ bHadron;dR(bQ,bHad)^{t}_{min}"+label+";b-quarks_{tt}",50,0,3.5));
    name = "bQuarkH_bHad_dRmin";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Min. dR b-quark_{H} ^ bHadron;dR(bQ,bHad)^{H}_{min}"+label+";b-quarks_{H}",50,0,3.5));
    name = "bQuarkT_bHad_dRmatched";
    m_histogram[name] = store(new TH1D(prefix+name+step, "dR b-quark_{tt} ^ bHadron_{tt};dR(bQ,bHad)^{t}_{matched}"+label+";b-quarks_{tt}",51,-0.07,3.5));
    name = "bQuarkH_bHad_dRmatched";
    m_histogram[name] = store(new TH1D(prefix+name+step, "dR b-quark_{H} ^ bHadron_{H};dR(bQ,bHad)^{H}_{matched}"+label+";b-quarks_{H}",51,-0.07,3.5));
    name = "bHadT_genJet_dRmin";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Min. dR b-hadron_{tt} ^ jet_{gen};dR(bHad,genJet)^{t}_{min}"+label+";b-hadrons_{tt}",50,0,3.5));
    name = "bHadH_genJet_dRmin";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Min. dR b-hadron_{H} ^ jet_{gen};dR(bHad,genJet)^{H}_{min}"+label+";b-hadrons_{H}",50,0,3.5));
    name = "bHadG_genJet_dRmin";
    m_histogram[name] = store(new TH1D(prefix+name+step, "dR b-hadron_{gluon} ^ jet_{gen};dR(bHad,genJet)^{g}_{min}"+label+";b-hadrons_{gluon}",50,0,3.5));
    name = "bHadT_genJet_dRmatched";
    m_histogram[name] = store(new TH1D(prefix+name+step, "dR b-hadron_{tt} ^ jet_{gen};dR(bHad,genJet)^{t}_{matched}"+label+";b-hadrons_{tt}",51,-0.07,3.5));
    name = "bHadH_genJet_dRmatched";
    m_histogram[name] = store(new TH1D(prefix+name+step, "dR b-hadron_{H} ^ jet_{gen};dR(bHad,genJet)^{H}_{matched}"+label+";b-hadrons_{H}",51,-0.07,3.5));
    name = "bHadG_genJet_dRmatched";
    m_histogram[name] = store(new TH1D(prefix+name+step, "dR b-hadron_{gluon} ^ jet_{gen};dR(bHad,genJet)^{g}_{matched}"+label+";b-hadrons_{gluon}",51,-0.07,3.5));
    name = "bQuarkT_genJet_dRmin";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Min. dR b-quark_{tt} ^ jet_{gen};dR(bQ,genJet)^{t}_{min}"+label+";b-quarks_{tt}",50,0,3.5));
    name = "bQuarkH_genJet_dRmin";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Min. dR b-quark_{H} ^ jet_{gen};dR(bQ,genJet)^{H}_{min}"+label+";b-quarks_{H}",50,0,3.5));
    name = "bQuarkT_genJet_dRmatched";
    m_histogram[name] = store(new TH1D(prefix+name+step, "dR b-quark_{tt} ^ jet_{gen};dR(bQ,genJet)^{t}_{matched}"+label+";b-quarks_{tt}",51,-0.07,3.5));
    name = "bQuarkH_genJet_dRmatched";
    m_histogram[name] = store(new TH1D(prefix+name+step, "dR b-quark_{H} ^ jet_{gen};dR(bQ,genJet)^{H}_{matched}"+label+";b-quarks_{H}",51,-0.07,3.5));

    name = "bHadT_unique_multiplicity_dR";
    m_histogram[name] = store(new TH1D(prefix+name+step, "B-hadron multiplicity (tt);N hadrons_{unique}^{tt} (dR)"+label+";Events",5,0,5));
    name = "bHadH_unique_multiplicity_dR";
    m_histogram[name] = store(new TH1D(prefix+name+step, "B-hadron multiplicity (H);N hadrons_{unique}^{H} (dR)"+label+";Events",5,0,5));
    name = "bHadTH_unique_multiplicity_dR";
    m_histogram[name] = store(new TH1D(prefix+name+step, "B-hadron multiplicity (ttH);N hadrons_{unique}^{ttH} (dR)"+label+";Events",5,0,5));
    name = "bHadT_unique_multiplicity_dR_05";
    m_histogram[name] = store(new TH1D(prefix+name+step, "B-hadron multiplicity (tt);N hadrons_{unique}^{tt} (dR<0.5)"+label+";Events",5,0,5));
    name = "bHadH_unique_multiplicity_dR_05";
    m_histogram[name] = store(new TH1D(prefix+name+step, "B-hadron multiplicity (H);N hadrons_{unique}^{H} (dR<0.5)"+label+";Events",5,0,5));
    name = "bHadTH_unique_multiplicity_dR_05";
    m_histogram[name] = store(new TH1D(prefix+name+step, "B-hadron multiplicity (ttH);N hadrons_{unique}^{ttH} (dR<0.5)"+label+";Events",5,0,5));
    name = "bHadT_unique_multiplicity_match";
    m_histogram[name] = store(new TH1D(prefix+name+step, "B-hadron multiplicity (tt);N hadrons_{unique}^{tt} (match)"+label+";Events",5,0,5));
    name = "bHadH_unique_multiplicity_match";
    m_histogram[name] = store(new TH1D(prefix+name+step, "B-hadron multiplicity (H);N hadrons_{unique}^{H} (match)"+label+";Events",5,0,5));
    name = "bHadTH_unique_multiplicity_match";
    m_histogram[name] = store(new TH1D(prefix+name+step, "B-hadron multiplicity (ttH);N hadrons_{unique}^{ttH} (match)"+label+";Events",5,0,5));
    name = "genJetT_unique_multiplicity_dR";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Jet_{gen} multiplicity (tt);N genJets_{unique}^{tt} (dR)"+label+";Events",5,0,5));
    name = "genJetH_unique_multiplicity_dR";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Jet_{gen} multiplicity (H);N genJets_{unique}^{H} (dR)"+label+";Events",5,0,5));
    name = "genJetTH_unique_multiplicity_dR";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Jet_{gen} multiplicity (ttH);N genJets_{unique}^{ttH} (dR)"+label+";Events",5,0,5));
    name = "genJetT_unique_multiplicity_dR_05";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Jet_{gen} multiplicity (tt);N genJets_{unique}^{tt} (dR<0.5)"+label+";Events",5,0,5));
    name = "genJetH_unique_multiplicity_dR_05";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Jet_{gen} multiplicity (H);N genJets_{unique}^{H} (dR<0.5)"+label+";Events",5,0,5));
    name = "genJetTH_unique_multiplicity_dR_05";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Jet_{gen} multiplicity (ttH);N genJets_{unique}^{ttH} (dR<0.5)"+label+";Events",5,0,5));
    name = "genJetT_unique_multiplicity_match";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Jet_{gen} multiplicity (tt);N genJets_{unique}^{tt} (match)"+label+";Events",5,0,5));
    name = "genJetH_unique_multiplicity_match";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Jet_{gen} multiplicity (H);N genJets_{unique}^{H} (match)"+label+";Events",5,0,5));
    name = "genJetTH_unique_multiplicity_match";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Jet_{gen} multiplicity (ttH);N genJets_{unique}^{ttH} (match)"+label+";Events",5,0,5));


    name = "weight";
    m_histogram[name] = store(new TH1D(prefix+name+step, "Weight of the event;weight"+label+";Events",30,0,3));

}


float DijetAnalyzer::correctPairFraction(const VLV& allJets, const std::vector<int>& jetsId,
                                         const std::vector<int>& bJetsId, const std::vector<double>& jetsBtagDiscriminant,
                                         const std::vector<int>& topJetsId, const std::vector<int>& higgsJetsId,
                                         const double weight, TH1* h_dijetMass, TH1* h_correctJetMultiplicity, bool fillAllCombinations)
{
    unsigned int nJets = jetsId.size();
    int nCorrectJetPairs = 0;
    int nAllJetPairs = 0;


    std::vector<int> higgsJetCandidatesId(0);

    for(unsigned int iJet1 = 0; iJet1<nJets; iJet1++) {
        const int iAllJet1 = jetsId.at(iJet1);
        if(isInVector(topJetsId, iAllJet1)) continue;              // Skip jet if it was assigned to the Top
        if(!isInVector(bJetsId, iAllJet1)) continue;               // Skip jet if it is not b-tagged

        for(unsigned int iJet2 = 0; iJet2<iJet1; iJet2++) {
            const int iAllJet2 = jetsId.at(iJet2);
            if(isInVector(topJetsId, iAllJet2)) continue;          // Skip jet if it was assigned to the Top
            if(!isInVector(bJetsId, iAllJet2)) continue;           // Skip jet if it is not b-tagged

            int nCorrectJets = 0;
            if(fillAllCombinations) {
                // Filling the dijet mass
                LV dijet = allJets.at(iAllJet1) + allJets.at(iAllJet2);
                h_dijetMass->Fill(dijet.M(), weight);

                if(isInVector(higgsJetsId, iAllJet1)) nCorrectJets++;
                if(isInVector(higgsJetsId, iAllJet2)) nCorrectJets++;
                // Filling the number of correct jets in the dijet pair
                h_correctJetMultiplicity->Fill(nCorrectJets, weight);
            }       // If fill all combinations of jets

            // Adding the 2 jets to the list of candidates for b-jets from Higgs
            if(!isInVector(higgsJetCandidatesId,iAllJet1)) higgsJetCandidatesId.push_back(iAllJet1);
            if(!isInVector(higgsJetCandidatesId,iAllJet2)) higgsJetCandidatesId.push_back(iAllJet2);

            // Updating the number of correct/wrong pairs
            if(nCorrectJets>=2) nCorrectJetPairs++;
            nAllJetPairs++;

        }       // End of the second loop over jets
    }       // End of the first loop over jets

    float correctPairFraction;
    if(higgsJetCandidatesId.size()<2) {
        correctPairFraction = -0.19;                   // If less than 2 true Higgs jets in acceptance
        return correctPairFraction;
    }

    correctPairFraction = (float)nCorrectJetPairs/nAllJetPairs;
//     if(bJetsId.size()>3 && topJetsId.size()==0) printf("All: %d\tCor: %d\tFrac: %.2f\n",nAllJetPairs,nCorrectJetPairs,correctPairFraction);

    if(higgsJetsId.size()<2) correctPairFraction = -0.09;          // If less than 2 candidates were found

    // Stopping if best combination is not needed
    if(fillAllCombinations) return correctPairFraction;

    // Finding the two jets that are assumed to come from the Higgs
    // Ordering jets by b-tagging discriminant if there are more than 2 of them
    if(higgsJetCandidatesId.size()>2) ttbar::orderIndices(higgsJetCandidatesId, jetsBtagDiscriminant);
    LV dijet = allJets.at(higgsJetCandidatesId.at(0)) + allJets.at(higgsJetCandidatesId.at(1));
    h_dijetMass->Fill(dijet.M(), weight);


    // Counting the number of correct higgs jets among the candidates
    int nCorrectJets = 0;
    for(unsigned int iJet=0; iJet<higgsJetsId.size(); iJet++) {
        int allJetId = higgsJetsId.at(iJet);
        if(!isInVector(higgsJetCandidatesId, allJetId)) continue;
        nCorrectJets++;
    }
    h_correctJetMultiplicity->Fill(nCorrectJets, weight);

    if(higgsJetsId.size()>=2)  {
        correctPairFraction = (int)(isInVector(higgsJetsId, higgsJetCandidatesId.at(0)) && isInVector(higgsJetsId, higgsJetCandidatesId.at(1)));
    }

    return correctPairFraction;
}


int DijetAnalyzer::genJetIdOfRecoJet(const LV& recoJet, const VLV& genJets, const float dR_max)
{
    float dR_min = 999.9;
    int genJetId = -1;
    // Loop over gen jets to find the closest one to reco jet
    for(unsigned int iJet=0, nJets=genJets.size(); iJet<nJets; iJet++) {
        float dR = ROOT::Math::VectorUtil::DeltaR(recoJet,genJets.at(iJet));
        if(dR>=dR_min) continue;
        if(dR>=dR_max) continue;
        dR_min = dR;
        genJetId = iJet;
    }

    return genJetId;
}


std::vector<int> DijetAnalyzer::bHadIdsInGenJet(const int jetId, const std::vector<int>& hadJetIndices)
{
    std::vector<int> hadIndices;

    if(jetId<0) return hadIndices;

    for(unsigned int iHad=0, nHads=hadJetIndices.size(); iHad<nHads; iHad++) {
        if(hadJetIndices.at(iHad)!=jetId) continue;
        hadIndices.push_back(iHad);
    }

    return hadIndices;
}


std::vector<int> DijetAnalyzer::bHadFlavoursInGenJet(const int jetId, const std::vector<int>& hadJetIndices,
                                                     const std::vector<int>& hadFlavours, const bool absFlavour)
{
    std::vector<int> flavours;
    std::vector<int> hadIndices = bHadIdsInGenJet(jetId, hadJetIndices);

    for(unsigned int iHad=0, nHads=hadIndices.size(); iHad<nHads; iHad++) {
        int hadId = hadIndices.at(iHad);
        int flavour = hadFlavours.at(hadId);
        if(absFlavour) flavour = std::abs(flavour);

        if(isInVector(flavours,flavour)) continue;

        flavours.push_back(flavour);
    }

    return flavours;
}


bool DijetAnalyzer::isInVector(const std::vector<int>& idVector, const int id)
{
    bool isIn = std::find(idVector.begin(), idVector.end(), id) != idVector.end();

    return isIn;
}



