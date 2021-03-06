#ifndef EventShapes_h
#define EventShapes_h

#include "DataFormats/PatCandidates/interface/Jet.h"
#include "TopAnalysis/TopAnalyzer/interface/SingleObject.h"

/**
   \class   EventShapes EventShapes.h "TopAnalysis/TopAnalyzer/interface/EventShapes.h"

   \brief   Derived class to analyze the event shapes on reconstruction and generator level

   The structure keeps histograms for event shapes. These histograms can be filled from
   edm::View<reco::Candidate>'s. The class is derived from the SingleObject<Collection>
   interface, which makes it usable in fwfull or fwlite. 
*/

class EventShapes : public SingleObject<const edm::View<reco::Candidate> > {

 public:
  /// default constructor for fw lite
  explicit EventShapes();
  /// default constructor for full fw
  explicit EventShapes(const edm::ParameterSet& configFile);
  /// default destructor
  ~EventShapes(){};

  /**
     The following functions have to be implemented for any class
     derived from SingleObject<Collection>
  **/

  /// histogramm booking for fwlite 
  void book();
  /// histogramm booking for fwfull
  void book(edm::Service<TFileService>& fileService);
  /// histogram filling for fwlite and for fwfull from reco objects
  void fill(const edm::View<reco::Candidate>& jets, const double& weight=1.);
  /// everything which needs to be done after the event loop
  void process() {};

 private:
  /// produce a TTree as output instead of histograms
  bool useTree_;

};

#endif
