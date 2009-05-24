import FWCore.ParameterSet.Config as cms

#-------------------------------------------------
# test cfg file for tqaflayer1 & 2 production from
# fullsim for semi-leptonic ttbar events 
#-------------------------------------------------
process = cms.Process("Step0")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
#process.MessageLogger.cerr.FwkReport.reportEvery = 100

#-------------------------------------------------
# process configuration
#-------------------------------------------------

## define input
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    ## add your favourite file here    
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

## add event weight information
process.load("TopAnalysis.TopUtils.EventWeightPlain_cfi")
process.wght = cms.Path(process.eventWeight)

## test basic event selection
process.load("TopAnalysis.TopFilter.sequences.semiLepMuonSelection_step0_cff")
process.semiLepMuonSelection = cms.Path(process.slmFilterFullMon)

## register TFileService
process.TFileService = cms.Service("TFileService",
    fileName = cms.string('semiLepMuonSelection_step0.root')
)

## configure output module
process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('patTuple_semiLepMuon_step0.root')
)
process.p1 = cms.Path(process.out)
