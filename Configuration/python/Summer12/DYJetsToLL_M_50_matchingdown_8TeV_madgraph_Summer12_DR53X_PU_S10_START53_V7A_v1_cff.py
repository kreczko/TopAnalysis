import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/FEE6178D-11F9-E111-BF33-002590200B3C.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/FE31BD7C-45F9-E111-AE95-001E6739801B.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/FCF54D19-F7F8-E111-AE4C-001E6739751C.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/FCC16805-10F9-E111-9190-002590200874.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/FAEE33F0-01F9-E111-BA20-00259020083C.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/FAE0B4AE-07F9-E111-8446-001E6739692D.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/F6AC2FF7-2BF9-E111-95B1-00259020083C.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/F4F906BD-11F9-E111-8BC7-001E67398E49.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/F4E6211A-25F9-E111-A101-00259020081C.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/F4AA0A34-27F9-E111-8651-002590200A54.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/F45ACF77-0AF9-E111-8DEA-002590200A00.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/F2C8AAD8-2FF9-E111-B9AD-0025B3E05D74.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/F2A3D35C-20F9-E111-834A-001E67397E54.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/F270BE6B-22F9-E111-8049-003048D4772E.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/F0F67C14-FBF8-E111-AFE3-0025902008AC.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/F0D8ABF3-0AF9-E111-85AF-003048673F9C.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/F08223C1-0CF9-E111-A8B7-001E6739801B.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/EA070B1F-0CF9-E111-B401-002590200B74.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/E8E1547C-E7F8-E111-9B22-001E67396892.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/E88CFE6B-3EF9-E111-AB9A-003048D476E0.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/E888B20C-E4F8-E111-9072-001E67396C43.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/E693F42D-DCF8-E111-BD60-001E67396E1E.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/E61FA20F-20F9-E111-8930-003048D4600C.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/E4B3D8A5-F8F8-E111-8883-001E67397EEA.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/E0E24B56-36F9-E111-B955-002481E14E56.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/E02C6CE8-DAF8-E111-8D2B-001E67397E90.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/DE3E6872-30F9-E111-9310-001E67396707.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/DC490023-07F9-E111-9B8F-001E67397701.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/DA0F41C3-39F9-E111-BF55-00304867406E.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/D8C84E79-F1F8-E111-863C-002590200AD8.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/D87A5AC4-DEF8-E111-9955-002590200824.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/D2AC58B8-06F9-E111-99CD-001E67397F71.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/D25807D8-2CF9-E111-BCA1-003048D45FF4.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/D2259974-1DF9-E111-9923-0025902008D8.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/D20AA56D-1AF9-E111-A6C5-001E673970C1.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/D20A4D1B-51F9-E111-9804-002481E14C8A.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/D04861C7-E1F8-E111-8D39-003048673F3A.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/CE0F108F-DDF8-E111-8C4A-002590200B70.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/CCFC508D-17F9-E111-BAA5-001E6739675C.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/CCE5391F-D2F8-E111-947E-002590200824.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/CCBB28F6-12F9-E111-BA67-001E67398E49.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/CCA91525-FAF8-E111-9B0F-0025902008AC.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/CAB86AE9-FBF8-E111-B1C2-002590200A98.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/C8AB936B-0AF9-E111-86DC-001E673984C1.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/C8119122-09F9-E111-B656-001E6739801B.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/C4C8A66A-0CF9-E111-A1D3-001E67398381.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/C49C26D1-38F9-E111-8F9F-0025B3E05D68.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/C47C703D-2FF9-E111-9D24-003048D45FF2.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/C42D3208-15F9-E111-9900-001E67396A09.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/C29B21F8-32F9-E111-BE6B-0025B3E0653C.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/C2936B96-E4F8-E111-9487-002590200A98.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/C0F8163A-3CF9-E111-B965-003048673FC0.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/C0A4BE29-D6F8-E111-8ACA-002590200B60.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/C087DA63-E8F8-E111-AD2C-001E67397CAB.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/C051D772-30F9-E111-879E-002481E15000.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/BCB59FA9-2BF9-E111-8833-0025902009B0.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/BCA04232-4CF9-E111-B6B8-0025902008C4.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/BACC5F46-4BF9-E111-A2A0-002590200844.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/BAC1F73D-E0F8-E111-A54D-001E67397EEA.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/BA45E5A8-3AF9-E111-84FE-002590200894.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/BA1D46B2-0CF9-E111-AF6A-001E67397AD0.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/B8C16913-FFF8-E111-8529-002590200988.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/B8A14FB4-15F9-E111-A196-001E67396FA9.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/B639D297-14F9-E111-8DD9-002590200B68.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/B486422E-31F9-E111-B390-003048D460E4.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/B2C10FFE-1EF9-E111-8EFA-003048673EAA.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/B0FCF7FA-32F9-E111-A191-002590200988.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/B0F00123-49F9-E111-A5A2-001E67396A40.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/AE685667-F9F8-E111-85AA-002590200ADC.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/ACDD1962-18F9-E111-862E-001E67397D91.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/AC1844D1-34F9-E111-BA77-001E67397454.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/AA1CFB90-E4F8-E111-8977-001E67396E3C.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/A8849F8C-29F9-E111-8626-00259020084C.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/A83EC7AC-09F9-E111-BCD6-002590200B50.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/A81C8DF0-0DF9-E111-AF3C-002590200894.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/A436648A-0EF9-E111-8C6A-001E67397094.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/A0E3C3E7-CBF8-E111-9FEC-002590200B60.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/A053B856-DFF8-E111-BA27-001E673970FD.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/A04175BF-2AF9-E111-B32C-003048D47716.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/A035FC4C-3BF9-E111-9C63-002590200874.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/9E61B9A2-3FF9-E111-B9E9-0025B3E05CAA.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/9E11A093-EFF8-E111-BEE2-002590200930.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/9E109D59-0AF9-E111-AB78-001E67398043.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/9C9AE018-3EF9-E111-9633-0025B31E3C04.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/9C906E80-34F9-E111-9857-003048D47A7C.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/9C565EFB-3AF9-E111-B4E4-002590200B74.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/9C1C1FE6-FBF8-E111-8B1C-0025902008F4.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/9A4458D8-2CF9-E111-924E-001E67398025.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/98BA94CB-0BF9-E111-98F9-001E67397EEA.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/984003C7-0CF9-E111-9E31-001E6739811F.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/96618630-DEF8-E111-A654-001E67396D56.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/94A5A0DB-E0F8-E111-890C-001E67397701.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/92540F79-D7F8-E111-B4CD-001E67396707.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/924ABF49-F2F8-E111-BF70-00259020097C.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/9238A10E-1CF9-E111-AC84-002590200B68.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/92358F76-2DF9-E111-9A76-002590200934.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/921FBCA0-E2F8-E111-A3AF-0025902009B0.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/920D774C-E3F8-E111-AFF7-001E673969FF.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/90E00313-46F9-E111-A61C-003048673E7A.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/8EEFA0F8-E8F8-E111-B139-001E67397580.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/8CDF8522-41F9-E111-9C4D-0025B3E05DCA.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/8C7E9FD7-37F9-E111-BE14-001E67396BA3.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/8A699E81-3CF9-E111-B062-003048D460F8.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/84C51739-24F9-E111-80EA-003048673EAA.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/848B715D-12F9-E111-8943-001E67397756.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/8455634C-26F9-E111-8D64-001E67398CE1.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/82D0B777-41F9-E111-8449-003048673F12.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/807A0F52-26F9-E111-A77F-003048D45FD6.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/800150A6-14F9-E111-8CD9-002590200AE4.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/7E21CDD5-21F9-E111-833D-003048D4DBFC.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/7AF6C00F-32F9-E111-9194-9C8E991A143E.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/7AF425AA-07F9-E111-B5A6-001E67398633.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/7AD948D0-EDF8-E111-BD68-001E67396761.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/78543A66-10F9-E111-A9E3-002590200A58.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/784FC7F0-43F9-E111-8D78-002590200A54.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/74819290-37F9-E111-97D7-00259020081C.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/723D7E8C-04F9-E111-BC20-001E67396DCE.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/70EC24FE-FDF8-E111-AFDA-002590200B38.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/6ED0EFCC-0EF9-E111-AED7-001E67398C0F.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/6ECBF601-23F9-E111-A699-001E673973E1.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/6CFE5914-0EF9-E111-A357-001E67397008.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/6C7DA60D-2BF9-E111-9CF2-003048D4610E.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/6AFE9D3A-F6F8-E111-9CD8-001E67398408.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/6AF47734-F0F8-E111-A7F3-001E67396577.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/682F6163-EAF8-E111-BEAB-001E67397EDB.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/6825F404-47F9-E111-AE8A-002481E154EC.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/68059CEF-01F9-E111-B9FA-002590200810.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/66E4874B-FBF8-E111-BE54-001E67398156.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/64942821-09F9-E111-BE32-001E6739811F.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/62E85992-ECF8-E111-945B-0025902008DC.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/6281305D-1BF9-E111-8E68-001E67396FCC.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/609E301C-0FF9-E111-B425-0025902008D0.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/5E74DF9C-33F9-E111-A9F8-0025B3E063EA.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/5E6830E8-4DF9-E111-A352-002590200A54.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/56B2D435-38F9-E111-9F62-0025902009CC.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/56990DC2-18F9-E111-9DC0-001E67397F3F.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/568335CC-0BF9-E111-803D-001E67398381.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/562690CB-04F9-E111-9CC7-001E67397CB0.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/54FE3E27-3DF9-E111-8A75-001E67397BC5.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/52FDAFFD-07F9-E111-96C9-001E67396ACC.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/52EEF251-F8F8-E111-8080-002590200978.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/5257DA77-FAF8-E111-8E43-001E67398025.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/50A1DFE6-F2F8-E111-8055-001E67397B25.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/4E6F060D-11F9-E111-8F20-002590200B3C.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/4C8F6694-10F9-E111-B5CA-0025902008F0.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/489349BD-1DF9-E111-9F12-0025B3E05CF8.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/46261F00-29F9-E111-AAAE-003048D462AE.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/44CB7319-1DF9-E111-A5CF-002590200AF4.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/42F7F97D-1CF9-E111-BF82-001E67396C43.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/42662C1E-EAF8-E111-942B-001E673981C4.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/3E85705A-3FF9-E111-9DD5-001E67397C33.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/3C678AFC-20F9-E111-BA4C-001E67398791.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/3A876FC6-08F9-E111-915A-001E67397B1B.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/3887976A-FDF8-E111-912F-002590200824.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/387D9172-05F9-E111-982E-001E67397CBA.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/3805793B-4FF9-E111-BA17-003048D47768.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/366FA8F5-52F9-E111-B3D4-001E67397E1D.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/36211B55-56F9-E111-895C-002481E0DCD8.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/348AB069-EBF8-E111-A9F0-001E67397756.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/345AF55A-3AF9-E111-8FA0-0025B31E3C24.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/32993749-13F9-E111-AD6E-002590200970.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/2EA43B62-35F9-E111-A86A-003048D46098.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/2A3EF984-F6F8-E111-A647-002590200A88.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/28F0FFBC-2AF9-E111-9F5C-001E67398011.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/28B3669A-19F9-E111-89DE-001E67396761.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/288C12AA-E4F8-E111-B40D-001E67396D4C.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/2820AF08-E7F8-E111-B8A3-001E6739815B.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/26B0011F-09F9-E111-8382-003048673F9C.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/26411CDD-26F9-E111-9ACD-003048D45FDE.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/26352443-33F9-E111-9B6E-003048D479D2.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/2627B066-28F9-E111-B159-003048D45FDE.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/2491E6B6-39F9-E111-A7A0-001E67396ACC.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/24518120-0CF9-E111-8BE6-001E67398110.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/24163BD9-4CF9-E111-8104-0025B3E05D46.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/22CE5014-05F9-E111-A7EB-001E67396DCE.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/22471713-2BF9-E111-9D01-001E67397094.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/221C096A-E5F8-E111-B68A-001E67397008.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/20BB2306-1EF9-E111-A09D-0025B3E06578.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/1E6A3BF5-23F9-E111-8A0E-002590200988.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/1E336F86-0EF9-E111-8AD6-0025902008C4.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/1E06A8C4-E7F8-E111-B5FE-001E67398E12.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/1CA75399-04F9-E111-924F-001E67396BAD.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/1ADCD89D-2EF9-E111-B296-003048D47704.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/1A21B2BE-F4F8-E111-899D-002590200A6C.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/1A0B3E24-00F9-E111-9B20-003048673FC0.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/18E993B3-07F9-E111-8B45-0025902009B8.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/16F43A52-E6F8-E111-895F-001E67396D51.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/16C9B8B3-31F9-E111-862D-003048D479DE.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/16C619B6-35F9-E111-897B-001E67396A40.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/16A83CE0-FCF8-E111-808E-001E67397431.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/1292DC2C-02F9-E111-8EF1-002590200B6C.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/1239FF78-2DF9-E111-A336-00259020081C.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/0E2B3504-1AF9-E111-8DE2-001E67398683.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/0E285BB6-E5F8-E111-BBE7-001E67396D51.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/0C44DBC4-2DF9-E111-9903-001E67396C52.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/0C3C4F80-06F9-E111-8DDC-003048673F24.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/0C3207CA-E1F8-E111-A429-001E67397B11.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/0C01ACB4-5AF9-E111-8A07-003048D476EE.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/0AC5F73F-F4F8-E111-8A88-002590200A40.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/08467C0E-18F9-E111-BD08-001E67396A1D.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/06D7502C-2DF9-E111-8EF5-002590200858.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/06C4C93C-16F9-E111-8AC2-0025902008DC.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/06BAD9B8-DFF8-E111-9CBC-0025902008CC.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/067F3D70-FFF8-E111-96CD-002590200ADC.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/0600C909-4AF9-E111-8EAE-003048D479E8.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/04452BAB-0DF9-E111-9E0D-0025902008C4.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/043E10FD-28F9-E111-BFB1-001E67396A40.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/02A05283-E2F8-E111-96E7-003048673F3A.root',
       '/store/mc/Summer12_DR53X/DYJetsToLL_M-50_matchingdown_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/005E608E-44F9-E111-BE31-003048D45F5E.root' ] );


secFiles.extend( [
               ] )
