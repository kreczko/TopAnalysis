#include <iostream>
#include <cstdlib>

#include <TString.h>

#include "sampleHelpers.h"






// --- Functions defined in namespace Systematic ---


Systematic::Systematic
Systematic::convertSystematic(const std::string& systematic){
    if(systematic == "Nominal") return nominal;
    if(systematic == "mH110") return mH110;
    if(systematic == "mH115") return mH115;
    if(systematic == "mH120") return mH120;
    if(systematic == "mH1225") return mH1225;
    if(systematic == "mH1275") return mH1275;
    if(systematic == "mH130") return mH130;
    if(systematic == "mH135") return mH135;
    if(systematic == "mH140") return mH140;
    std::cout<<"Warning! The following systematic conversion is not implemented: "<<systematic<<std::endl;
    return undefined;
}


std::string
Systematic::convertSystematic(const Systematic& systematic){
    if(systematic == nominal) return "Nominal";
    if(systematic == mH110) return "mH110";
    if(systematic == mH115) return "mH115";
    if(systematic == mH120) return "mH120";
    if(systematic == mH1225) return "mH1225";
    if(systematic == mH1275) return "mH1275";
    if(systematic == mH130) return "mH130";
    if(systematic == mH135) return "mH135";
    if(systematic == mH140) return "mH140";
    if(systematic == undefined) return "";
    std::cout<<"Error! Systematic conversion is not implemented, break...\n"<<std::endl;
    exit(99);
}


std::vector<Systematic::Systematic>
Systematic::convertSystematics(const std::vector<std::string>& systematics){
    std::vector<Systematic> v_systematic;
    for(auto systematic : systematics)v_systematic.push_back(convertSystematic(systematic));
    return v_systematic;
}


std::vector<std::string>
Systematic::convertSystematics(const std::vector<Systematic>& systematics){
    std::vector<std::string> v_systematic;
    for(auto systematic : systematics)v_systematic.push_back(convertSystematic(systematic));
    return v_systematic;
}








// --- Functions defined in namespace Channel ---


Channel::Channel 
Channel::convertChannel(const std::string& channel){
    if(channel == "ee") return ee;
    if(channel == "emu") return emu;
    if(channel == "mumu") return mumu;
    if(channel == "combined") return combined;
    std::cout<<"Warning! The following channel conversion is not implemented: "<<channel<<std::endl;
    return undefined;
}


std::string
Channel::convertChannel(const Channel& channel){
    if(channel == ee) return "ee";
    if(channel == emu) return "emu";
    if(channel == mumu) return "mumu";
    if(channel == combined) return "combined";
    if(channel == undefined) return "";
    std::cout<<"Error! Channel conversion is not implemented, break...\n"<<std::endl;
    exit(98);
}


std::string
Channel::channelLabel(const Channel& channel){
    if(channel == ee) return "ee";
    if(channel == emu) return "e#mu";
    if(channel == mumu) return "#mu#mu";
    if(channel == combined) return "Dilepton Combined";
    if(channel == undefined) return "";
    std::cout<<"Error! Channel label is not implemented, break...\n"<<std::endl;
    exit(97);
}


std::vector<Channel::Channel>
Channel::convertChannels(const std::vector<std::string>& channels){
    std::vector<Channel> v_channel;
    for(auto channel : channels)v_channel.push_back(convertChannel(channel));
    return v_channel;
}


std::vector<std::string>
Channel::convertChannels(const std::vector<Channel>& channels){
    std::vector<std::string> v_channel;
    for(auto channel : channels)v_channel.push_back(convertChannel(channel));
    return v_channel;
}









// --- Functions defined in namespace Tools ---


TString
Tools::assignFolder(const Channel::Channel& channel){
    const TString outpathPlots = "./Plots";
    TString subfolderChannel = Channel::convertChannel(channel);
    subfolderChannel.Prepend("/");
    return outpathPlots + subfolderChannel;
}


TString
Tools::assignFolder(const Channel::Channel& channel, const Systematic::Systematic& systematic){
    const TString path = assignFolder(channel);
    TString subfolderSystematic = Systematic::convertSystematic(systematic);
    subfolderSystematic.Prepend("/");
    return path + subfolderSystematic;
}













