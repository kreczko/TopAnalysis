import FWCore.ParameterSet.Config as cms

#-------------------------------------------------
# cfg file for the analysis of selected muon
# quantities
#-------------------------------------------------
process = cms.Process("TopQuark")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 1
## configure process options
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

#-------------------------------------------------
# process configuration
#-------------------------------------------------

## define input
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(    
    ## add your favourite file here
    #'/store/user/jlange/Mu/PAT_Nov4RerecoL1IncludedUHH/e37a6f43ad6b01bd8486b714dc367330/DataNov4RerecoL1included_9_1_0dl.root'
    #'/store/user/henderle/TTJets_TuneD6T_7TeV-madgraph-tauola/PAT_FALL10HH/6c1c00d4602477b58cef63f182ce0614/fall10MC_9_1_WVh.root'
    '/store/user/henderle/TTJets_TuneD6T_7TeV-madgraph-tauola/PAT_FALL10HH/6c1c00d4602477b58cef63f182ce0614/fall10MC_5_1_wzx.root'
    #'/store/user/mgoerner/WJetsToLNu_TuneD6T_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_9_1_c8G.root'
    )
)

## define maximal number of events to loop over
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)
## skip events
process.source.skipEvents = cms.untracked.uint32(0)

#-------------------------------------------------
# top analysis
#-------------------------------------------------
## ---
##    a) produce top generated event
## ---
process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff"       )
process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEventFilters_cff")
process.ttSemiLeptonicFilter.allowedTopDecays.decayBranchA.electron = False
process.ttSemiLeptonicFilter.allowedTopDecays.decayBranchA.muon     = True
## ---
##    b) configure event selection
## ---
process.load("TopAnalysis.TopFilter.sequences.semiLeptonicSelection_cff")
## muon selection
process.load("TopAnalysis.TopFilter.sequences.muonSelection_cff")
process.muonSelection = process.muonSelection.clone       (src = 'tightMuons'      , minNumber = 1, maxNumber = 99999999)
process.jetSelection  = process.leadingJetSelection.clone (src = 'tightLeadingPFJets', minNumber = 4)
## jet selection
process.load("TopAnalysis.TopFilter.sequences.jetSelection_cff")
## redefine veto jets to be sure it is also replaced when running on PF
from TopAnalysis.TopFilter.sequences.jetSelection_cff import goodJets
process.vetoJets.src="goodJetsPF30"
process.vetoJets.cut=''

## ---
##    c) configure KinFit
## ---
## choose which hypotheses to produce
process.load('TopQuarkAnalysis.TopEventProducers.sequences.ttSemiLepEvtBuilder_cff')
from TopQuarkAnalysis.TopEventProducers.sequences.ttSemiLepEvtBuilder_cff import *
addTtSemiLepHypotheses(process,['kKinFit'])
## process.ttSemiLepJetPartonMatch.verbosity = 1
process.kinFitTtSemiLepEventHypothesis.leps = 'tightMuons' #'tightMuons'
process.kinFitTtSemiLepEventHypothesis.jets = 'tightLeadingPFJets'#'selectedPatJetsAK5PF'
process.kinFitTtSemiLepEventHypothesis.mets = 'patMETsPF'

# maximum number of jets to be considered in the jet combinatorics
# (has to be >= 4, can be set to -1 if you want to take all)
process.kinFitTtSemiLepEventHypothesis.maxNJets = 5

# maximum number of jet combinations finally written into the event, starting from the "best"
# (has to be >= 1, can be set to -1 if you want to take all)
process.kinFitTtSemiLepEventHypothesis.maxNComb = 3

# set constraints:: 1: Whad-mass, 2: Wlep-mass, 3: thad-mass, 4: tlep-mass, 5: nu-mass, 6: equal t-masses
process.kinFitTtSemiLepEventHypothesis.constraints = [1, 2, 6]

# consider b-tagging in event reconstruction
#process.kinFitTtSemiLepEventHypothesis.bTagAlgo = "trackCountingHighEffBJetTags"
process.kinFitTtSemiLepEventHypothesis.bTagAlgo = "simpleSecondaryVertexHighEffBJetTags"

# TCHE discr.values 7TeV: 1.7, 3.3, 10.2
process.kinFitTtSemiLepEventHypothesis.minBDiscBJets     = 1.74
process.kinFitTtSemiLepEventHypothesis.maxBDiscLightJets = 1.74
process.kinFitTtSemiLepEventHypothesis.useBTagging       = True

# keep only events with unambigues parton matches
# (no other partons exist in dR=0.3 cone) 
# attention: improves purity but reduces efficiency
process.ttSemiLepJetPartonMatch.algorithm = "unambiguousOnly"
#process.ttSemiLepJetPartonMatch.algorithm = "totalMinDist"
process.ttSemiLepJetPartonMatch.useMaxDist = True
## set number of jets considered in jet-parton matching
process.ttSemiLepJetPartonMatch.maxNJets=-1
## choose jet collection considered in jet-parton matching
process.ttSemiLepJetPartonMatch.jets='tightLeadingPFJets'
    
## configure module you would like to test
process.load("TopAnalysis.TopAnalyzer.HypothesisKinFit_cfi"    )
hypoKinFit = cms.PSet(hypoKey = cms.string("kKinFit"),
                      wantTree = cms.bool(True),
                      maxNJets = process.kinFitTtSemiLepEventHypothesis.maxNJets)
process.analyzeHypothesisKinFitModule = process.analyzeHypothesisKinFit.clone(analyze=hypoKinFit)

#process.load("TopAnalysis.TopAnalyzer.HypothesisKinFitMET_cfi" )
#process.load("TopAnalysis.TopAnalyzer.HypothesisKinFitJets_cfi")
#process.load("TopAnalysis.TopAnalyzer.HypothesisKinFitMuon_cfi")

## ## configure top reconstruction analyzers
process.load("TopAnalysis.TopAnalyzer.TopKinematics_cfi")

## define PSets for top reconstruction analyzer
## 1) event hypothesis built of objects from genmatch to partons (ttSemiLepJetPartonMatch)
recoGenMatch      = cms.PSet(hypoKey=cms.string('kGenMatch'), useTree=cms.bool(True), matchForStabilityAndPurity=cms.bool(False), ttbarInsteadOfLepHadTop = cms.bool(False), maxNJets = process.kinFitTtSemiLepEventHypothesis.maxNJets)
## 2) event hypothesis built of objects as defined above
recoKinFit        = cms.PSet(hypoKey=cms.string('kKinFit'  ), useTree=cms.bool(True), matchForStabilityAndPurity=cms.bool(False), ttbarInsteadOfLepHadTop = cms.bool(False), maxNJets = process.kinFitTtSemiLepEventHypothesis.maxNJets)
## 4) event hypothesis built with generator truth informations
genTtbarSemiMu    = cms.PSet(hypoKey=cms.string("None"     ), useTree=cms.bool(True), matchForStabilityAndPurity=cms.bool(False), ttbarInsteadOfLepHadTop = cms.bool(False), maxNJets = process.kinFitTtSemiLepEventHypothesis.maxNJets)

# a) as reconstructed from kinFit after reco selection
process.analyzeTopRecoKinematicsKinFit        = process.analyzeTopRecKinematics.clone(analyze=recoKinFit  )
# b) as reconstructed from genmatched objects after reco selection
process.analyzeTopRecoKinematicsGenMatch      = process.analyzeTopRecKinematics.clone(analyze=recoGenMatch)
# c) as reconstructed from generator objects after gen selection
process.analyzeTopGenLevelKinematics          = process.analyzeTopGenKinematics.clone(analyze=genTtbarSemiMu)

## register TFileService
process.TFileService = cms.Service("TFileService",
    fileName = cms.string('analyzeHypothesisKinFit.root')
)

process.p1 = cms.Path(## ttbar semilept. mu only
                      process.makeGenEvt             *
                      process.ttSemiLeptonicFilter   *
                      ## introduce some collections
                      process.semiLeptonicSelection  *
                      process.makeTtSemiLepEvent     *
                      ## event selection
#                      process.muonSelection          *
#                      process.jetSelection           *
                      ## KinFit monitoring modules
                      process.analyzeHypothesisKinFitModule         *
                      process.analyzeTopRecoKinematicsKinFit        *
                      process.analyzeTopRecoKinematicsGenMatch      *
                      process.analyzeTopGenLevelKinematics          
#                      process.analyzeHypothesisKinFitMET *
#                      process.analyzeHypothesisKinFitJets *
#                      process.analyzeHypothesisKinFitMuon
                      )
## switch to SSV btagging
from PhysicsTools.PatAlgos.tools.helpers import massSearchReplaceAnyInputTag
massSearchReplaceAnyInputTag(process.p1, 'tightBottomPFJets', 'simpleSecondaryVertexHighEffBJets')
process.simpleSecondaryVertexHighEffBJets.src="goodJetsPF30"
process.p1.replace(process.semiLeptonicSelection, process.semiLeptonicSelection*process.simpleSecondaryVertexHighEffBJets)
