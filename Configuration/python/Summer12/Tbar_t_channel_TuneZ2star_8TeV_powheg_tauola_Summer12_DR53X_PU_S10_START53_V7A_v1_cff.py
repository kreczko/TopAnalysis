import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/00823877-1EEA-E111-811B-0026189438AD.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/008A8085-1AEA-E111-BD06-003048678B70.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/04334822-22EA-E111-A1A9-0018F3D09642.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/04BAE4AD-22EA-E111-997C-003048678B84.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/0661FC37-0FEA-E111-8594-001A92971BA0.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/080C9371-3CEA-E111-B1FE-002354EF3BDA.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/0CC6A537-50EA-E111-9168-0018F3D09614.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/0EB26C42-1DEA-E111-853E-00248C65A3EC.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/10079B83-1AEA-E111-9D07-003048D15E24.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/101378C3-3CEA-E111-A421-0018F3D09614.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/1014BEA3-1FEA-E111-B85C-00261894384F.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/10827A2C-30EA-E111-88F0-001A928116C2.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/1691E496-23EA-E111-A6D3-0026189437F8.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/183BB8E9-23EA-E111-9CFE-0030486790BE.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/1893CA7B-36EA-E111-B046-0018F3D095FC.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/02EC82AE-3AEA-E111-8654-0018F3D095FC.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/083D0965-2EEA-E111-9ACF-001A928116B2.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/0C337DAB-3DEA-E111-AF3C-0018F3D095FC.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/121A1284-1AEA-E111-8A50-0026189437F5.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/18EECF58-1CEA-E111-A6EB-002618943894.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/1EC94922-25EA-E111-A50D-00261894389E.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/1CA5D444-20EA-E111-BCA9-003048FFD76E.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/1CAA6CC7-1EEA-E111-8C39-0026189438FD.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/20ACEF13-1CEA-E111-A955-002618943945.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/1E18D55C-1FEA-E111-8A69-00304867915A.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/1EB9CEE0-23EA-E111-8491-002354EF3BDE.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/20081BDC-49EA-E111-AF53-0026189438C9.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/2E0A705B-1FEA-E111-9D50-0030486792AC.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/2068A6B8-22EA-E111-8119-0018F3D09628.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/343FC8EC-31EA-E111-A920-00304867904E.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/363033FD-18EA-E111-9C33-002618943907.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/36F05361-1FEA-E111-B0B6-003048FFD728.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/247BD779-1EEA-E111-9B27-003048678A78.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/249B100D-23EA-E111-AB25-001BFCDBD182.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/446D6445-1DEA-E111-AB97-003048FFCB8C.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/447B7146-33EA-E111-88EF-001A928116B0.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/28EAE095-35EA-E111-9A5A-0018F3D09676.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/44C40E09-1CEA-E111-990A-003048678B18.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/44EE31AB-1DEA-E111-A33E-0018F3D09660.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/489CB4B6-46EA-E111-A6E6-003048FFCC0A.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/4CC89F69-19EA-E111-A764-003048678B70.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/2E40E93F-2CEA-E111-AD1F-003048678C9A.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/3C74AAB1-25EA-E111-BE9A-002618FDA207.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/50396E42-20EA-E111-BBCD-0030486792AC.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/506CC37A-1EEA-E111-A0D3-002618943914.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/50E9306F-21EA-E111-8FE0-003048678B7C.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/547FF16F-1BEA-E111-ADFC-0026189437ED.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/2644A440-1AEA-E111-A011-003048678CA2.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/2E9FFBB5-1CEA-E111-9E1F-001BFCDBD182.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/3697456D-1BEA-E111-B8FD-0026189438D2.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/386D8AF8-40EA-E111-9E6C-0018F3D09614.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/3AD34F75-3CEA-E111-96D3-0018F3D095FC.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/3E6B2EDF-2FEA-E111-A2CC-003048FFD736.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/409F1C01-26EA-E111-910B-002618943896.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/46C6BADA-21EA-E111-BDEB-0018F3D096C0.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/48692B4D-26EA-E111-8F77-003048FFCBB0.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/72BEDF3E-1AEA-E111-8428-003048678D6C.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/4CE6D058-1CEA-E111-B016-003048678F8C.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/4C809BA4-20EA-E111-895E-0018F3D0963C.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/4CA7CC6D-18EA-E111-9073-0026189438D5.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/54455EFC-29EA-E111-9822-0018F3D096A2.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/566A8912-26EA-E111-BB21-00261894389E.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5AF127AC-1CEA-E111-BFD3-001A92971B38.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5C669B12-26EA-E111-86B3-00261894389E.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5CA9DE83-1AEA-E111-AFE1-002618FDA237.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5E02E12B-42EA-E111-9CE7-0018F3D09700.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5E08DF4F-38EA-E111-8B1B-0026189438A0.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/662A6BEA-19EA-E111-8965-003048678FB2.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/6A983F16-25EA-E111-BECA-003048FFD71A.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/72ABB806-23EA-E111-9681-0030486790BE.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/74B51549-1DEA-E111-9E89-003048FFCB74.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/7852AFCA-24EA-E111-9DCC-00304867C1B0.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/7A2ED109-2CEA-E111-AC7A-00261894389E.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/0AD0C544-2FEA-E111-A6E1-003048678BB2.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/72D82112-31EA-E111-B6F9-003048FFCC1E.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/7CA78016-22EA-E111-8C5D-003048679076.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/72EDEC24-25EA-E111-9D6E-0018F3D096F8.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/7E038A0D-28EA-E111-A04F-0026189438AC.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/7E58A80D-4BEA-E111-AEB8-003048D3FC94.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/78F41773-21EA-E111-8C8E-0026189438FA.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/80288767-18EA-E111-A05B-0026189438F6.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/804307CF-24EA-E111-A8AC-003048FFCB74.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/808371B0-34EA-E111-BEEB-003048FFD796.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/80A57AB4-28EA-E111-AE31-0018F3D09612.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/7A571472-1BEA-E111-B4D6-003048678BB8.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/7C5C8FB6-22EA-E111-8203-001A92971B38.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/84D0A573-1EEA-E111-8B76-003048678B8E.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/7CF9D62C-27EA-E111-B463-0026189438FF.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/88BFF08B-3BEA-E111-8BAC-002354EF3BDA.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/7EDF2D9E-1CEA-E111-8D3E-00304867C1BC.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/82E449E0-23EA-E111-96FF-00304867C034.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/84CDD6C6-24EA-E111-9384-002618943849.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/8E531039-2AEA-E111-8F20-00261894389E.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/84EB3B0C-43EA-E111-95FB-002618943940.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/8A7110C4-39EA-E111-8299-0018F3D095FC.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/8AE89C80-33EA-E111-8FA8-001A92971B8C.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/92715910-2EEA-E111-9F4B-00304867926C.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/946E9F6A-1BEA-E111-81ED-003048FFD76E.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/94D5B8E1-23EA-E111-8FB7-00261894387E.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/960CD77E-1BEA-E111-AA34-0018F3D096C0.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/8E3C03DA-20EA-E111-9066-003048678BAA.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/9AD99B42-26EA-E111-B007-0026189438D6.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/A06CAB27-25EA-E111-86F6-0018F3D09612.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/8EF33F20-37EA-E111-A1FD-001A92811716.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/A26F00DE-14EA-E111-9CEA-0018F3D09616.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/90CA3628-2DEA-E111-89BE-00304867926C.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/92079A66-3DEA-E111-8C13-0018F3D09614.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/9A9C835C-34EA-E111-A44A-003048FFD7A2.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/AAA6E643-20EA-E111-A7D8-003048FFD728.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/A2120C99-23EA-E111-B5E3-003048678B84.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/AEAF68AD-40EA-E111-A109-0018F3D09608.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/A42F8E75-1EEA-E111-B413-002618943849.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/A83492E5-19EA-E111-BA20-0026189438DD.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/A87FE536-2AEA-E111-BBC1-001A92810AE4.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B04EA833-39EA-E111-B23D-001A9281172A.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B07EAAC4-39EA-E111-A763-001BFCDBD1BA.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/AE4DB6FD-18EA-E111-81D4-0030486792BA.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B21040AF-20EA-E111-A187-0018F3D09642.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B29CAFEA-3EEA-E111-A020-001A9281172C.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B2B89854-20EA-E111-B2DB-0018F3D0961A.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/AEC60744-44EA-E111-A79F-0018F3C3E3A6.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B440DD8D-1DEA-E111-A9F1-002618943944.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/AECC4991-1DEA-E111-BDAC-00261894390A.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B032717E-1EEA-E111-AB67-003048FFCB74.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B6EECD47-3BEA-E111-82F5-001A9281172A.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B0C8FC3A-3BEA-E111-B443-003048678B92.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B8B9B071-39EA-E111-A3B9-003048FFCC2C.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B4136A19-37EA-E111-992B-003048FFD756.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B8F038C9-27EA-E111-9FB4-003048FFCBB0.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/BCBBAFC6-2AEA-E111-8995-002618943974.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/BEAE5B5F-32EA-E111-B107-0018F3D09676.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B4CA533B-1AEA-E111-BB33-003048FFD760.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C028550F-1CEA-E111-A2E3-0018F3D0969A.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C0423B6A-1BEA-E111-A512-00248C0BE01E.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C4E0C039-1AEA-E111-A7DD-002354EF3BE4.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B623E4AF-37EA-E111-9909-001BFCDBD1BA.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C8FF20DA-1EEA-E111-BB6D-0018F3D09628.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B6FAC2B1-25EA-E111-870A-001A92971B36.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/BE6A9BE1-2CEA-E111-8BB9-0026189438D7.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C016FB95-38EA-E111-A3DE-003048FFD770.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D0A0C8AF-3EEA-E111-8735-0018F3D09660.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D4D06547-26EA-E111-8139-0026189438F4.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C616CB54-26EA-E111-AF49-00304867C034.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D8016E95-3BEA-E111-A41A-003048FFD71A.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/DA807A57-19EA-E111-91D5-003048678D52.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/CCAC49A6-23EA-E111-B0AA-0018F3D09612.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D8319214-18EA-E111-9080-002354EF3BDE.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/E069878E-1DEA-E111-8BD8-00248C0BE01E.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/CE7D814F-5BEA-E111-A7E0-00261894395B.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/E28A1B66-1BEA-E111-A8F9-0026189438AD.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/E4F7AF75-30EA-E111-B0BD-003048679166.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/DCB4CC05-29EA-E111-BF43-001A928116F2.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/DE077ADE-20EA-E111-9E6C-00304867920A.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/E4C1B0D5-1EEA-E111-9386-001A928116FC.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/EAE056D5-53EA-E111-9484-001A928116D6.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/EE746DE3-19EA-E111-B374-00261894392F.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/EE7ADC75-21EA-E111-B651-003048678B70.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D0254297-4EEA-E111-8D5A-001BFCDBD166.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/F4355EF4-23EA-E111-8B90-00261894389E.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/F4B5AAC3-1EEA-E111-B9C0-00304867920A.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/F6D1E32C-36EA-E111-BDEB-003048FFCB6A.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/E69A8B7D-1BEA-E111-A38C-001A92810AEC.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/EAE5CD23-25EA-E111-ABA8-001A9281172C.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/F8F29F53-1CEA-E111-8E3D-003048FFCC2C.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/FC3BCCD9-17EA-E111-BFAC-0018F3D09706.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/FC7C7F68-2BEA-E111-8B50-001A92810AE4.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/FC817F09-1CEA-E111-B5C7-002618943981.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/FCB14C4F-38EA-E111-AC7F-0018F3D095FC.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/FE520727-2BEA-E111-94D3-00248C55CC3C.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/EC0A45B2-25EA-E111-9680-003048FFCB74.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/F821CCA9-1FEA-E111-8BA4-0018F3D09652.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/F83FC002-23EA-E111-BB10-00304867918E.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/F8B02A5D-2EEA-E111-86E6-003048FFD744.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/728CAED5-27EA-E111-B3FD-00261894389E.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/720406F0-29EA-E111-B42C-0018F3D095FC.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/6C889B10-19EA-E111-89A4-001A92971AA8.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/6AD396D7-21EA-E111-9D93-0030486792AC.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/6824E419-25EA-E111-A297-002618943856.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/664FF298-23EA-E111-AF37-00261894393C.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/62C6BBC2-3FEA-E111-8222-002618943920.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/6282D87E-1EEA-E111-93E7-003048FFCB74.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/6264FBAE-34EA-E111-8E2C-001A928116D0.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/60B04F01-49EA-E111-8763-003048FFD71E.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5E5CB088-20EA-E111-BD6C-002618943809.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5AF6891C-22EA-E111-B533-002618943920.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5A0FA278-3FEA-E111-862D-0018F3D09614.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/589EBF8F-32EA-E111-9E11-003048678FF4.root',
       '/store/mc/Summer12_DR53X/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/56F5F41C-4DEA-E111-BED4-001A928116F0.root' ] );


secFiles.extend( [
               ] )
