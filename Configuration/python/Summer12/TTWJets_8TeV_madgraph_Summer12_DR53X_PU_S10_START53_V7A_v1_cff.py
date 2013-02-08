import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/0C570F59-B7DA-E111-A245-003048D437BA.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/287F5461-58DA-E111-98FB-0030487D70FD.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/34C820C1-AEDA-E111-A69E-003048D437DA.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/3EDACE8E-20DB-E111-A69A-0030487FA623.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/48348A82-B3DA-E111-B2BE-00266CF33118.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/54190A74-C4DA-E111-9841-003048C68F6A.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/58DD2ACA-F3DA-E111-B4FC-003048D436B4.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/5A61C025-B9DA-E111-ADFC-003048D437F2.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/72782730-41DA-E111-84D8-003048C69292.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/6A9B5383-97DA-E111-94EB-0030487F1BCD.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/8676B4E2-EEDA-E111-9241-0030487F1F23.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/88C32C1D-C5DA-E111-9E90-003048F0E188.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/78853135-9CDA-E111-92CF-0030487E5247.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/9A2E7FF6-BCDA-E111-9EC6-003048C692BA.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/AA8C56B8-97DA-E111-B431-003048C693B8.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/AEC6FE4C-E5DA-E111-8AAF-0030487EBB27.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/B69D6CCF-E8DA-E111-9CD8-0030487F929B.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/A4438E84-97DA-E111-BF02-002481E101DA.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/BC6CDAA5-61DA-E111-B8D3-0030487F1A49.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/C0E0E318-A9DA-E111-AA03-003048D438EA.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/CEF7737C-9FDA-E111-94E9-0030487F1BCF.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/D4028F46-E0DA-E111-AD92-003048D3C7DC.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/AA5029D5-A2DA-E111-9E33-0030487F0EDD.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/D441AD8B-9DDA-E111-8A4E-0030487CF3F7.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/E8445539-C2DA-E111-AE1B-0030487D5E75.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/BE146CF7-B0DA-E111-9D83-002481E94B6C.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/E0216244-99DA-E111-A871-003048C6617E.root',
       '/store/mc/Summer12_DR53X/TTWJets_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/E67C6173-9BDA-E111-BAF3-0030487F1309.root' ] );


secFiles.extend( [
               ] )

