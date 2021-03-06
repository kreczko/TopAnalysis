import FWCore.ParameterSet.Config as cms

##########################################################################################
# Dataset: /QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/Summer11-PU_S4_START42_V11-v1/AODSIM #
# Events : 2030033                                                                       #
# eff    : 0.00242                                                                       #
# genXSec: 59.440.000 (LO PYTHIA)                                                        #
##########################################################################################

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource", fileNames = cms.untracked.vstring( *(
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/F86F7CD8-388C-E011-B700-0017A4770C3C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/F81ECAC6-398C-E011-9A63-1CC1DE1CEFC8.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/F6E097D5-748C-E011-863C-0017A4770C00.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/F633F9B9-778C-E011-903F-00237DA1ED1C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/F612252A-CF8C-E011-98A0-1CC1DE047FD8.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/F4A7281E-6D8C-E011-AFA0-0017A477003C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/F26C590A-7E8C-E011-A2B9-0022649E7902.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/F0DA7386-808C-E011-A498-00237DA1ED1C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/EEC9AE1B-9B8C-E011-A1AA-0017A4771008.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/ECB48014-6F8C-E011-817C-0017A477102C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/EA0629B7-6F8C-E011-B1F3-1CC1DE052068.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/E8797496-7E8C-E011-B752-0025B3E0216C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/E28AD7FF-6A8C-E011-88D9-0017A477102C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/E0B3D52E-718C-E011-8993-0017A4770004.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/E0AF17BC-738C-E011-9B06-0017A4771018.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/E066B044-878C-E011-8F9E-00237DA2F1DC.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/E03D8A4C-748C-E011-B6DA-0017A477081C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/DE7F0671-7F8C-E011-866F-00237DA14FF4.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/DC83B11F-6A8C-E011-B285-1CC1DE051038.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/D4CDA619-758C-E011-851D-0017A4771000.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/D4AAF2F1-8C8C-E011-86EF-001E0B5F3148.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/D2FC764F-748C-E011-B3BA-0017A4770408.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/D0AF03E5-828C-E011-9779-0025B3E0216C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/C45A65EB-768C-E011-8382-0017A477102C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/C29D57E7-6F8C-E011-BA1D-00237DA10D06.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/BE7652E0-7E8C-E011-93F0-0017A4771000.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/BE32C440-828C-E011-9F11-0017A477102C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/BC4CE4D9-388C-E011-8E03-1CC1DE1CDD02.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/B4FCD652-6B8C-E011-B9B4-0017A4771030.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/B21D427C-7B8C-E011-BB97-78E7D164BFC8.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/B0CBEBD7-7E8C-E011-9FFE-00237DA15C00.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/AE152E16-708C-E011-8A5C-0017A477102C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/A8E90018-698C-E011-BD07-0017A4770400.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/A4AD1040-768C-E011-9153-00237DA12FB2.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/A42AC30D-798C-E011-A739-0017A4771034.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/A0E8DC02-798C-E011-8AC7-0025B3E0228C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/9ED01479-6C8C-E011-A808-1CC1DE051038.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/9EAC9C35-6F8C-E011-B2A2-0017A4770828.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/9E98058A-398C-E011-BFB4-0017A4770C08.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/9A8D97B7-658C-E011-AA95-1CC1DE046F78.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/9860B9BD-6C8C-E011-8603-0017A4770414.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/98010CB8-6A8C-E011-9B49-0017A4770800.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/94E1AF32-7A8C-E011-B416-00237DA1ED1C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/94A1B354-858C-E011-B65D-0025B3E0216C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/90F2E95E-708C-E011-A70E-001F29C424E4.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/8E893C87-748C-E011-9EBA-0017A4771024.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/8A8BC0C7-438C-E011-9419-001E0B476FA4.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/8666E1B1-758C-E011-809E-0017A4770020.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/82E3A6E8-648C-E011-88A6-0017A4770400.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/8210E55A-698C-E011-9CAC-0017A477080C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/80DDDB82-398C-E011-86CC-1CC1DE1D2028.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/7CF157B5-398C-E011-99C8-1CC1DE1CF1BA.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/7C5A892C-738C-E011-A5F7-0017A4771000.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/7A2F3AE2-708C-E011-8D07-1CC1DE053050.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/74B6ADFC-758C-E011-8DFB-0017A4770004.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/7456B9AC-838C-E011-B2EB-0017A477102C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/72FC3403-728C-E011-9429-0017A4770800.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/6CC5571C-6E8C-E011-86D1-0017A4771028.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/6866FFA3-798C-E011-BCC0-0017A4770004.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/66F00983-718C-E011-A991-0017A4771030.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/64C7E494-698C-E011-ACBF-0017A4770800.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/5C854154-798C-E011-A2EF-0017A4770814.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/5C1A3A50-728C-E011-9A55-0017A4771030.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/58F019AC-6E8C-E011-B69B-0017A4770814.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/56AA513A-788C-E011-A365-78E7D164BFC8.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/54257F01-748C-E011-BFA2-0017A4771000.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/528DFB05-9C8C-E011-A458-0017A4771008.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/4EEB86F1-708C-E011-ADA4-0017A4771000.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/4E83C925-448C-E011-9466-1CC1DE1CDCAE.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/4CBD8996-768C-E011-AE02-00237DA1ED1C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/4C960404-CE8C-E011-87DE-1CC1DE047FD8.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/4C039292-6D8C-E011-815C-00237DA1CD92.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/48AB1674-778C-E011-B97E-001B78CE74FE.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/4689476A-428C-E011-8D7B-1CC1DE053050.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/4614079F-728C-E011-88B0-0017A4771018.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/44B94EEB-778C-E011-AD66-0017A4771028.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/449AFBAC-6E8C-E011-8132-0017A4770800.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/40534ADB-698C-E011-B7C6-0017A4770004.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/3E9597F6-398C-E011-942E-001E0B5F27BC.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/3C42FE19-3C8C-E011-B496-001B78E3E38E.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/3A70494E-7C8C-E011-8126-78E7D164BFC8.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/3A69E9B0-678C-E011-940B-1CC1DE040FA0.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/36DA7AF9-758C-E011-A9A2-0017A4770814.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/366A2A50-858C-E011-A3CC-00237DA2F1DC.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/36642C83-6A8C-E011-A367-0017A4770414.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/34DE084E-788C-E011-BDC9-0017A4770004.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/3028CD69-758C-E011-AD2A-0017A4770C28.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/3022E848-6D8C-E011-B557-78E7D164BFC8.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/2E63B999-668C-E011-9294-0017A4770018.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/28C727E6-7A8C-E011-AD45-00237DA1ED1C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/28172FD6-6F8C-E011-B093-001E0B5F5898.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/26ECEBDE-6D8C-E011-BFEE-0017A4770434.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/26186019-398C-E011-BF15-1CC1DE04FF48.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/1ED81597-6B8C-E011-800D-0017A4770004.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/1AE47885-718C-E011-8035-0017A4771000.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/1834456E-738C-E011-9912-0025B3E020D0.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/180B8B00-748C-E011-AE92-00237DA1ED1C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/16866839-718C-E011-A298-00237DA1A66C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/146377A1-388C-E011-8787-1CC1DE1D208E.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/0E718ED9-728C-E011-8F4E-00237DA1A66C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/0E3DC93C-8B8C-E011-9AC4-00237DA2F1DC.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/0C1060C2-398C-E011-B57E-00237DA12CE8.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/0ACCBB01-808C-E011-88CA-0017A477102C.root',
'/store/mc/Summer11/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S4_START42_V11-v1/0000/0A998C9C-388C-E011-B2C6-00237DA13F9E.root'
    ) )
)
