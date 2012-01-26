import FWCore.ParameterSet.Config as cms

produceHadronLevelBJets = cms.EDProducer("HadronLevelBJetProducer",
    ttGenEvent = cms.InputTag('genEvt'),
    genJets = cms.InputTag('ak5GenJets'),
    deltaR = cms.double(0.5),
)


