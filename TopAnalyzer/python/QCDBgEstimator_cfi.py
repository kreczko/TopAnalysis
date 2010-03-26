import FWCore.ParameterSet.Config as cms

estimateQCDBg = cms.EDAnalyzer("QCDBgEstimator",
    # source
    muons = cms.InputTag("selectedPatMuons"),     
    # option to weight events
    useEventWeight = cms.bool(True),
    # of the worse isolated muon's isolation
    isoBins = cms.vdouble(0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0) 
)


