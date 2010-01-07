#ifndef ElectronKinematics_h
#define ElectronKinematics_h

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "TopAnalysis/TopAnalyzer/interface/SingleObject.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

/**
   \class   ElectronKinematics ElectronKinematics.h "TopAnalysis/TopAnalyzer/interface/ElectronKinematics.h"

   \brief   Derived class to analyze the kinematics of electrons on reconstruction and generator level

   The structure keeps histograms for the kinematics of electrons only(!). These histograms can be 
   filled from edm::View<pat::Electron>'s or from std::vector<reco::GenParticles>'s. The class 
   is derived from the SingleObject<Collection> interface, which makes it usable in fwfull  or 
   fwlite. 
*/

class ElectronKinematics : public SingleObject<const edm::View<pat::Electron> > {

 public:
  /// default constructor for fw lite
  explicit ElectronKinematics(const int index);
  /// default constructor for full fw
  explicit ElectronKinematics(const edm::ParameterSet& configFile);
  /// default destructor
  ~ElectronKinematics(){};

  /**
     The following functions have to be implemented for any class
     derived from SingleObject<Collection>
  **/
  /// histogramm booking for fwlite 
  void book();
  /// histogramm booking for fwfull
  void book(edm::Service<TFileService>& fileService);
  /// histogram filling for fwlite and for fwfull from reco objects
  void fill(const edm::View<pat::Electron>& electrons, const double& weight=1.);
  /// histogram filling for fwlite and for fwfull from generator objects
  void fill(const std::vector<reco::GenParticle>& electrons, const double& weight=1.);
  /// everything which needs to be done after the event loop
  void process() {};

 private:
  /// index of jet to be plotted
  int index_;
};

#endif
