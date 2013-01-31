import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/053/6E9C7467-40B0-E011-8BED-003048F024FE.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/067/329CA668-62B0-E011-B55F-003048D2BDD8.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/070/E20D2A8E-65B0-E011-B24D-BCAEC518FF63.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/071/A8BC4D2D-6FB0-E011-B941-003048D37514.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/181/B0D86651-BDB0-E011-9CD7-BCAEC518FF6B.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/202/AC21BEE9-DDB0-E011-B330-BCAEC518FF69.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/212/2C4E0853-00B1-E011-BFE9-BCAEC5329710.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/249/9E659D82-CAB1-E011-9AED-BCAEC53296F9.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/255/64EC3285-E0B1-E011-B90B-003048D2C108.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/286/EA1B79CB-07B2-E011-BF1C-003048F1C58C.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/292/0EF9840D-13B2-E011-884F-003048F1C58C.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/298/5870B79A-1EB2-E011-B815-003048F118C4.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/303/189E0E7F-13B2-E011-A3E0-003048F01E88.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/304/908CC358-23B2-E011-A444-003048F118AC.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/307/F8E018CA-18B2-E011-A0BB-BCAEC518FF63.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/348/66B9D1B3-7FB2-E011-8863-003048F1BF68.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/354/EA90C0C1-86B2-E011-BECE-BCAEC5329707.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/376/6AEB0B78-B9B2-E011-AA2E-BCAEC5329707.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/378/C4773015-85B2-E011-AA79-BCAEC518FF91.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/380/34D6A36A-84B2-E011-9D9A-BCAEC518FF76.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/382/6EB540A6-C4B2-E011-8A53-BCAEC5329718.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/382/B2AD6531-9BB3-E011-8E21-0030486733D8.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/396/A28E6BF0-97B2-E011-9C8C-001D09F24600.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/397/0AD34D47-EEB2-E011-96FA-BCAEC5329707.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/397/A469CFEF-CFB2-E011-ACD3-0030487C8E00.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/406/5E3BEDFD-85B3-E011-B468-0030487C6090.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/452/C88B0040-3AB3-E011-938A-BCAEC5364C42.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/497/B0C200EA-0CB3-E011-8886-BCAEC53296FE.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/527/1EBE4B2B-8AB3-E011-8333-BCAEC518FF4A.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/713/3CF16DFF-0FB4-E011-94CD-003048D37514.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/718/9CF48D81-14B4-E011-883C-BCAEC518FF76.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/722/DE46516D-36B8-E011-86CE-BCAEC53296F4.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/743/8E7967AB-53B4-E011-89A2-BCAEC53296FF.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/759/78D6269B-A8B4-E011-9070-003048D37514.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/759/E0220280-C5B4-E011-82BD-0030487CD7EE.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/826/1E027890-E5B4-E011-BE9B-0030487CD184.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/826/DEC5D77C-15B5-E011-AAD6-001D09F28EA3.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/842/3A8FA7C5-FFB4-E011-BCEF-0030487C8CB8.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/842/947FCB84-1DB5-E011-888E-001D09F2437B.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/854/14DB232E-1DB5-E011-869A-003048F024E0.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/854/50BB34A8-34B5-E011-B672-001D09F34488.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/876/8E4F9E7E-36B5-E011-93C4-BCAEC5329705.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/896/029CFB42-54B5-E011-9F85-BCAEC5329732.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/899/DC480AA9-58B5-E011-BAE0-BCAEC5329730.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/901/C459875F-5EB5-E011-A123-003048F1C58C.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/907/D078D1D0-31B5-E011-8A98-001D09F2924F.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/909/4C868E80-45B5-E011-B331-BCAEC5329708.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/170/975/CABB1E6E-9BB5-E011-9B7F-BCAEC518FF62.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/050/2CB38166-5EB6-E011-ABA2-003048F110BE.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/050/62F241E4-55B6-E011-906C-BCAEC5329731.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/050/DCB2B0D9-84B6-E011-BEB7-003048F11942.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/050/FC55FD63-5EB6-E011-B2CB-BCAEC532971E.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/091/9283BA0E-74B6-E011-815B-003048F11C28.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/098/4C0EE171-4BB6-E011-8CD6-001D09F2932B.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/102/EAB3E1F0-78B6-E011-862B-003048D37456.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/106/F21E5642-8BB6-E011-8ACB-003048D2BDD8.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/116/DE45B730-47B6-E011-849E-BCAEC5329716.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/117/40FCF7AE-0EB8-E011-8CF6-001D09F23D1D.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/156/1C0D33E6-BEB7-E011-951B-BCAEC518FF62.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/156/900B0E90-2BB8-E011-AD47-001D09F295A1.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/156/9448CD72-F3B7-E011-9F24-0030487CF41E.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/156/A0597757-C5B7-E011-B025-003048F117B6.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/178/2862C862-BFB7-E011-B0E8-BCAEC5329717.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/178/3E164562-BFB7-E011-BEAF-BCAEC518FF63.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/178/64E6F254-DDB7-E011-A392-0030486780AC.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/178/D868F255-22B8-E011-A961-BCAEC5329703.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/182/74438158-C5B7-E011-AB93-001D09F24024.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/191/08F4F6B2-C4B7-E011-8FDD-001D09F2924F.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/219/9C973D6A-16B8-E011-8558-001D09F2841C.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/246/0A00B237-CCB7-E011-9189-001D09F29114.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/274/B64CEE04-9CB8-E011-A07C-BCAEC5329701.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/282/62555ACF-83B8-E011-A586-003048F1183E.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/282/882603D9-E9B7-E011-BA10-001D09F24493.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/315/724C868C-93B8-E011-B1EB-BCAEC518FF5F.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/315/EAF6978D-F5B7-E011-BA6E-001D09F251B8.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/348/CC5DAC56-C5B7-E011-B618-BCAEC518FF6B.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/369/804514A0-13B8-E011-81E6-0030486733D8.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/446/6A46E067-94B8-E011-91D0-003048F024FA.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/446/70F49C7C-5FB8-E011-A2C3-BCAEC5329725.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/446/72D7491A-49B8-E011-A02A-003048D373AE.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/446/9241BAF5-54B8-E011-8BBE-003048D2BE12.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/446/9AFC43DB-59B8-E011-931F-001D09F25267.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/446/AC41EBCA-57B8-E011-8037-003048678098.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/484/120DD77B-84B8-E011-8698-003048CFB40C.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/484/8EA14CDF-77B8-E011-B4FD-0019B9F581C9.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/484/9E4C8E18-6FB8-E011-BC62-003048F1C836.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/484/EA481513-B9B8-E011-BD85-BCAEC5329730.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/504/942C3CC4-49B8-E011-BB62-003048D2C0F0.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/521/70319ED2-61B8-E011-95A7-BCAEC53296F8.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/548/42E46B90-83B8-E011-BC10-BCAEC53296F6.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/577/22BA8746-9CB8-E011-8ED3-003048F117EA.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/578/0293C17A-06B9-E011-B92D-003048F11942.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/578/18DE77BC-FDB8-E011-9EFF-001D09F29169.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/578/36A2AA2A-02B9-E011-96AD-BCAEC518FF56.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/578/54E002E6-23B9-E011-9DD7-003048F117EC.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/578/BA19A379-0AB9-E011-95A2-485B3977172C.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/812/58E5E6C8-DFB9-E011-8545-003048F024C2.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/812/BE50D8AB-E4B9-E011-8DCA-003048F11C5C.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/812/DC6CCB53-28BA-E011-B2E2-E0CB4E553673.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/812/F67EE932-E1B9-E011-ACF7-003048F118D2.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/866/3E6C1E06-EFB9-E011-994B-003048D375AA.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/875/444124EE-1BBA-E011-A334-BCAEC518FF62.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/876/20E4643A-BFBA-E011-B5CD-0030487CD178.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/876/3EE16A60-73BA-E011-839C-0030487C8CB6.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/876/76E5F86A-71BA-E011-B1B3-0030487A3232.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/876/C4650554-6CBA-E011-99D5-001D09F23944.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/876/D408458A-75BA-E011-BE95-0030487CD812.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/879/8E61EF89-7CBA-E011-8C06-003048D37538.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/880/38CEA021-86BA-E011-96FD-001D09F2305C.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/890/3A09C9FD-85BA-E011-B383-BCAEC518FF4A.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/895/5C856D0A-91BA-E011-A047-001D09F297EF.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/897/6C97B12E-89BA-E011-84E6-003048F117EC.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/897/DAF9BCFD-92BA-E011-B18F-003048F118C4.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/897/FAB09956-B3BA-E011-983B-001D09F2512C.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/921/8C213B63-0CBB-E011-8B6C-BCAEC5329701.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/926/3072C1CF-E8BA-E011-81AA-BCAEC53296FC.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/926/48F4EDCC-1FBB-E011-8342-BCAEC53296F4.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/945/BEE7E148-ABBA-E011-92B5-001D09F250AF.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/171/949/9ADF7272-B3BA-E011-83E6-0030487CBD0A.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/014/5A048ADE-DBBB-E011-B33D-001D09F2424A.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/014/7C3610E7-67BB-E011-806B-0030486780EC.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/014/E0BE0A5C-70BB-E011-B635-BCAEC518FF44.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/024/9EC02DEC-98BB-E011-ADA2-003048F024F6.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/033/18747D37-94BB-E011-814A-003048F118AA.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/033/24BC9C13-90BB-E011-A65B-003048D373AE.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/033/3202625C-88BB-E011-8B90-0030487CD6D2.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/033/8269F359-88BB-E011-B7B3-0030487CD6D8.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/033/C0455D32-B3BB-E011-9175-003048F1C420.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/111/5CD34CC7-78BB-E011-B8F6-003048D2C092.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/163/0C9CF84F-20BC-E011-868D-003048F1110E.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/163/245F934A-0FBC-E011-833B-E0CB4E4408C4.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/163/7483A14D-20BC-E011-9582-003048F11C28.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/163/7EE9154B-6BBC-E011-BCAB-003048F118C4.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/163/82A0C0BD-0BBC-E011-BF72-003048F110BE.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/163/D2B74288-07BC-E011-ABCE-003048F1182E.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/163/EE5F964A-0FBC-E011-959A-BCAEC5329732.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/208/02D4629A-92BC-E011-8CE3-001D09F23944.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/208/E0CA5312-FFBC-E011-A929-BCAEC532970B.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/251/52A2F662-8BBC-E011-992E-003048F024FA.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/252/C6DF9980-5EBD-E011-A8D5-003048F01E88.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/254/64128418-6BBD-E011-8219-BCAEC532972C.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/255/8470466C-5EBD-E011-9A47-003048D37580.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/268/06DCA04A-24BD-E011-8247-BCAEC518FF89.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/268/5029D26C-D9BD-E011-BEFA-E0CB4E553673.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/276/646E22AA-D0BC-E011-B74B-E0CB4E4408D2.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/286/047C4616-51BD-E011-B67B-BCAEC518FF8D.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/286/7A6FCE49-BDBD-E011-BB1D-003048F1110E.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/383/D0C2CD47-1BBE-E011-A449-003048F117B4.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/384/84FEE3A6-24BE-E011-9F7F-003048F1183E.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/389/361D4801-A9BE-E011-85C9-003048F01E88.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/389/6A867801-A9BE-E011-8E19-003048F1C836.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/389/6CB17850-9BBE-E011-BE32-BCAEC53296FE.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/389/B8E7921D-F0BE-E011-8D09-BCAEC532972C.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/389/BA20A58A-9FBE-E011-9F5F-BCAEC5329716.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/399/6CE67F02-34BF-E011-8F83-E0CB4E4408E3.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/399/C2A370B9-CEBE-E011-A94B-001D09F242EF.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/400/266B49EA-FDBE-E011-9D21-BCAEC5329730.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/400/423F2A2D-F9BE-E011-B9B9-BCAEC518FF89.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/400/563F88EE-2EBF-E011-8994-001D09F25041.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/400/68F48DE9-FDBE-E011-A81B-BCAEC53296FE.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/400/B83DFA29-F9BE-E011-9757-BCAEC5329713.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/400/C0E23F28-F9BE-E011-8402-BCAEC53296F8.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/401/AA9A6AA9-1EBF-E011-B27B-003048D2BB58.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/411/0EB79EBC-42BF-E011-88C6-BCAEC53296FD.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/411/50C2E274-2AC0-E011-B38D-001D09F251B8.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/411/7A524DCA-33BF-E011-9179-BCAEC518FF80.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/461/EAA49A6F-0BBF-E011-8443-001D09F26509.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/463/4EAABFEF-10BF-E011-B54C-0030487CD6B4.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/467/40FB37D1-1EBF-E011-A2D5-001D09F25267.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/468/38CEFB51-1EBF-E011-A211-0030487CD13A.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/469/7A4F2F71-21BF-E011-805F-BCAEC53296F3.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/473/CE77AF89-3EBF-E011-AD48-E0CB4E55365C.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/475/D6D95BFB-5BBF-E011-8E26-BCAEC518FF7C.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/476/7A900C22-5CBF-E011-A33A-001D09F24D8A.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/478/1AC41B04-74BF-E011-9894-0030486780E6.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/485/5CAF3C3D-A6BF-E011-ADCB-BCAEC5364C42.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/485/5ED5D01D-A0BF-E011-AD5C-E0CB4E4408E7.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/485/708E7E2A-38C0-E011-A4AC-003048D2C108.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/485/94B24940-A6BF-E011-808B-003048D3750A.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/485/985AA1EC-AABF-E011-9180-BCAEC518FF52.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/485/D2F3D63D-A6BF-E011-B867-003048F0258C.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/488/FCAAA63C-ABBF-E011-971E-BCAEC5329729.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/495/447748BA-B8BF-E011-9925-003048D37580.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/497/7CDACD23-ACBF-E011-AFA5-003048D375AA.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/507/0C9D5000-B9BF-E011-B1F7-BCAEC53296FD.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/516/D01139E5-B2BF-E011-834A-003048D2BCA2.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/549/2C8A0BED-9FBF-E011-9647-003048F118E0.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/550/AA8F328D-A5BF-E011-841F-BCAEC53296FD.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/561/34B0AC1B-ACBF-E011-97D2-BCAEC518FF76.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/564/3240D247-C7BF-E011-8EE3-BCAEC5364C6C.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/567/AAC559D8-B1BF-E011-BFEF-BCAEC53296F6.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/576/8C81070A-B2BF-E011-944C-003048F11942.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/579/8CA12BDD-B8BF-E011-9016-BCAEC518FF63.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/584/86BAB440-B9BF-E011-B246-003048D2BC30.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/588/66DA2289-F8BF-E011-B6BE-003048F1C420.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/593/BE8C1964-BDBF-E011-A33E-003048F117B6.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/597/06C02AB5-E4BF-E011-82B1-BCAEC518FF7C.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/598/F4062ABD-C1BF-E011-8282-BCAEC5329732.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/604/12EC2B90-EEBF-E011-8BA3-001D09F295FB.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/606/349968E8-11C0-E011-8FDB-E0CB4E55365C.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/611/46C081E6-07C0-E011-B305-001D09F2546F.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/615/02F2B3C5-08C0-E011-BF4C-BCAEC5364C42.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/617/70732D8B-0CC0-E011-B2EA-E0CB4E4408D5.root',
       '/store/data/Run2011A/MET/AOD/PromptReco-v5/000/172/619/365D81B4-11C0-E011-B11A-BCAEC518FF50.root' ] );


secFiles.extend( [
               ] )
