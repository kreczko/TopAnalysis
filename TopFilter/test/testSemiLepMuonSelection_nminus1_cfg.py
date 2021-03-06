import FWCore.ParameterSet.Config as cms

#-------------------------------------------------
# test cfg file for tqaflayer1 & 2 production from
# fullsim for semi-leptonic ttbar events 
#-------------------------------------------------
process = cms.Process("TEST")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 100

#-------------------------------------------------
# process configuration
#-------------------------------------------------

## define input
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    #PAT test sample
    'file:/afs/cern.ch/cms/PRS/top/cmssw-data/relval200-for-pat-testing/FullSimTTBar-2_1_X_2008-07-08_STARTUP_V4-AODSIM.100.root'
    )
)

## define maximal number of events to loop over
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

## configure process options
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(False)
)

## configure geometry
process.load("Configuration.StandardSequences.Geometry_cff")

## configure conditions
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('STARTUP_V4::All')

## Magnetic field now needs to be in the high-level py
process.load("Configuration.StandardSequences.MagneticField_cff")

#-------------------------------------------------
# tqaf configuration; if you want just to produce 
# tqafLayer2 on top of an already existing
# tqafLayer1 just comment the standard tqafLayer1
# production sequence
#-------------------------------------------------

## std sequence for tqaf layer1
process.load("PhysicsTools.PatAlgos.patSequences_cff")
process.p0 = cms.Path(process.patDefaultSequenceNoCleaning)

## add event weight information
process.load("TopAnalysis.TopUtils.EventWeightPlain_cfi")

process.load("TopAnalysis.TopFilter.sequences.semiLepMuonSelection_nminus1_cff")

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('analyzeSemiLepMuonEvents_nminus1_ttbar.root')
)

process.p1 = cms.Path(process.eventWeight     *
                      process.makeSemiMuonNon *
                      process.makeSemiMuonLep *
                      process.makeSemiMuonIso *
                      process.makeSemiMuonJet *
                      process.makeSemiMuonAll
                      )
                      

