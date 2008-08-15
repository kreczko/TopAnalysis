#ifndef MatrixAnalyzer_h
#define MatrixAnalyzer_h
/**
 *  class:   MatrixAnalyzer.h
 * @author: Lukas Kreczko, Uni Hamburg (lkreczko@mail.desy.de)
 * version $Id: MatrixAnalyzer.h,v 1.6 2008/08/13 12:01:20 kreczko Exp $

 ________________________________________________________________**/
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "PhysicsTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/Candidate/interface/CandMatchMap.h"

#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "TopAnalysis/TopUtils/interface/NameScheme.h"
#include "TopAnalysis/TopUtils/interface/RootSystem.h"
#include "TopAnalysis/TopUtils/interface/RootHistograms.h"
#include "TopAnalysis/TopAnalyzer/plugins/LeptonCounter.h"

#include "DataFormats/RecoCandidate/interface/RecoCandidate.h"

class MatrixAnalyzer: public edm::EDAnalyzer {

public:
	explicit MatrixAnalyzer(const edm::ParameterSet&);
	~MatrixAnalyzer();

private:

	virtual void beginJob(const edm::EventSetup&);
	virtual void analyze(const edm::Event&, const edm::EventSetup&);
	virtual void endJob();
	virtual void setEnv(int &);
	virtual void getBefore();
	virtual double getHist(TString, TString, int&);
	//	virtual int pdgOfMother(pat::Muon matchedMuon,edm::Handle<reco::GenParticleCollection> genParticles);
	//	virtual bool matchedMuonIsContainedInDaughter(reco::GenParticleCollection::const_iterator part, reco::Muon muon);
	template<typename T1, typename T2> void log(T1 msg, T2 from, bool debug) {
		if (debug && debug_ || !debug)
			cout << from << ": " << msg << endl;
	}
	int numberOfmatchedMuons(edm::Handle<edm::View<pat::Muon> >,
			edm::Handle<edm::Association<reco::GenParticleCollection> >);
	std::string hist_, pmodulename_;
	bool before_, debug_;
	//int numberOfSignalL, numberOfSignalT, numberOfBgL, numberOfBgT;
	//double eff_Signal, eff_Bg;
//	int hadrCount_, lCount_, llCount_, mlCount_,
	int noBins_, beforeBin_, afterBin_;
//	int rhadrCount_, rlCount_, rllCount_, rmlCount_;
//	double whadrCount_, wlCount_, wllCount_, wmlCount_;
//	Double_t bgBefore_, slBefore_, dlBefore_, mlBefore_;
//	double effBG_, effSL_, effDL_, effML_,
	double sampleweight_;
	edm::InputTag muons_;
	edm::InputTag var_;
	std::vector<double> varBins_;
	typedef std::vector<pat::Muon> TopMuonCollection;

	std::map<int, TopMuonCollection> mothermap_;

	TH1F *background_, *binnedBkg_;

	TH1F *lep_, *binnedSemiLep_;

	TH1F *llep_, *binnedDiLep_;

	TH1F * multilep_, *binnedMultiLep_;

	TH1F *eff_, *binnedEff_;

	TFile *f_;

	TH1F *varPlot_;
	LeptonCounter *Counters_, *countersBefore_, *effCounter_, *effErrors_;
	//TODO: boolean for before and after. use same histograms, but different bins
	//TODO: try to find a way to store double directly in root file



};
#endif
