#ifndef MvaWeights2d_h
#define MvaWeights2d_h

#include <vector>
#include <string>
#include <map>

class TSelectorList;
class TString;
class TH1;

#include "mvaStructs.h"
#include "../../common/include/storeTemplate.h"

namespace mvaSetup{
    class MvaConfig;
    class MvaSet;
}




/// Class for plotting 2D distributions for MVA weights of correct and swapped training
class MvaWeights2d{

public:

    /// Constructor for selection steps
    MvaWeights2d(const std::map<TString, std::vector<MvaTopJetsVariables> >& m_stepMvaVariables,
                 const char* mvaWeightFileDirectory,
                 const std::vector<mvaSetup::MvaSet>& v_mvaSet,
                 const bool separationPowerPlots =false);

    /// Destructor
    ~MvaWeights2d(){}



    /// Clear the class instance
    void clear();



    /// Plot the variables and write them to the specified folder
    /// If separationPowerPlots==true: plot them exclusively for the cases of correct, swapped and wrong combinations to see separation power
    /// If separationPowerPlots==false: plot them inclusively for data/MC comparisons
    void plotVariables(const std::string& f_savename);

    /// Plot the variables and store the histograms in the specified TSelectorList
    /// If separationPowerPlots==true: plot them exclusively for the cases of correct, swapped and wrong combinations to see separation power
    /// If separationPowerPlots==false: plot them inclusively for data/MC comparisons
    void plotVariables(TSelectorList* output);



private:

    /// Struct holding the histograms for one selection step
    struct StepHistograms{
        /// Constructor
        StepHistograms(){};
        /// Destructor
        ~StepHistograms(){};

        /// The map with all the histograms for one selection step
        std::map<TString, TH1*> m_histogram_;
    };



    /// Book and fill histograms for given MVA set
    void plotStep(const mvaSetup::MvaSet& mvaSet);

    /// Book 1-D histograms exclusively for correct, swapped and wrong combinations, and inclusively
    void bookHistosInclExcl(std::map<TString, TH1*>& m_histogram, const TString& prefix, const TString& step,
                            const TString& name, const TString& title,
                            const int& nBinX, const double& xMin, const double& xMax);

    /// Book 2-D histograms exclusively for correct, swapped and wrong combinations, and inclusively
    void bookHistosInclExcl2D(std::map<TString, TH1*>& m_histogram, const TString& prefix, const TString& step,
                              const TString& name, const TString& title,
                              const int& nBinX, const double& xMin, const double& xMax,
                              const int& nBinY, const double& yMin, const double& yMax);

    /// Fill 1-D histograms exclusively for correct, swapped and wrong combinations, and inclusively
    void fillHistosInclExcl(std::map<TString, TH1*>& m_histogram, const TString& name,
                            const double& variable,
                            const MvaTopJetsVariables& mvaTopJetsVariables, const double& weight =1.);

    /// Fill 2-D histograms exclusively for correct, swapped and wrong combinations, and inclusively
    void fillHistosInclExcl2D(std::map<TString, TH1*>& m_histogram, const TString& name,
                              const float& variable1, const float& variable2,
                              const MvaTopJetsVariables& mvaTopJetsVariables, const double& weight =1.);

    /// Store names of the step and corresponding trainings to the output root file
    void storeTrainingsForStep(const TString& stepName, const std::vector<mvaSetup::MvaConfig>& v_mvaConfigCorrect,
                               const std::vector<mvaSetup::MvaConfig>& v_mvaConfigSwapped );



    /// Store the object in the output list and return it
    template<class T> T* store(T* obj){return common::store(obj, selectorList_);}



    /// Pointer for bookkeeping of histograms, trees, etc.
    TSelectorList* selectorList_;

    /// The map containing all the vectors of MVA variables for all selection steps
    const std::map<TString, std::vector<MvaTopJetsVariables> >& m_stepMvaVariables_;

    /// The map containing all the step histograms for all selection steps
    std::map<TString, StepHistograms> m_stepHistograms_;

    /// Whether to produce plots inclusively, or exclusively for correct, swapped and wrong combinations
    const bool plotExclusively_;

    /// Where to find the MVA weight files and to store the 2D-weight histograms
    const char* mvaWeightFileDirectory_;

    /// The MVA sets used to define the MVA trainings
    const std::vector<mvaSetup::MvaSet>& v_mvaSet_;
};







#endif







