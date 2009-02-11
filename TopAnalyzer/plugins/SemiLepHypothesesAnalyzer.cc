#include "TopAnalysis/TopAnalyzer/plugins/SemiLepHypothesesAnalyzer.h"

#include "TopAnalysis/TopUtils/interface/NameScheme.h"

#include "TopQuarkAnalysis/TopTools/interface/TtSemiLepEvtPartons.h"

SemiLepHypothesesAnalyzer::SemiLepHypothesesAnalyzer(const edm::ParameterSet& cfg):
  semiLepEvt_      (cfg.getParameter<edm::InputTag>("semiLepEvent"    )),
  hypoClassKey_    (cfg.getParameter<edm::InputTag>("hypoClassKey"    )),
  wgt_             (cfg.getParameter<edm::InputTag>("weight"          )),
  nJetsMax_        (cfg.getParameter<unsigned int> ("nJetsMax"        )),
  maxSumDRGenMatch_(cfg.getParameter<double>       ("maxSumDRGenMatch")),
  minProbKinFit_   (cfg.getParameter<double>       ("minProbKinFit"   )),
  minMVADisc_      (cfg.getParameter<double>       ("minMVADisc"      )),
  hist_            (cfg.getParameter<std::string>  ("hist"            ))
{
}

void
SemiLepHypothesesAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup)
{

  edm::Handle<TtSemiLeptonicEvent> semiLepEvt;
  evt.getByLabel(semiLepEvt_, semiLepEvt);

  edm::Handle<int> hypoClassKeyHandle;
  evt.getByLabel(hypoClassKey_, hypoClassKeyHandle);
  TtSemiLeptonicEvent::HypoClassKey& hypoClassKey = (TtSemiLeptonicEvent::HypoClassKey&) *hypoClassKeyHandle;

  edm::Handle<double> wgt;
  evt.getByLabel(wgt_, wgt);
  double weight = *wgt;

  nEventsTotal++;

  // -----------------------
  // check if hypothesis is valid in this event
  // and if it satisfies some quality criteria
  // -----------------------

  if( !semiLepEvt->isHypoAvailable(hypoClassKey) ){
    edm::LogWarning ( "NonValidHyp" ) << "Hypothesis not available for this event";
    return;
  }
  if( !semiLepEvt->isHypoValid(hypoClassKey) ){
    edm::LogWarning ( "NonValidHyp" ) << "Hypothesis not valid for this event";
    return;
  }
  else nEventsValid++;
  
  if( !semiLepEvt->isHypoValid(hypoClassKey) ||
      (hypoClassKey==TtSemiLeptonicEvent::kGenMatch && semiLepEvt->genMatchSumDR()>maxSumDRGenMatch_) ||
      (hypoClassKey==TtSemiLeptonicEvent::kKinFit   && semiLepEvt->fitProb()<minProbKinFit_         ) ||
      (hypoClassKey==TtSemiLeptonicEvent::kMVADisc  && semiLepEvt->mvaDisc()<minMVADisc_            )
      ) {
    goodHypo_->Fill(0., weight); // not a good hypothesis
    return;
  }
  else {
    goodHypo_->Fill(1., weight); // good hypothesis
    nEventsQuali++;
  }
//  if( !semiLepEvt->isHypoValid(TtSemiLeptonicEvent::kGeom         ) ||
//      !semiLepEvt->isHypoValid(TtSemiLeptonicEvent::kWMassMaxSumPt) ||
//      !semiLepEvt->isHypoValid(TtSemiLeptonicEvent::kMaxSumPtWMass) ||
//      !semiLepEvt->isHypoValid(TtSemiLeptonicEvent::kGenMatch     ) ||
//      !semiLepEvt->isHypoValid(TtSemiLeptonicEvent::kMVADisc      ) ||
//      !semiLepEvt->isHypoValid(TtSemiLeptonicEvent::kKinFit       ) )
//    return;  // return if any of the hypotheses is not valid

  // -----------------------
  // fill histos related to quality of the TtSemiLeptonicEvent
  // -----------------------
  fillQualityHistos(*semiLepEvt, weight);

  // good0: LepB correct
  // good1: HadB correct
  // good2: HadW correct
  // good3: HadT correct
  // good4: good1 && good2
  // good5: good0 && good4

  bool good[6];

  good[0] = (semiLepEvt->jetLepComb(hypoClassKey)                  [TtSemiLepEvtPartons::LepB] ==
	     semiLepEvt->jetLepComb(TtSemiLeptonicEvent::kGenMatch)[TtSemiLepEvtPartons::LepB]);

  good[1] = (semiLepEvt->jetLepComb(hypoClassKey)                  [TtSemiLepEvtPartons::HadB] ==
	     semiLepEvt->jetLepComb(TtSemiLeptonicEvent::kGenMatch)[TtSemiLepEvtPartons::HadB]);

  std::vector<int> HadWJets;
  HadWJets.push_back( TtSemiLepEvtPartons::LightQ    );
  HadWJets.push_back( TtSemiLepEvtPartons::LightQBar );

  std::vector<int> HadTJets;
  HadTJets.push_back( TtSemiLepEvtPartons::LightQ    );
  HadTJets.push_back( TtSemiLepEvtPartons::LightQBar );
  HadTJets.push_back( TtSemiLepEvtPartons::HadB      );
  
  good[2] = sameJets( *semiLepEvt, hypoClassKey, TtSemiLeptonicEvent::kGenMatch, HadWJets);

  good[3] = sameJets( *semiLepEvt, hypoClassKey, TtSemiLeptonicEvent::kGenMatch, HadTJets);

  good[4] = (good[1] && good[2]);
  good[5] = (good[0] && good[4]);

  for(unsigned i=0; i<6; i++)
    if(good[i]) ++nEventsGood[i];

//  if( semiLepEvt->genMatchSumDR() > maxSumDRGenMatch_ ||
//      semiLepEvt->fitProb() < minProbKinFit_          ||
//      semiLepEvt->mvaDisc() < minMVADisc_ )
//    return; // return if any of the quality criteria is not fulfilled

  // -----------------------
  // fill histos for basic kinematic variables
  // -----------------------
  const reco::Candidate* HadTop   = semiLepEvt->hadronicTop(hypoClassKey);
  const reco::Candidate* HadW     = semiLepEvt->hadronicW  (hypoClassKey);
  const reco::Candidate* HadB     = semiLepEvt->hadronicB  (hypoClassKey);
  const reco::Candidate* HadQ     = semiLepEvt->lightQuarkQ(hypoClassKey);
  const reco::Candidate* HadP     = semiLepEvt->lightQuarkP(hypoClassKey);
  const reco::Candidate* LepTop   = semiLepEvt->leptonicTop(hypoClassKey);
  const reco::Candidate* LepW     = semiLepEvt->leptonicW  (hypoClassKey);
  const reco::Candidate* LepB     = semiLepEvt->leptonicB  (hypoClassKey);
  const reco::Candidate* Lepton   = semiLepEvt->lepton     (hypoClassKey);
  const reco::Candidate* Neutrino = semiLepEvt->neutrino   (hypoClassKey);

  fillKinHistos(hadTopKin_, *HadTop  , weight);
  fillKinHistos(hadWKin_,   *HadW    , weight);
  fillKinHistos(hadBKin_,   *HadB    , weight);
  fillKinHistos(hadQKin_,   *HadQ    , weight);
  fillKinHistos(hadPKin_,   *HadP    , weight);
  fillKinHistos(lepTopKin_, *LepTop  , weight);
  fillKinHistos(lepWKin_,   *LepW    , weight);
  fillKinHistos(lepBKin_,   *LepB    , weight);
  fillKinHistos(leptonKin_, *Lepton  , weight);
  fillKinHistos(neutriKin_, *Neutrino, weight);

  hadTopLepTopMassDiff->Fill( HadTop->mass()-LepTop->mass() , weight );
  hadWLepWMassDiff    ->Fill( HadW  ->mass()-LepW  ->mass() , weight );

  // -----------------------
  // fill resolution histos for kinematic variables
  // with respect to the generator particles
  // -----------------------
  if( semiLepEvt->genEvent()->isSemiLeptonic() ) {

    const reco::Candidate* genHadTop   = semiLepEvt->genHadronicTop();
    const reco::Candidate* genHadW     = semiLepEvt->genHadronicW();
    const reco::Candidate* genHadB     = semiLepEvt->genHadronicB();
    const reco::Candidate* genHadQ     = semiLepEvt->genHadronicQ();
    const reco::Candidate* genHadP     = semiLepEvt->genHadronicP();
    const reco::Candidate* genLepTop   = semiLepEvt->genLeptonicTop();
    const reco::Candidate* genLepW     = semiLepEvt->genLeptonicW();
    const reco::Candidate* genLepB     = semiLepEvt->genLeptonicB();
    const reco::Candidate* genLepton   = semiLepEvt->genLepton();
    const reco::Candidate* genNeutrino = semiLepEvt->genNeutrino();

    fillKinResHistos(hadTopKinRes_, *HadTop  , *genHadTop  , weight);
    fillKinResHistos(hadWKinRes_  , *HadW    , *genHadW    , weight);
    fillKinResHistos(hadBKinRes_  , *HadB    , *genHadB    , weight);
    fillKinResHistos(hadQKinRes_  , *HadQ    , *genHadQ    , weight);
    fillKinResHistos(hadPKinRes_  , *HadP    , *genHadP    , weight);
    fillKinResHistos(lepTopKinRes_, *LepTop  , *genLepTop  , weight);
    fillKinResHistos(lepWKinRes_  , *LepW    , *genLepW    , weight);
    fillKinResHistos(lepBKinRes_  , *LepB    , *genLepB    , weight);
    fillKinResHistos(leptonKinRes_, *Lepton  , *genLepton  , weight);
    fillKinResHistos(neutriKinRes_, *Neutrino, *genNeutrino, weight);

  }

  // -----------------------
  // fill correlation histos for jet parton association
  // -----------------------
  fillJetCorrelHistos(semiLepEvt->jetLepComb(hypoClassKey),
		      semiLepEvt->jetLepComb(TtSemiLeptonicEvent::kGenMatch),
		      weight);

}

void 
SemiLepHypothesesAnalyzer::beginJob(const edm::EventSetup&)
{

  if( hist_.empty() ) throw edm::Exception( edm::errors::Configuration, "Empty string for hist in cfi file" );
  ofstream hist(hist_.c_str(), std::ios::out);

  edm::Service<TFileService> fs;
  if( !fs ) throw edm::Exception( edm::errors::Configuration, "TFile Service is not registered in cfg file" );

  bookKinHistos      (fs, hist);
  bookKinResHistos   (fs, hist);
  bookJetCorrelHistos(fs, hist);
  bookQualityHistos  (fs, hist);

  nEventsTotal = 0;
  nEventsValid = 0;
  nEventsQuali = 0;
  for(unsigned i=0; i<6; i++)
    nEventsGood[i] = 0;

}

void
SemiLepHypothesesAnalyzer::endJob() 
{

  numbEvents_->SetBinContent(1, nEventsTotal);
  fracEvents_->SetBinContent(1, (double)nEventsTotal/nEventsTotal);

  numbEvents_->SetBinContent(2, nEventsValid);
  fracEvents_->SetBinContent(2, (double)nEventsValid/nEventsTotal);

  numbEvents_->SetBinContent(3, nEventsQuali);
  fracEvents_->SetBinContent(3, (double)nEventsQuali/nEventsTotal);

  for(unsigned i=0; i<6; i++) {
    numbEvents_->SetBinContent(4+i, nEventsGood[i]);
    fracEvents_->SetBinContent(4+i, (double)nEventsGood[i]/nEventsQuali);
  }

  edm::LogInfo summary("SemiLepHypothesesAnalyzer");
  summary << "HypoKey: " << hypoClassKey_.label() << "\n";
  summary << "Number, fraction of events (total): "
	  << setw(6) << nEventsTotal << ", " << setw(6) << fixed << setprecision(3) << (double)nEventsTotal/nEventsTotal << "\n";
  summary << "Number, fraction of events (valid): "
	  << setw(6) << nEventsValid << ", " << setw(6) << fixed << setprecision(3) << (double)nEventsValid/nEventsTotal << "\n";
  summary << "Number, fraction of events (quali): "
	  << setw(6) << nEventsQuali << ", " << setw(6) << fixed << setprecision(3) << (double)nEventsQuali/nEventsTotal << "\n";
  for(unsigned i=0; i<6; i++)
    summary << "Number, fraction of events (good" << i+1 << "): "
	    << setw(6) << nEventsGood[i] << ", " << setw(6) << fixed << setprecision(3) << (double)nEventsGood[i]/nEventsQuali << "\n";

}

void
SemiLepHypothesesAnalyzer::bookKinHistos(edm::Service<TFileService>& fs, ofstream& hist)
{

  NameScheme ns("kin");

  hadTopKin_.push_back( fs->make<TH1F>(ns.name(hist, "hadTopPt"  ), "p_{T} (t_{had}) [GeV]", 50,  0. , 500. ) );
  hadTopKin_.push_back( fs->make<TH1F>(ns.name(hist, "hadTopEta" ), "#eta (t_{had})"       , 34, -3.4,   3.4) );
  hadTopKin_.push_back( fs->make<TH1F>(ns.name(hist, "hadTopPhi" ), "#phi (t_{had})"       , 34, -3.4,   3.4) );
  hadTopKin_.push_back( fs->make<TH1F>(ns.name(hist, "hadTopMass"), "M (t_{had}) [GeV]"    , 30,  0. , 600. ) );

  hadWKin_.push_back( fs->make<TH1F>(ns.name(hist, "hadWPt"  ), "p_{T} (W_{had}) [GeV]", 50,  0. , 500. ) );
  hadWKin_.push_back( fs->make<TH1F>(ns.name(hist, "hadWEta" ), "#eta (W_{had})"       , 34, -3.4,   3.4) );
  hadWKin_.push_back( fs->make<TH1F>(ns.name(hist, "hadWPhi" ), "#phi (W_{had})"       , 34, -3.4,   3.4) );
  hadWKin_.push_back( fs->make<TH1F>(ns.name(hist, "hadWMass"), "M (W_{had}) [GeV]"    , 25,  0. , 250. ) );

  hadBKin_.push_back( fs->make<TH1F>(ns.name(hist, "hadBPt"  ), "p_{T} (b_{had}) [GeV]", 50,  0. , 500. ) );
  hadBKin_.push_back( fs->make<TH1F>(ns.name(hist, "hadBEta" ), "#eta (b_{had})"       , 34, -3.4,   3.4) );
  hadBKin_.push_back( fs->make<TH1F>(ns.name(hist, "hadBPhi" ), "#phi (b_{had})"       , 34, -3.4,   3.4) );
  hadBKin_.push_back( fs->make<TH1F>(ns.name(hist, "hadBMass"), "M (b_{had}) [GeV]"    , 30,  0. , 150. ) );

  hadQKin_.push_back( fs->make<TH1F>(ns.name(hist, "hadQPt"  ), "p_{T} (q_{had}) [GeV]", 40,  0. , 400. ) );
  hadQKin_.push_back( fs->make<TH1F>(ns.name(hist, "hadQEta" ), "#eta (q_{had})"       , 34, -3.4,   3.4) );
  hadQKin_.push_back( fs->make<TH1F>(ns.name(hist, "hadQPhi" ), "#phi (q_{had})"       , 34, -3.4,   3.4) );
  hadQKin_.push_back( fs->make<TH1F>(ns.name(hist, "hadQMass"), "M (q_{had}) [GeV]"    , 20,  0. , 100. ) );

  hadPKin_.push_back( fs->make<TH1F>(ns.name(hist, "hadPPt"  ), "p_{T} (#bar q_{had}) [GeV]", 40,  0. , 400. ) );
  hadPKin_.push_back( fs->make<TH1F>(ns.name(hist, "hadPEta" ), "#eta (#bar q_{had})"       , 34, -3.4,   3.4) );
  hadPKin_.push_back( fs->make<TH1F>(ns.name(hist, "hadPPhi" ), "#phi (#bar q_{had})"       , 34, -3.4,   3.4) );
  hadPKin_.push_back( fs->make<TH1F>(ns.name(hist, "hadPMass"), "M (#bar q_{had}) [GeV]"    , 20,  0. , 100. ) );

  lepTopKin_.push_back( fs->make<TH1F>(ns.name(hist, "lepTopPt"  ), "p_{T} (t_{lep}) [GeV]", 50,  0. , 500. ) );
  lepTopKin_.push_back( fs->make<TH1F>(ns.name(hist, "lepTopEta" ), "#eta (t_{lep})"       , 34, -3.4,   3.4) );
  lepTopKin_.push_back( fs->make<TH1F>(ns.name(hist, "lepTopPhi" ), "#phi (t_{lep})"       , 34, -3.4,   3.4) );
  lepTopKin_.push_back( fs->make<TH1F>(ns.name(hist, "lepTopMass"), "M (t_{lep}) [GeV]"    , 30,  0. , 600. ) );

  lepWKin_.push_back( fs->make<TH1F>(ns.name(hist, "lepWPt"  ), "p_{T} (W_{lep}) [GeV]", 50,  0. , 500. ) );
  lepWKin_.push_back( fs->make<TH1F>(ns.name(hist, "lepWEta" ), "#eta (W_{lep})"       , 34, -3.4,   3.4) );
  lepWKin_.push_back( fs->make<TH1F>(ns.name(hist, "lepWPhi" ), "#phi (W_{lep})"       , 34, -3.4,   3.4) );
  lepWKin_.push_back( fs->make<TH1F>(ns.name(hist, "lepWMass"), "M (W_{lep}) [GeV]"    , 25,  0. , 250. ) );

  lepBKin_.push_back( fs->make<TH1F>(ns.name(hist, "lepBPt"  ), "p_{T} (b_{lep}) [GeV]", 50,  0. , 500. ) );
  lepBKin_.push_back( fs->make<TH1F>(ns.name(hist, "lepBEta" ), "#eta (b_{lep})"       , 34, -3.4,   3.4) );
  lepBKin_.push_back( fs->make<TH1F>(ns.name(hist, "lepBPhi" ), "#phi (b_{lep})"       , 34, -3.4,   3.4) );
  lepBKin_.push_back( fs->make<TH1F>(ns.name(hist, "lepBMass"), "M (b_{lep}) [GeV]"    , 30,  0. , 150. ) );

  leptonKin_.push_back( fs->make<TH1F>(ns.name(hist, "leptonPt"  ), "p_{T} (lepton) [GeV]", 30,  0. , 300. ) );
  leptonKin_.push_back( fs->make<TH1F>(ns.name(hist, "leptonEta" ), "#eta (lepton)"       , 34, -3.4,   3.4) );
  leptonKin_.push_back( fs->make<TH1F>(ns.name(hist, "leptonPhi" ), "#phi (lepton)"       , 34, -3.4,   3.4) );
  leptonKin_.push_back( fs->make<TH1F>(ns.name(hist, "leptonMass"), "M (lepton) [GeV]"    , 25,  0. ,  50. ) );

  neutriKin_.push_back( fs->make<TH1F>(ns.name(hist, "neutriPt"  ), "p_{T} (neutrino) [GeV]", 40,  0. , 400. ) );
  neutriKin_.push_back( fs->make<TH1F>(ns.name(hist, "neutriEta" ), "#eta (neutrino)"       , 34, -3.4,   3.4) );
  neutriKin_.push_back( fs->make<TH1F>(ns.name(hist, "neutriPhi" ), "#phi (neutrino)"       , 34, -3.4,   3.4) );
  neutriKin_.push_back( fs->make<TH1F>(ns.name(hist, "neutriMass"), "M (neutrino) [GeV]"    , 25,  0. ,  50. ) );  

  hadTopLepTopMassDiff = fs->make<TH1F>(ns.name(hist, "hadTopLepTopMassDiff"), "M (t_{had}) -  M (t_{lep}) [GeV]", 40, -400., 400);
  hadWLepWMassDiff     = fs->make<TH1F>(ns.name(hist, "hadWLepWMassDiff"    ), "M (W_{had}) -  M (W_{lep}) [GeV]", 40, -200., 200);

}

void
SemiLepHypothesesAnalyzer::bookKinResHistos(edm::Service<TFileService>& fs, ofstream& hist)
{

  NameScheme ns("kinRes");

  hadTopKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "hadTopPt"  ), "(p_{T}^{rec}-p_{T}^{gen})/p_{T}^{gen} (t_{had})",  20, -1.2, 1.2) );
  hadTopKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "hadTopEta" ), "(#eta^{rec}-#eta^{gen})/#eta^{gen} (t_{had})   ",  20, -1.2, 1.2) );
  hadTopKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "hadTopPhi" ), "(#phi^{rec}-#phi^{gen})/#phi^{gen} (t_{had})   ",  20, -1.2, 1.2) );
  hadTopKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "hadTopMass"), "(M^{rec}-M^{gen})/M^{gen} (t_{had})            ",  20, -1.2, 1.2) );

  hadWKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "hadWPt"  ), "(p_{T}^{rec}-p_{T}^{gen})/p_{T}^{gen} (W_{had})", 20, -1.2, 1.2) );
  hadWKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "hadWEta" ), "(#eta^{rec}-#eta^{gen})/#eta^{gen} (W_{had})   ", 20, -1.2, 1.2) );
  hadWKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "hadWPhi" ), "(#phi^{rec}-#phi^{gen})/#phi^{gen} (W_{had})   ", 20, -1.2, 1.2) );
  hadWKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "hadWMass"), "(M^{rec}-M^{gen})/M^{gen} (W_{had})            ", 20, -1.2, 1.2) );

  hadBKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "hadBPt"  ), "(p_{T}^{rec}-p_{T}^{gen})/p_{T}^{gen} (b_{had})", 20, -1.2, 1.2) );
  hadBKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "hadBEta" ), "(#eta^{rec}-#eta^{gen})/#eta^{gen} (b_{had})   ", 20, -1.2, 1.2) );
  hadBKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "hadBPhi" ), "(#phi^{rec}-#phi^{gen})/#phi^{gen} (b_{had})   ", 20, -1.2, 1.2) );
  hadBKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "hadBMass"), "(M^{rec}-M^{gen})/M^{gen} (b_{had})            ", 20, -1.2, 1.2) );

  hadQKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "hadQPt"  ), "(p_{T}^{rec}-p_{T}^{gen})/p_{T}^{gen} (q_{had})", 20, -1.2, 1.2) );
  hadQKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "hadQEta" ), "(#eta^{rec}-#eta^{gen})/#eta^{gen} (q_{had})   ", 20, -1.2, 1.2) );
  hadQKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "hadQPhi" ), "(#phi^{rec}-#phi^{gen})/#phi^{gen} (q_{had})   ", 20, -1.2, 1.2) );
  hadQKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "hadQMass"), "(M^{rec}-M^{gen})/M^{gen} (q_{had})            ", 20, -1.2, 1.2) );

  hadPKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "hadPPt"  ), "(p_{T}^{rec}-p_{T}^{gen})/p_{T}^{gen} (#bar q_{had})", 20, -1.2, 1.2) );
  hadPKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "hadPEta" ), "(#eta^{rec}-#eta^{gen})/#eta^{gen} (#bar q_{had})   ", 20, -1.2, 1.2) );
  hadPKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "hadPPhi" ), "(#phi^{rec}-#phi^{gen})/#phi^{gen} (#bar q_{had})   ", 20, -1.2, 1.2) );
  hadPKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "hadPMass"), "(M^{rec}-M^{gen})/M^{gen} (#bar q_{had})            ", 20, -1.2, 1.2) );

  lepTopKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "lepTopPt"  ), "(p_{T}^{rec}-p_{T}^{gen})/p_{T}^{gen} (t_{lep})", 20, -1.2, 1.2) );
  lepTopKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "lepTopEta" ), "(#eta^{rec}-#eta^{gen})/#eta^{gen} (t_{lep})   ", 20, -1.2, 1.2) );
  lepTopKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "lepTopPhi" ), "(#phi^{rec}-#phi^{gen})/#phi^{gen} (t_{lep})   ", 20, -1.2, 1.2) );
  lepTopKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "lepTopMass"), "(M^{rec}-M^{gen})/M^{gen} (t_{lep})            ", 20, -1.2, 1.2) );

  lepWKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "lepWPt"  ), "(p_{T}^{rec}-p_{T}^{gen})/p_{T}^{gen} (W_{lep})", 20, -1.2, 1.2) );
  lepWKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "lepWEta" ), "(#eta^{rec}-#eta^{gen})/#eta^{gen} (W_{lep})   ", 20, -1.2, 1.2) );
  lepWKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "lepWPhi" ), "(#phi^{rec}-#phi^{gen})/#phi^{gen} (W_{lep})   ", 20, -1.2, 1.2) );
  lepWKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "lepWMass"), "(M^{rec}-M^{gen})/M^{gen} (W_{lep})            ", 20, -1.2, 1.2) );

  lepBKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "lepBPt"  ), "(p_{T}^{rec}-p_{T}^{gen})/p_{T}^{gen} (b_{lep})", 20, -1.2, 1.2) );
  lepBKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "lepBEta" ), "(#eta^{rec}-#eta^{gen})/#eta^{gen} (b_{lep})   ", 20, -1.2, 1.2) );
  lepBKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "lepBPhi" ), "(#phi^{rec}-#phi^{gen})/#phi^{gen} (b_{lep})   ", 20, -1.2, 1.2) );
  lepBKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "lepBMass"), "(M^{rec}-M^{gen})/M^{gen} (b_{lep})            ", 20, -1.2, 1.2) );

  leptonKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "leptonPt"  ), "(p_{T}^{rec}-p_{T}^{gen})/p_{T}^{gen} (lepton)", 20, -1.2, 1.2) );
  leptonKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "leptonEta" ), "(#eta^{rec}-#eta^{gen})/#eta^{gen} (lepton)   ", 20, -1.2, 1.2) );
  leptonKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "leptonPhi" ), "(#phi^{rec}-#phi^{gen})/#phi^{gen} (lepton)   ", 20, -1.2, 1.2) );
  leptonKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "leptonMass"), "(M^{rec}-M^{gen})/M^{gen} (lepton)            ", 20, -1.2, 1.2) );

  neutriKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "neutriPt"  ), "(p_{T}^{rec}-p_{T}^{gen})/p_{T}^{gen} (neutrino)", 20, -1.2, 1.2) );
  neutriKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "neutriEta" ), "(#eta^{rec}-#eta^{gen})/#eta^{gen} (neutrino)   ", 20, -1.2, 1.2) );
  neutriKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "neutriPhi" ), "(#phi^{rec}-#phi^{gen})/#phi^{gen} (neutrino)   ", 20, -1.2, 1.2) );
  neutriKinRes_.push_back( fs->make<TH1F>(ns.name(hist, "neutriMass"), "(M^{rec}-M^{gen})/M^{gen} (neutrino)            ", 20, -1.2, 1.2) );

}

void
SemiLepHypothesesAnalyzer::bookJetCorrelHistos(edm::Service<TFileService>& fs, ofstream& hist)
{

  NameScheme ns("jetCorrel");

  int nBins = nJetsMax_;
  double upEdge = nJetsMax_ + 0.5;

  hadBJetCorrel_ = fs->make<TH2F>(ns.name(hist, "hadB"), ns.name("hadB"), nBins, 0.5, upEdge, nBins, 0.5, upEdge);
  hadQJetCorrel_ = fs->make<TH2F>(ns.name(hist, "hadQ"), ns.name("hadQ"), nBins, 0.5, upEdge, nBins, 0.5, upEdge);
  hadPJetCorrel_ = fs->make<TH2F>(ns.name(hist, "hadP"), ns.name("hadP"), nBins, 0.5, upEdge, nBins, 0.5, upEdge);
  lepBJetCorrel_ = fs->make<TH2F>(ns.name(hist, "lepB"), ns.name("lepB"), nBins, 0.5, upEdge, nBins, 0.5, upEdge);

}

void
SemiLepHypothesesAnalyzer::bookQualityHistos(edm::Service<TFileService>& fs, ofstream& hist)
{

  NameScheme ns("qual1D");

  goodHypo_ = fs->make<TH1F>(ns.name(hist, "goodHypo"), "good hypothesis", 2, -0.5, 1.5);

  numbEvents_ = fs->make<TH1F>(ns.name(hist, "numbEvents"), "number of events"         , 10, 0., 10.);
  fracEvents_ = fs->make<TH1F>(ns.name(hist, "fracEvents"), "relative number of events", 10, 0., 10.);

  genMatchSumDR_ = fs->make<TH1F>(ns.name(hist, "genMatchSumDR"), "#Sigma #Delta R (genMatch)"          , 50, 0., 5.);
  genMatchSumPt_ = fs->make<TH1F>(ns.name(hist, "genMatchSumPt"), "#Sigma #Delta p_{T} (genMatch) [GeV]", 40, 0., 400.);
  mvaDisc_       = fs->make<TH1F>(ns.name(hist, "mvaDisc"),       "MVA discrim."                        , 20, 0., 1.);
  fitChi2_       = fs->make<TH1F>(ns.name(hist, "fitChi2"),       "#chi^{2} (kinFit)"                   , 20, 0., 2.);
  fitProb_       = fs->make<TH1F>(ns.name(hist, "fitProb"),       "#chi^{2} probability (kinFit)"       , 20, 0., 1.);

  NameScheme ns2("qual2D");

  genMatchSumDRVsSumPt_      = fs->make<TH2F>(ns2.name(hist, "genMatchSumDRVsSumPt"),      "#Sigma #Delta R (genMatch) vs. #Sigma #Delta p_{T} (genMatch) [GeV]", 50, 0., 5., 40, 0., 400.);
  genMatchSumDRVsHadWMass_   = fs->make<TH2F>(ns2.name(hist, "genMatchSumDRVsHadWMass"),   "#Sigma #Delta R (genMatch) vs. M (W_{had}) [GeV] (genMatch)"        , 50, 0., 5., 50, 0., 500.);
  genMatchSumDRVsHadTopMass_ = fs->make<TH2F>(ns2.name(hist, "genMatchSumDRVsHadTopMass"), "#Sigma #Delta R (genMatch) vs. M (t_{had}) [GeV] (genMatch)"        , 50, 0., 5., 60, 0., 600.);
  genMatchSumDRVsMVADisc_    = fs->make<TH2F>(ns2.name(hist, "genMatchSumDRVsMVADisc"),    "#Sigma #Delta R (genMatch) vs. MVA discrim."                        , 50, 0., 5., 20, 0., 1.);
  genMatchSumDRVsFitProb_    = fs->make<TH2F>(ns2.name(hist, "genMatchSumDRVsFitProb"),    "#Sigma #Delta R (genMatch) vs. #chi^{2} probability (kinFit)"                      , 50, 0., 5., 20, 0., 1.);
  mvaDiscVsHadWMass_   = fs->make<TH2F>(ns2.name(hist, "mvaDiscVsHadWMass"),   "MVA discrim. vs. M (W_{had}) [GeV] (MVADisc)"  , 20, 0., 1., 50, 0., 500.);
  mvaDiscVsHadTopMass_ = fs->make<TH2F>(ns2.name(hist, "mvaDiscVsHadTopMass"), "MVA discrim. vs. M (t_{had}) [GeV] (MVADisc)", 20, 0., 1., 60, 0., 600.);
  mvaDiscVsFitProb_       = fs->make<TH2F>(ns2.name(hist, "mvaDiscVsFitProb"), "MVA discrim. vs. #chi^{2} probability (kinFit)", 20, 0., 1., 20, 0., 1.);
  fitProbVsHadWMass_   = fs->make<TH2F>(ns2.name(hist, "fitProbVsHadWMass"),   "#chi^{2} probability (kinFit) vs. M (W_{had}) [GeV] (MVADisc)"  , 20, 0., 1., 50, 0., 500.);
  fitProbVsHadTopMass_ = fs->make<TH2F>(ns2.name(hist, "fitProbVsHadTopMass"), "#chi^{2} probability (kinFit) vs. M (t_{had}) [GeV] (MVADisc)", 20, 0., 1., 60, 0., 600.);

}

void
SemiLepHypothesesAnalyzer::fillKinHistos(std::vector<TH1F*>& histos, const reco::Candidate& candidate, const double& weight)
{
  histos[0]->Fill( candidate.pt()   , weight );
  histos[1]->Fill( candidate.eta()  , weight );
  histos[2]->Fill( candidate.phi()  , weight );
  histos[3]->Fill( candidate.mass() , weight );
}

void
SemiLepHypothesesAnalyzer::fillKinResHistos(std::vector<TH1F*>& histos, const reco::Candidate& candidate,
					    const reco::Candidate& genCandidate, const double& weight)
{
  histos[0]->Fill( (candidate.pt()  -genCandidate.pt()  )/genCandidate.pt()   , weight );
  histos[1]->Fill( (candidate.eta() -genCandidate.eta() )/genCandidate.eta()  , weight );
  histos[2]->Fill( (candidate.phi() -genCandidate.phi() )/genCandidate.phi()  , weight );
  histos[3]->Fill( (candidate.mass()-genCandidate.mass())/genCandidate.mass() , weight );
}

void
SemiLepHypothesesAnalyzer::fillJetCorrelHistos(const std::vector<int>& match, const std::vector<int>& matchCompare, const double& weight)
{

  hadBJetCorrel_->Fill( match[TtSemiLepEvtPartons::HadB]     +1, matchCompare[TtSemiLepEvtPartons::HadB]     +1, weight );
  hadQJetCorrel_->Fill( match[TtSemiLepEvtPartons::LightQ]   +1, matchCompare[TtSemiLepEvtPartons::LightQ]   +1, weight );
  hadPJetCorrel_->Fill( match[TtSemiLepEvtPartons::LightQBar]+1, matchCompare[TtSemiLepEvtPartons::LightQBar]+1, weight );
  lepBJetCorrel_->Fill( match[TtSemiLepEvtPartons::LepB]     +1, matchCompare[TtSemiLepEvtPartons::LepB]     +1, weight );

}

void
SemiLepHypothesesAnalyzer::fillQualityHistos(const TtSemiLeptonicEvent& semiLepEvt, const double& weight)
{

  // genMatch histos
  if( semiLepEvt.isHypoValid(TtSemiLeptonicEvent::kGenMatch) ) {
    genMatchSumDR_->Fill( semiLepEvt.genMatchSumDR() , weight );
    genMatchSumPt_->Fill( semiLepEvt.genMatchSumPt() , weight );
    genMatchSumDRVsSumPt_     ->Fill( semiLepEvt.genMatchSumDR() , semiLepEvt.genMatchSumPt()                                     , weight );
    genMatchSumDRVsHadWMass_  ->Fill( semiLepEvt.genMatchSumDR() , semiLepEvt.hadronicW  (TtSemiLeptonicEvent::kGenMatch)->mass() , weight );
    genMatchSumDRVsHadTopMass_->Fill( semiLepEvt.genMatchSumDR() , semiLepEvt.hadronicTop(TtSemiLeptonicEvent::kGenMatch)->mass() , weight );
    // vs. MVADisc
    if( semiLepEvt.isHypoValid(TtSemiLeptonicEvent::kMVADisc) )
      genMatchSumDRVsMVADisc_->Fill( semiLepEvt.genMatchSumDR() , semiLepEvt.mvaDisc() , weight );
    // vs. KinFit
    if( semiLepEvt.isHypoValid(TtSemiLeptonicEvent::kKinFit) )
      genMatchSumDRVsFitProb_->Fill( semiLepEvt.genMatchSumDR() , semiLepEvt.fitProb() , weight );
  }

  // MVADisc histos
  if( semiLepEvt.isHypoValid(TtSemiLeptonicEvent::kMVADisc) ) {
    mvaDisc_->Fill( semiLepEvt.mvaDisc() , weight );
    mvaDiscVsHadWMass_  ->Fill( semiLepEvt.mvaDisc() , semiLepEvt.hadronicW  (TtSemiLeptonicEvent::kMVADisc)->mass() , weight );
    mvaDiscVsHadTopMass_->Fill( semiLepEvt.mvaDisc() , semiLepEvt.hadronicTop(TtSemiLeptonicEvent::kMVADisc)->mass() , weight );
    // vs. kinFit
    if( semiLepEvt.isHypoValid(TtSemiLeptonicEvent::kKinFit) )
      mvaDiscVsFitProb_->Fill( semiLepEvt.mvaDisc() , semiLepEvt.fitProb() , weight );
  }

  // kinFit histos
  if( semiLepEvt.isHypoValid(TtSemiLeptonicEvent::kKinFit) ) {
    fitChi2_->Fill( semiLepEvt.fitChi2() , weight );
    fitProb_->Fill( semiLepEvt.fitProb() , weight );
    fitProbVsHadWMass_  ->Fill( semiLepEvt.fitProb() , semiLepEvt.hadronicW   (TtSemiLeptonicEvent::kKinFit)->mass() , weight );
    fitProbVsHadTopMass_->Fill( semiLepEvt.fitProb() , semiLepEvt.hadronicTop (TtSemiLeptonicEvent::kKinFit)->mass() , weight );
  }

}

bool
SemiLepHypothesesAnalyzer::sameJets(const TtSemiLeptonicEvent& semiLepEvt,
				    const TtSemiLeptonicEvent::HypoClassKey& hyp1,
				    const TtSemiLeptonicEvent::HypoClassKey& hyp2,
				    const std::vector<int>& jetsToCompare)
{

  std::vector<int> jetIndicesHyp1;
  std::vector<int> jetIndicesHyp2;

  for(unsigned i = 0; i < jetsToCompare.size(); i++) {
    jetIndicesHyp1.push_back( (semiLepEvt.jetLepComb(hyp1))[ jetsToCompare[i] ] );
    jetIndicesHyp2.push_back( (semiLepEvt.jetLepComb(hyp2))[ jetsToCompare[i] ] );
  }

  std::sort( jetIndicesHyp1.begin(), jetIndicesHyp1.end() );
  std::sort( jetIndicesHyp2.begin(), jetIndicesHyp2.end() );

  return (jetIndicesHyp1==jetIndicesHyp2);
  
}
