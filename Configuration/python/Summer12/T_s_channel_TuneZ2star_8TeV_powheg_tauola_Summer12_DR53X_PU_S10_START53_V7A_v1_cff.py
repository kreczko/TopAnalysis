import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/0AC0A593-1AEA-E111-9DA4-0026189438C0.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/2A8C005D-19EA-E111-A59C-0026189438D2.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/3C50727B-21EA-E111-841C-003048FFD7A2.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/42246509-1CEA-E111-8E2A-003048FFD744.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/44DE7F01-16EA-E111-A570-003048678E8A.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/0A7905FA-18EA-E111-9A39-0026189438DF.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/0EC81816-37EA-E111-A074-003048FFCBFC.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/1C83475F-19EA-E111-9DEA-002354EF3BDA.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/2E503BC8-14EA-E111-94C9-00261894387A.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/72399048-35EA-E111-960C-001BFCDBD100.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/745DD721-2BEA-E111-AEFF-00261894389D.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/565E3AD6-44EA-E111-9D46-0018F3D0960A.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/56979CE6-16EA-E111-9F65-0026189438FD.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/583E02C4-39EA-E111-9D3D-0018F3D095F2.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/68278F16-34EA-E111-8554-003048FFCB8C.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/7AFDD01C-18EA-E111-A575-00261894386F.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/84A764F1-23EA-E111-9DA9-0018F3D095EE.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/8E5510F1-1FEA-E111-8855-0018F3D096B4.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/8EEAB2EC-19EA-E111-8641-003048FFD756.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/AC7568CC-08EA-E111-A6C3-00304867C1BA.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/AE396C1A-19EA-E111-8747-0026189438F2.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B254E16D-18EA-E111-9961-003048678B70.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B89A396F-18EA-E111-BE21-0026189438C0.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/BC12E84F-26EA-E111-AF5B-003048FFCBA4.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/BC6EBE31-17EA-E111-94AD-002618FDA216.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C2DFF9B9-22EA-E111-BD53-0018F3D0960E.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/CCCCBEEE-31EA-E111-955F-003048FFD736.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/CE49ECD9-17EA-E111-A590-0026189438E8.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D4A66310-2FEA-E111-8C1A-0018F3D096F8.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/E6359E7A-0CEA-E111-89B8-0026189438A2.root',
       '/store/mc/Summer12_DR53X/T_s-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/FA60F350-38EA-E111-9A5B-001A9281171C.root' ] );


secFiles.extend( [
               ] )

