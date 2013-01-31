import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/041D4456-B3DA-E111-A80D-0030487F1BD5.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/06BE490F-DEDA-E111-9DDD-0030487F1BD3.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/0081641E-ACDA-E111-83BD-0030487E5247.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/103FBC54-DCDA-E111-A835-0030487F132D.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/04936B8D-C5DA-E111-97D1-0030487E4EBF.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/12F3AAB8-C9DA-E111-B5F9-003048C692DA.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/04FA8A6A-C6DA-E111-BFCA-0030487F929F.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/164E411F-CDDA-E111-B24A-003048C693EC.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/06CA50B0-CADA-E111-8B71-003048C692B4.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/0A7A29B6-C9DA-E111-8C12-003048D462DC.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/2466D58E-B7DA-E111-A6F9-003048C692BA.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/2477F286-A0DA-E111-B31B-002481E0DA96.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/2486316E-C5DA-E111-AF95-003048D436EA.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/266B4DB4-D6DA-E111-8985-0030487F1653.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/28E26ECC-D8DA-E111-8BEB-002481E0E912.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/108609F1-B5DA-E111-BD73-0030487D7105.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/2ED3F853-D5DA-E111-8028-0030487F1A67.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/1614704C-32DB-E111-A9D8-0030487D8151.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/34F8BDA3-D1DA-E111-A983-0030487D5DC3.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/1A88E822-BCDA-E111-BC2C-0030487D5E4B.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/36511D6D-C6DA-E111-877C-002481E15184.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/1E4480B5-03DB-E111-A19C-002481E1070E.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/2E1312AD-96DA-E111-887C-0030487D5EBB.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/348CE302-CDDA-E111-8EAB-0030487F92B5.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/3C712380-C8DA-E111-B77F-0030487CF3F7.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/364285EE-A5DA-E111-A2BC-0030487F132D.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/38BE2239-CCDA-E111-96D9-003048D47912.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/3C215F24-C5DA-E111-B526-003048F0E1B2.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/3C6549BE-C5DA-E111-BEB5-003048F0E1AC.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/4030188F-C0DA-E111-BFEC-0030487E4EBF.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/420593BB-C9DA-E111-A095-003048C68A98.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/483F4B06-E6DA-E111-AEC6-0030487D5EA9.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/4AC9D28F-D5DA-E111-98B4-00266CFB8D74.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/42DE7C28-CCDA-E111-B61B-0030487E4EB7.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/44C35AA9-BDDA-E111-8F65-003048C692BA.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/56B19125-C4DA-E111-ACC1-0030487F932D.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/56D69E4D-D8DA-E111-A308-003048C692FA.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5845A713-9EDA-E111-82BB-0030487FA629.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/46BB1142-D3DA-E111-AF40-0030487F9295.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5AD1C069-C8DA-E111-9CCD-0030487E54B5.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5C084CC1-C5DA-E111-926E-002481E94B2A.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/46C46B81-D6DA-E111-9691-003048C69314.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5E69C47C-C5DA-E111-9A2E-003048F0E188.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5E9A07C7-CADA-E111-B1A3-003048D2BB3E.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5EA8947B-D5DA-E111-A20A-003048D4DFAA.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/4C9A0EDB-BCDA-E111-A7A4-003048C68A88.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5007C67B-D0DA-E111-B3DD-0030487F9151.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/60154DE8-D2DA-E111-B669-003048D43996.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/601D584F-D6DA-E111-A926-0030487D5D89.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5A90BC37-CCDA-E111-9B67-0030487F933F.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5CB57084-A4DA-E111-A9FD-0030487F9367.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5ED9E7C5-C5DA-E111-8727-002481E1026A.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5EE95A44-BADA-E111-A8C7-0030487E0A29.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/606FEF54-E2DA-E111-90C3-0030487D5E49.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/64130844-D3DA-E111-B47B-0030487D70FD.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/6437262C-CCDA-E111-AF1E-003048C693EA.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/72AC2EA8-C9DA-E111-A3A4-0030487EBB2B.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/72C91221-C3DA-E111-9884-00266CF2ABA8.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/740F4761-CFDA-E111-8ACE-003048C693C8.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/665C3CEC-E7DA-E111-A1E1-003048F02CBA.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/7423E367-B9DA-E111-B168-003048D439A0.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/6A10B26F-C8DA-E111-B8AF-0030487D5D91.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/6A4439CA-DADA-E111-BC16-0030487D8635.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/7816B6A9-DFDA-E111-A089-0030487D858B.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/7889F35F-CEDA-E111-AE91-003048D436B4.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/6A7B30A8-C9DA-E111-9C9B-0030487EBB2B.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/7A74687C-B9DA-E111-9B26-003048C692B8.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/826F2BA0-DEDA-E111-9067-0030487D814D.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/7413C44C-CCDA-E111-9221-0030487F929B.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/84FEEF54-CFDA-E111-906F-0030487E4ED3.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/74A54E7D-A7DA-E111-A605-0030487D5D67.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/8A260993-D1DA-E111-85A9-0030487E55B9.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/8ACEBB48-D5DA-E111-98FB-0030487F1653.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/74CAFB2B-C2DA-E111-BC71-003048D4610C.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/8E206A6A-CDDA-E111-BE1C-003048C692E4.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/8E2AA808-D3DA-E111-B853-003048D3CB3C.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/90D89436-CCDA-E111-BB65-003048D439C0.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/92F1854B-C4DA-E111-AC4F-003048D4DCD8.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/7A2C7DB6-BCDA-E111-859E-0030487D5E45.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/84A9143B-D3DA-E111-A622-00237DE0BED6.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/8855642A-C1DA-E111-8191-003048C6931E.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/8C7FEA94-CFDA-E111-9F17-0030487D7B79.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/92FA5632-CCDA-E111-97AF-002481E10CC2.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/96436075-BFDA-E111-8109-0030487F1A47.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/98781D23-C3DA-E111-8796-003048D373CC.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/A60E7F27-AADA-E111-91DE-003048C676E0.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/AA301D75-B6DA-E111-8F50-0030487D7105.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/A68197E0-D8DA-E111-8255-0030487D5DA9.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/AE6AA460-D3DA-E111-B973-003048C68A98.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/A6928D41-D5DA-E111-86BC-003048D4365C.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B4C60700-D3DA-E111-A0BB-003048C693D2.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B4DE8A1E-C4DA-E111-9BA9-002481E76052.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/A8115E3F-C2DA-E111-A0F1-0030487F1A31.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B8765C8E-C8DA-E111-B2E4-0030487E5101.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/BA2B06BD-CADA-E111-92D6-003048D436FE.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/A838767B-CEDA-E111-A2E8-003048D4DEDC.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/BCC48B5A-C6DA-E111-9F70-003048F0E3BE.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C0881A1C-C2DA-E111-AF8A-003048D47976.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C2933A11-BEDA-E111-AD5A-003048C69032.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C2CA6023-C2DA-E111-9D51-003048C693E6.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C2E963D5-C5DA-E111-ACE8-00215AD4D6E2.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/ACF55062-CEDA-E111-BBBD-003048D43730.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C482F35C-C8DA-E111-9F65-0030487D5EA9.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C4D7B04F-CDDA-E111-9712-002481E76052.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/AE76ACAB-DDDA-E111-B1BD-003048C6931C.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/CA0DF907-CDDA-E111-95E2-0030487EAFF9.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/CA159684-BFDA-E111-B38F-0030487F1A49.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B66ECC5C-C6DA-E111-B6CE-003048C693E4.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/CC6EC97A-D1DA-E111-A870-003048C68A88.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/BA2B5734-BCDA-E111-B58E-003048C692BA.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C407F45D-CEDA-E111-BACD-0030487D7B79.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D09FBE25-BBDA-E111-B185-0030487D5E49.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D21B1835-BBDA-E111-8143-003048D437DA.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D4EB5186-D1DA-E111-A8E2-0030487D8541.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D690D340-D0DA-E111-9A17-0030487F1F23.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/DAE1344D-E0DA-E111-8744-003048C68F6A.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C8E35B58-CDDA-E111-8445-003048D43730.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/CA30CB62-C8DA-E111-A69C-0030487FA4C9.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/E0322B5B-C1DA-E111-9706-0030487F92FB.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/E06E034E-D3DA-E111-9BA0-003048D439A6.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/CE1634C2-CADA-E111-AECD-003048D43734.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/E695A33F-C4DA-E111-8B5D-003048D4797E.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/E6DE8A67-C6DA-E111-B39B-002481E101DA.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/EA0F9BCD-C5DA-E111-8229-003048C662D4.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/EA17CA19-D9DA-E111-9623-003048C693D0.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/EA2FE268-D7DA-E111-9665-003048D43656.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/EAD5EA9A-C9DA-E111-91B2-003048CF632C.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/EC01DC70-CFDA-E111-9775-0030487D5EAD.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D089B09E-B6DA-E111-B9DB-003048D43734.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/DC109CA4-BEDA-E111-BF0C-003048D3CB3C.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/DE601D7C-AFDA-E111-ADD4-002481E0D974.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/F0C617D0-CADA-E111-8864-0030487DA061.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/E65C6BD2-C5DA-E111-9908-002481E0EA70.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/F62DF20B-D9DA-E111-8B9A-0030487D5EB3.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/ECE5B505-CDDA-E111-A720-0030487F1BE5.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/F6F2DAE1-B4DA-E111-AB4F-0030487F1651.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/EE3C26A4-C9DA-E111-85B0-0030487F92B1.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/F851DF36-D7DA-E111-91EA-0030487D8151.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/EECD83AD-D6DA-E111-A765-0030487F1BE5.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/F62232EE-ADDA-E111-884D-003048D4365C.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/FA3AEDBD-C5DA-E111-8E01-003048F0E3BE.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/FA40844C-DBDA-E111-AA12-0030487E54B7.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/F65FEE45-D0DA-E111-A4AB-003048D439A0.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/FCCDF91E-C3DA-E111-A711-003048CF6332.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/F6FE77C2-DADA-E111-A4AC-0030487D5DBB.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/F86AAEA1-E3DA-E111-A2C5-003048C6931E.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/F8C0F097-C8DA-E111-B086-0030487D5E4B.root',
       '/store/mc/Summer12_DR53X/TToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/FC42C74F-C8DA-E111-ACD2-003048D43724.root' ] );


secFiles.extend( [
               ] )
