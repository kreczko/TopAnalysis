#ifndef MatrixAnalyzer_h
#define MatrixAnalyzer_h
/**
 *  class:   MatrixAnalyzer.h
 * @author: Lukas Kreczko, Uni Hamburg (lkreczko@mail.desy.de)
 * version $Id: MatrixAnalyzer.h,v 1.9.4.2 2008/12/01 17:03:51 kreczko Exp $

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
#include "DataFormats/PatCandidates/interface/Jet.h"

class MatrixAnalyzer: public edm::EDAnalyzer {

public:
	explicit MatrixAnalyzer(const edm::ParameterSet&);
	~MatrixAnalyzer();

private:

	virtual void beginJob(const edm::EventSetup&);
	virtual void analyze(const edm::Event&, const edm::EventSetup&);
	virtual void endJob();
	virtual void setEnv();
//	virtual void getBefore();
//	virtual double getHist(TString, TString, int);

	template<typename T1, typename T2> void log(T1 msg, T2 from, bool debug) {
		if (debug && debug_ || !debug)
			cout << from << ": " << msg << endl;
	}
	int numberOfmatchedMuons(edm::Handle<edm::View<pat::Muon> >,
			edm::Handle<edm::Association<reco::GenParticleCollection> >);
	std::string hist_;//, pmodulename_;
	bool debug_;
	int noBins_;//, beforeBin_, afterBin_;
	double sampleweight_;
	edm::InputTag muons_;
	edm::InputTag var_, jets_, mva_;
	edm::ParameterSet bins_;
	//std::vector<double> varBins1_, varBins2_, varBins3_, varBins4_;
	std::string mvamodule_;
	//std::string notNeededHists_;
	typedef std::vector<pat::Muon> TopMuonCollection;
	typedef std::vector<pat::Jet>  TopJetCollection;
	std::vector<double> varBins_, mvaDiscBins_;
	bool useMVA_;
	std::string module_;
	std::string discinput_;

	std::map<int, TopMuonCollection> mothermap_;

	TH1F *nVSmet_, *nVSmetSimple_, *nVSdisc_, *nVSdiscSimple_;



	TH1F *varPlot_;
	LeptonCounter *Counters_;
};
#endif
