jetType="PF"
dataSelector = 1
leptonTypeId = 13
triggerPathSelector1 = "HLT_IsoMu24_eta2p1_v*"
## NOTE the name change between V1ReReco and V4PromptReco!!!
triggerPathSelector2 = "HLT_IsoMu17_eta2p1_TriCentralJet30_v*"
cutflowSelector = "effOnly"
runOnAOD = True

jetMinNumber = 3

#execfile("TopAnalysis/Configuration/analysis/fullLeptonic/analyzeZMuMuTagAndProbe_cfg.py")
execfile("analyzeCrossTriggerRatios_cfg.py")

## 4540 files
process.load("TopAnalysis/Configuration/Fall11/wlnujets_MadgraphZ2_Fall11_AOD_cff")

process.TFileService.fileName = 'analyzeCrossTriggerRatiosMCFall11WJets_IsoMu24_eta2p1_IsoMu17TriJet.root'
process.maxEvents.input = 10000
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
