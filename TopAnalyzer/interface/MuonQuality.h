#ifndef MuonQuality_h
#define MuonQuality_h

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "TopAnalysis/TopAnalyzer/interface/SingleObject.h"

/**
   \class   MuonQuality MuonQuality.h "TopAnalysis/TopAnalyzer/interface/MuonQuality.h"

   \brief   Derived class to analyze the quality/id of muons on reconstruction level

   The structure keeps histograms for the identification and (high quality) reconstructed 
   muons. These histograms can be filled from std::vector<pat::Muon> only(!). The class 
   is derived from the SingleObject<Collection> interface, which makes it usable in fwfull
   or fwlite. 
*/

class MuonQuality : public SingleObject<const std::vector<pat::Muon> > {

 public:
  /// default constructor for fwlite
  explicit MuonQuality(const int index);
  /// default constructor for fwfull
  explicit MuonQuality(const edm::ParameterSet& configFile);
  /// default destructor
  ~MuonQuality(){};

  /**
     The following functions have to be implemented for any class
     derived from SingleObject<Collection>
  **/
  /// histogramm booking for fwlite 
  void book();
  /// histogramm booking for fwfull
  void book(edm::Service<TFileService>& fileService);
  /// histogram filling for fwlite and for fwfull from reco objects
  void fill(const std::vector<pat::Muon>& muons, const double& weight=1.);
  /// everything which needs to be done after the event loop
  void process();

 private:
  /// get energy of objects within a ring in deltaR corresponding to the 
  /// bin width of the histogram 'hist' from 'deposit' & fill hist with it
  void energyFlow(TH1* hist, const pat::IsoDeposit* deposit);
  /// get energy of objects within a ring in deltaR corresponding to the 
  /// bin width of the histogram 'hist' from 'deposit' & fill hist with it
  void energyFlow(TH1* hist, const pat::IsoDeposit* ecalDeposit, const pat::IsoDeposit* hcalDeposit);
  /// get number of objects within a ring in deltaR corresponding to the 
  /// bin width of the histogram 'hist' from 'deposit' and fill hist with it
  void objectFlow(TH1* hist, const pat::IsoDeposit* deposit);

 private:
  /// number of (weighted) histogram entries for normalization
  double norm_;
  /// index of jet to be plotted
  int index_;
};

#endif
