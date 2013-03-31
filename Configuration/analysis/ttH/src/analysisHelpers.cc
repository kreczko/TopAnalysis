#include <iostream>
#include <cstdlib>

#include "analysisHelpers.h"






AnalysisMode::AnalysisMode AnalysisMode::convertAnalysisMode(const std::string& analysisMode)
{
    if(analysisMode == "cp") return cp;
    if(analysisMode == "mva") return mva;
    std::cout<<"Warning! The following analysis mode conversion is not implemented: "<<analysisMode<<std::endl;
    return undefined;
}



std::string AnalysisMode::convertAnalysisMode(const AnalysisMode& analysisMode)
{
    if(analysisMode == cp) return "cp";
    if(analysisMode == mva) return "mva";
    if(analysisMode == undefined) return "";
    std::cout<<"Error! Analysis mode conversion is not implemented, break...\n"<<std::endl;
    exit(96);
}



std::vector<AnalysisMode::AnalysisMode> AnalysisMode::convertAnalysisModes(const std::vector<std::string>& analysisModes)
{
    std::vector<AnalysisMode> v_analysisMode;
    for(auto analysisMode : analysisModes)v_analysisMode.push_back(convertAnalysisMode(analysisMode));
    return v_analysisMode;
}



std::vector<std::string> AnalysisMode::convertAnalysisModes(const std::vector<AnalysisMode>& analysisModes)
{
    std::vector<std::string> v_analysisMode;
    for(auto analysisMode : analysisModes)v_analysisMode.push_back(convertAnalysisMode(analysisMode));
    return v_analysisMode;
}









