import FWCore.ParameterSet.Config as cms

## high level trigger filter
from HLTrigger.HLTfilters.hltHighLevel_cfi import *

## ---
##    setup trigger filter path
## ---
## single-muon trigger, threshold pt > 9 GeV, no isolation requirements
hltMu9 = hltHighLevel.clone(HLTPaths = ["HLT_Mu9"])
## single-electron trigger, threshold et > 15 GeV + electronID, no isolation requirements
hltEle15 = hltHighLevel.clone(HLTPaths = ["HLT_Ele15_SW_EleId_L1R"])
## 4 jet trigger, threshold pt > 30 GeV
hltQuadJet30 = hltHighLevel.clone(HLTPaths = ["HLT_QuadJet30"])
## sum of pts of jets HT > 200 GeV (uncorrected)
hltHt200 = hltHighLevel.clone(HLTPaths = ["HLT_HT200"])
## 1 jet trigger, threshold pt > 80 GeV
hltJet80 = hltHighLevel.clone(HLTPaths = ["HLT_Jet80"])
## 2 jet trigger, threshold pt > 50 GeV (uncorrected)
hltDiJet50 = hltHighLevel.clone(HLTPaths = ["HLT_DiJetAve50U"])
