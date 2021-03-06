#ifndef AnalysisHistograms_h
#define AnalysisHistograms_h

#include <map>
#include <vector>

class TString;
class TH1;
class TSelectorList;

#include "../../common/include/storeTemplate.h"

class JetCategories;
class RecoObjects;
class CommonGenObjects;
class TopGenObjects;
class HiggsGenObjects;
class KinRecoObjects;
namespace tth{
    class RecoLevelWeights;
    class GenLevelWeights;
    class GenObjectIndices;
    class RecoObjectIndices;
}



/// Base class for histograms for analysis, useful to handle same set of histograms for different selection steps
class AnalysisHistogramsBase{
    
public:
    
    /// Constructor with setting up selection steps
    AnalysisHistogramsBase(const TString& prefix,
                           const std::vector<TString>& selectionStepsNoCategories,
                           const std::vector<TString>& stepsForCategories =std::vector<TString>(),
                           const JetCategories* jetCategories =0);
    
    /// Destructor
    ~AnalysisHistogramsBase(){};
    
    /// Book all histograms for all defined selection steps
    void book(TSelectorList* output);
    
    /// Fill all histograms for given selection step, if defined
    void fill(const RecoObjects& recoObjects, const CommonGenObjects& commonGenObjects,
              const TopGenObjects& topGenObjects, const HiggsGenObjects& higgsGenObjects,
              const KinRecoObjects& kinRecoObjects,
              const tth::RecoObjectIndices& recoObjectIndices, const tth::GenObjectIndices& genObjectIndices,
              const tth::GenLevelWeights& genLevelWeights, const tth::RecoLevelWeights& recoLevelWeights,
              const double& weight, const TString& stepShort);
    
    /// Clear all steps
    void clear();
    
    
    
protected:
    
    /// Struct holding the histograms for one selection step
    struct StepHistograms{
        /// Constructor
        StepHistograms(){};
        /// Destructor
        ~StepHistograms(){};

        /// The map with all the histograms for one selection step
        std::map<TString, TH1*> m_histogram_;
    };
    
    /// Add a new selection step
    void addStep(const TString& step);
    
    /// Book all histograms for given selection step (dummy method, override in inherited AnalysisHistograms)
    virtual void bookHistos(const TString& step, std::map<TString, TH1*>& m_histogram);
    
    /// Fill all histograms for given selection step (dummy method, override in inherited AnalysisHistograms)
    virtual void fillHistos(const RecoObjects& recoObjects, const CommonGenObjects& commonGenObjects,
                            const TopGenObjects& topGenObjects, const HiggsGenObjects& higgsGenObjects,
                            const KinRecoObjects& kinRecoObjects,
                            const tth::RecoObjectIndices& recoObjectIndices, const tth::GenObjectIndices& genObjectIndices,
                            const tth::GenLevelWeights& genLevelWeights, const tth::RecoLevelWeights& recoLevelWeights,
                            const double& weight, const TString& step,
                            std::map<TString, TH1*>& m_histogram);
    
    /// Check whether a given selection step already exists
    bool checkExistence(const TString& step)const;
    
    /// Store the object in the output list and return it
    template<class T> T* store(T* obj){return common::store(obj, selectorList_);}
    
    
    
    /// The prefix which all histograms of the specific analyzer should have
    const TString prefix_;
    
    /// Pointer for bookkeeping of histograms
    TSelectorList* selectorList_;
    
    /// The map containing all the step histograms for all selection steps
    std::map<TString, StepHistograms> m_stepHistograms_;
    
    /// The vector of all defined selection steps not separated in jet categories
    const std::vector<TString> selectionSteps_;
    
    /// The vector of selection steps where analysis should also be performed in individual jet categories
    const std::vector<TString> stepsForCategories_;
    
    /// The categories in no. of jets and b-jets
    const JetCategories* jetCategories_;
};






/// Class for histograms needed for event yields
class EventYieldHistograms : public AnalysisHistogramsBase{
    
public:
    
    /// Constructor
    EventYieldHistograms(const std::vector<TString>& selectionStepsNoCategories,
                         const std::vector<TString>& stepsForCategories =std::vector<TString>(),
                         const JetCategories* jetCategories =0);
    
    /// Destructor
    ~EventYieldHistograms(){}
    
    
    
private:
    
    /// Book all histograms for given selection step
    virtual void bookHistos(const TString& step, std::map<TString, TH1*>& m_histogram);
    
    /// Fill all histograms for given selection step
    virtual void fillHistos(const RecoObjects& recoObjects, const CommonGenObjects& commonGenObjects,
                            const TopGenObjects& topGenObjects, const HiggsGenObjects& higgsGenObjects,
                            const KinRecoObjects& kinRecoObjects,
                            const tth::RecoObjectIndices& recoObjectIndices, const tth::GenObjectIndices& genObjectIndices,
                            const tth::GenLevelWeights& genLevelWeights, const tth::RecoLevelWeights& recoLevelWeights,
                            const double& weight, const TString& step,
                            std::map<TString, TH1*>& m_histogram);
};





/// Class for histograms needed for Drell-Yan reweighting
class DyScalingHistograms : public AnalysisHistogramsBase{

public:

    /// Constructor
    DyScalingHistograms(const std::vector<TString>& selectionSteps, const TString& looseStep);

    /// Destructor
    ~DyScalingHistograms(){}



private:

    /// Book all histograms for given selection step
    virtual void bookHistos(const TString& step, std::map<TString, TH1*>& m_histogram);

    /// Store histogram in output
    TH1* bookHisto(TH1* histo, const TString& name);
    
    /// Fill all histograms for given selection step
    virtual void fillHistos(const RecoObjects& recoObjects, const CommonGenObjects& commonGenObjects,
                            const TopGenObjects& topGenObjects, const HiggsGenObjects& higgsGenObjects,
                            const KinRecoObjects& kinRecoObjects,
                            const tth::RecoObjectIndices& recoObjectIndices, const tth::GenObjectIndices& genObjectIndices,
                            const tth::GenLevelWeights& genLevelWeights, const tth::RecoLevelWeights& recoLevelWeights,
                            const double& weight, const TString& step,
                            std::map<TString, TH1*>& m_histogram);
    
    /// The loose selection step used for the estimation of the Drell-Yan background in emu
    const TString& looseStep_;
};






#endif







