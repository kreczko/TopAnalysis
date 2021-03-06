#include "TopAnalysis/TopAnalyzer/interface/DileptonEventWeight.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

double getPuWeight(const edm::Event& evt, 
                   const edm::InputTag& puweight_){
		   
    edm::Handle<double> weightHandle;
    if (puweight_.label().empty())    
      return 1.;
      
    evt.getByLabel(puweight_, weightHandle);
    return *weightHandle;
}


double getDileptonSFWeight(const edm::Event& evt, 
                           const edm::InputTag& lepweight_){
		   
    edm::Handle<double> weightHandle;
    if (lepweight_.label().empty())    
      return 1.;
      
    evt.getByLabel(lepweight_, weightHandle);
    return *weightHandle;
}


double getWeight(const edm::Event& evt, const edm::InputTag& tag_) {
    edm::Handle<double> weightHandle;
    evt.getByLabel( tag_, weightHandle);
    
    return weightHandle.failedToGet() ? 1. : *weightHandle;
}


/// return the PU event weight for the MC events;
/// return 1 for data
double getDileptonEventWeight(const edm::Event& evt, 
                              const edm::InputTag& puweight_, 
			      const edm::InputTag& lepweight_) {
				   				   			   
    if (evt.isRealData()) return 1.; // the data are the data!

    // get PU weight first
    double weight = getPuWeight(evt, puweight_);

    weight *= getDileptonSFWeight(evt, lepweight_);
    
    const edm::InputTag tagKin("eventWeightDileptonKinEffSF", "eventWeightDileptonKinEffSF");
    weight *= getWeight(evt, tagKin); 
      
    const edm::InputTag tagMdl("eventWeightDileptonModelVariation");
    weight *= getWeight(evt, tagMdl);
  
    return weight;
}
