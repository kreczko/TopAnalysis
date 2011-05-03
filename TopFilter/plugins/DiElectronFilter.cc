#include "DataFormats/PatCandidates/interface/Electron.h"
#include "TopAnalysis/TopFilter/plugins/DiElectronFilter.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

/// default constructor 
DiElectronFilter::DiElectronFilter(const edm::ParameterSet& cfg):
  electrons_    (cfg.getParameter<edm::InputTag>(       "electrons"  )),
  fltrChrg_ (cfg.getParameter<int> (       "filterCharge"    )),
  fltrMass_ (cfg.getParameter<bool> (       "filterMass"    )),
  Cut_      (cfg.getParameter<std::vector<double> >("Cut"    )),
  isVeto_   (cfg.getParameter<bool>(                "isVeto" ))
{
}

/// default destructor
DiElectronFilter::~DiElectronFilter()
{
}

/// sanity check
void 
DiElectronFilter::beginJob()
{ 
  if(Cut_.size()!=2)  edm::LogError("topFilter") << "Cut has wrong size. Size has to be 2!\n";
  if(Cut_[0]>Cut_[1]) edm::LogError("topFilter") << "Lower cut value is higher than upper one!\n";
}

/// event veto
bool
DiElectronFilter::filter(edm::Event& event, const edm::EventSetup& setup)
{   
  // fetch the input collection from the event content  
  edm::Handle<std::vector<pat::Electron> > electrons;
  event.getByLabel(electrons_, electrons);
  
  // skip events with less than 2 electrons
  if(electrons->size()<=1) return false;
  
  bool Return=false;

  bool OSign=false;
  bool SSign=false;
  bool OSignMass=false;
  bool SSignMass=false;

  // loop over all electron pairs
  for(int i=0; i< (int)electrons->size(); ++i){
    for(int j=0; j<i; ++j){
   
      // check if like or unlike sign	  
      if((*electrons)[i].charge()*(*electrons)[j].charge()<0) OSign=true;
      else SSign=true;
      // reconstruct invariant mass of 2 electrons
      reco::Particle::LorentzVector diElec = (*electrons)[i].p4() + (*electrons)[j].p4();
      double diElecMass = sqrt( diElec.Dot(diElec) );
      if(diElecMass > Cut_[0] && diElecMass < Cut_[1]){
	if (OSign == true) OSignMass=true;
	else SSignMass=true;
      }
    }
  }

  // filter on unlike or like  sign if configured
  if(fltrChrg_<0 && OSign==true){
    // filter on mass window if configured
    if(fltrMass_ && OSignMass==false) Return=false;
    else Return=true;
  }
  if(fltrChrg_>0 && SSign==true){
    // filter on mass window if configured
    if(fltrMass_ && SSignMass==false) Return=false;
    else Return=true;
  }
  // filter on mass window if configured
  else if(fltrChrg_==0){
    if(fltrMass_ && (OSignMass==true ||SSignMass==true )) Return=true;
    else Return=false;
  }
  // invert selection
  if(isVeto_){
    if (Return==false) Return=true;
    else Return=false;
  }
  
  return Return;
}


