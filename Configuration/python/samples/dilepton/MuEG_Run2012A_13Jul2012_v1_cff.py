import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/F6FC96E7-63D8-E111-BC6A-20CF3056170A.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/F6CCBF9E-48DA-E111-99C2-001EC9D8D4A3.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/F67A9D02-FCD7-E111-ACB9-20CF3027A5B6.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/F4DF46A2-BCD9-E111-A190-0030487C73D4.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/F430720A-3ED8-E111-ADA3-0030487CDAC6.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/FEF59314-34D8-E111-8DF9-E0CB4E19F972.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/FA8D0C50-A5D8-E111-A7F2-001EC9D825E5.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/F2AD4CF9-A9D7-E111-8958-00259073E322.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/F0CCB363-33D8-E111-B6BB-20CF3027A626.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/EAFD6AF0-FFD8-E111-AC1F-90E6BA442F07.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/EAC7BDF2-B2D9-E111-8A52-001EC9D26C2C.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/E8D6A130-A7D9-E111-BA6E-20CF3027A62F.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/E864D1C5-77D9-E111-8A12-20CF3027A608.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/E6E14328-9CD8-E111-8847-20CF3027A631.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/E68CE64E-B5D7-E111-81F1-90E6BA0D09E8.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/E466B138-D8D7-E111-ABE2-00259073E374.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/E4551B1A-B7D7-E111-A17C-002618FDA1AA.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/E25D6231-50DA-E111-90F9-90E6BAE8CC0C.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/E257CA28-35D8-E111-B3D4-90E6BA19A23E.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/DEC1A4F1-90D7-E111-B936-00259073E49A.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/DE4C2D99-FCD8-E111-B59A-0030487C6A90.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/DE41CE91-64D8-E111-B4B5-E0CB4E4408E6.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/DCFF73EF-40D8-E111-AC8E-00261834B5D2.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/DAA2697F-4ADA-E111-BED3-90E6BA442EF6.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/DA9E071A-A4D8-E111-864C-00259073E3D6.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/DA8BA834-54DA-E111-9C50-00261834B5A0.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/DA58E455-B7D9-E111-AC67-E0CB4E55367B.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/D8E40140-63D8-E111-83F5-90E6BA19A240.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/D847F26E-9AD8-E111-9B56-20CF3027A5BC.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/D685734D-52DA-E111-95FD-00259073E504.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/D61E6DD7-A9D9-E111-ACB1-00259073E32A.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/D05995CD-6BD8-E111-885B-90E6BA442F11.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/CE523299-C6D7-E111-9604-E0CB4E1A1145.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/CCCFF500-BAD9-E111-B93A-20CF305B051B.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/CC938297-6AD8-E111-B1F1-001E4F236DC1.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/CAE1EE10-66D8-E111-AFC7-E0CB4E29C513.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/CA8C853F-58DA-E111-BEEF-485B39800BD3.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/CA80C528-D3D8-E111-B942-90E6BA0D09B6.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/CA076E1D-50D8-E111-B781-E0CB4E19F97C.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/C89AF0F0-DCD7-E111-B8FC-20CF3027A584.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/C68C4834-68DA-E111-8D2C-002618FDA18F.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/C640BDAD-D1D8-E111-8BDD-00259073E500.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/C4F48B9E-56D8-E111-9EEC-002590747E14.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/C4CF7B1C-A4D8-E111-A6E1-00259074AE8C.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/C2B8ECA5-DBD8-E111-97E5-20CF3056171C.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/C2B7BF65-3BD8-E111-8C6E-00261834B594.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/C0B93B06-AFD9-E111-8B49-90E6BA0D09B3.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/BE5D51FE-37D8-E111-BFE5-20CF3027A5EC.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/BA8F78A3-FCD7-E111-BC45-E0CB4E55366B.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/BA2863FD-69D8-E111-8BD4-002590747DF0.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/B8A20A2D-8AD7-E111-8D8C-20CF3027A608.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/B87F561D-5ADA-E111-93C3-00259073E380.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/B6E0B8A9-71D9-E111-B3BE-E0CB4E19F9A1.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/B6D4B11C-FFD7-E111-803B-00259073E4F6.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/B63C6564-41D8-E111-B503-E0CB4E29C4B6.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/B4ABA1F4-ADD7-E111-B727-E0CB4E1A1180.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/B2B9C9BF-3FD8-E111-BAE0-20CF3027A637.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/B27E98BC-36D8-E111-8685-E0CB4E29602B.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/AE989677-6BD9-E111-ADCF-001EC9D28298.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/AE24B5C7-D1D7-E111-9534-00259073E408.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/AC154C31-4BD8-E111-9787-00261834B5C1.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/A8676F31-50DA-E111-B245-001EC9D80A9D.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/A85C678F-A6D9-E111-9A84-20CF3019DEE9.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/A81DCDA5-FCD7-E111-B75C-E0CB4E1A114C.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/A41D8AC8-8AD7-E111-A629-E0CB4EA0A906.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/A2596E2C-3FD8-E111-8454-001EC9D81D4C.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/A254DB7D-9CDA-E111-86F8-001EC9D8D997.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/A0D6B589-25D7-E111-9E73-E0CB4E29C512.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/9E854F0B-55DA-E111-91C8-E0CB4E29C4D9.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/9E2E982D-98D8-E111-8878-20CF3027A626.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/9CC0BDBE-9CD8-E111-9AFD-E0CB4E29C4BE.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/9CB0F8D4-D8D8-E111-A37B-001EC9D278EC.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/9C64E315-A4D8-E111-B73B-00261834B561.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/9C1922B3-A4D8-E111-ADA9-E0CB4E29C4B8.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/9842912F-A7D9-E111-9588-E0CB4E553642.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/96F288F6-08D9-E111-BE9F-00259074AEAC.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/94FB976D-9AD8-E111-9E44-E0CB4E1A116A.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/94BC4C2C-C1D7-E111-9BEA-485B39800BA4.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/920878DE-CBD7-E111-B4B3-485B39800C1A.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/903749BC-67D8-E111-A6B6-00259074AE82.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/8CF911CF-2ED7-E111-8D13-20CF3027A611.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/8A9058A6-61D8-E111-AEBB-E0CB4E55366A.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/8A903C30-99D8-E111-9D30-00261834B580.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/8A87CDE9-FDD7-E111-98D9-90E6BA442F11.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/887752E8-ADD9-E111-8C95-001EC9D8D973.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/82E24643-4EDA-E111-BE6A-20CF3027A637.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/82CD4607-FBD8-E111-A506-00259073E524.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/8208259D-4CD8-E111-8FD2-00259073E532.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/7C7EBE23-35D8-E111-B872-001EC9D8314D.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/7C6CFA5A-86DA-E111-A11F-00261834B575.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/7C25FE0D-3CD8-E111-AAA2-20CF3027A57B.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/7C168773-B0D9-E111-AFE1-20CF3027A608.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/7AA9EEF8-A6D8-E111-A8D6-E0CB4E55363D.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/7A2DF4B7-36D8-E111-8B9C-20CF3027A574.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/782C672E-6ED8-E111-8338-20CF3019DEF7.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/74A9DC53-88D7-E111-89AE-E0CB4E55366E.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/72B18FEA-88D7-E111-B117-00259073E324.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/728A8F25-9CD8-E111-BBFA-90E6BA19A243.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/704AF9DC-C7D7-E111-B852-00259073E398.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/703A5F30-46D8-E111-B0AC-E0CB4E29C50F.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/6E30F754-68D8-E111-9C3F-20CF305B0534.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/6CC91414-A4D8-E111-8BCB-20CF30561701.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/6C7A87C0-93D7-E111-972D-001EC9F628C2.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/6C2FF64B-A2D8-E111-B132-00261834B557.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/6C0B832D-99D8-E111-B95B-90E6BA19A245.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/6ADCEC48-04D8-E111-AE99-00259074AE38.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/6A6A0C6F-4CDA-E111-BA39-001EC9D28298.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/66788EB6-8FD7-E111-8636-E0CB4E5536EF.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/64C3BD4F-CED7-E111-B475-485B39897219.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/62D42E36-51DA-E111-BC80-90E6BA19A212.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/62CECEE5-63D8-E111-949B-E0CB4E29C4CF.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/627DE749-64D9-E111-BA9C-485B39800C17.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/624C56A3-8DD7-E111-8FE5-00259073E336.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/5ED224A7-FCD7-E111-BCF5-001EC9D7FF4F.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/5AEF095F-D3D7-E111-9CD5-00261834B524.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/562DAE5F-9ED8-E111-B4A5-E0CB4E4408EF.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/54ED9298-AAD7-E111-B4EF-001EC9D7F1FF.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/52B205B5-66D8-E111-BA99-20CF3056170A.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/508C4087-A5D7-E111-A7DE-E0CB4E29C50E.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/4CED2C35-51DA-E111-8769-90E6BA19A210.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/4AEBF485-D0D7-E111-9ECF-20CF3027A5EC.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/4A61B1F1-8CD7-E111-A5B2-E0CB4E19F975.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/481CD8B2-A4D8-E111-B729-E0CB4EA0A91E.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/4801325E-A1D8-E111-928D-20CF3027A59B.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/46D394B2-D4D7-E111-87FB-E0CB4E1A1187.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/464BDE3A-60DA-E111-ACF8-001EC9D282AC.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/44C5721D-A0D8-E111-AABD-00259073E3E6.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/449A0240-53DA-E111-9696-E0CB4E1A1163.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/409CAF15-66D8-E111-A1EF-002590747DC8.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/409090B3-9DD8-E111-B1E1-485B39800BB9.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/40122960-87D7-E111-BE61-20CF3027A5B7.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/3E2D2D66-3BD8-E111-8BBF-E0CB4E1A117B.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/3AD1C90F-32D8-E111-8FC4-485B39800C00.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/3A354127-35D8-E111-BE18-20CF305B0585.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/38CC9415-A4D8-E111-8B1B-90E6BA19A24C.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/383E5FF2-5BDA-E111-90A0-00259073E482.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/36E99072-4CDA-E111-AFBB-00259073E3CE.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/364DE54C-52D8-E111-9258-00261834B51B.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/3431BAFF-A6D8-E111-8190-001EC9D7F20F.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/340C9D4A-4ED8-E111-B0F6-20CF305B058C.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/323311D6-98D7-E111-A767-485B39800B94.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/30B261AF-3CD8-E111-925F-E0CB4E29C50A.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/2ECDF648-40D8-E111-A8BC-00259073E41E.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/2E3494C8-2FD8-E111-BBC7-E0CB4E55366E.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/2E1FAC35-C8D9-E111-BBBF-20CF3027A5E9.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/2C483A41-63D8-E111-B02C-90E6BA19A210.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/2C2A0FBC-36D8-E111-A705-E0CB4E4408DF.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/2A004FE8-B3D9-E111-8A26-001EC9D8D07D.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/2845C128-5EDA-E111-97D7-E0CB4E553643.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/240C2C77-34D8-E111-A9EF-20CF300E9EB6.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/22716F01-57DA-E111-A04F-00259073E3D2.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/224C5DF3-FDD7-E111-86A3-0030487CDB24.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/20665DB3-46DA-E111-A1AD-002590747DEC.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/20199D9E-A5D9-E111-AB08-00259073E374.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/200A29FF-69D8-E111-96F6-001EC9D8BDE7.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/1EED1284-97D8-E111-BE01-E0CB4E29C50F.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/1C2620FC-56DA-E111-B13F-001EC9D8B14D.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/1AFF556C-3BD8-E111-95BA-001EC9D29E23.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/1872B3D5-8BD7-E111-8D3C-20CF3027A5B0.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/18615659-ABD9-E111-88A8-20CF305B056F.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/168E3FD2-8ED7-E111-A8DB-20CF305616E0.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/1676DFA0-64D8-E111-8A39-20CF3027A596.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/12E0D923-A9D8-E111-A91E-00259074AE8C.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/10F3BFD5-92D7-E111-9C6B-485B39800B84.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/10EA8C25-9CD8-E111-8F29-485B39800BB9.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/10DA21CC-B5D9-E111-90BC-E0CB4E29C4B6.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/103A993F-ADD8-E111-8908-20CF305B0524.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/1005D0F0-40D8-E111-AAFF-20CF3027A61B.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/0EC7FE65-A5D8-E111-834E-20CF3027A564.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/0EC68627-2CD7-E111-8291-20CF3027A5CE.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/0E5A9405-C3D9-E111-AD6C-00259073E45E.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/0C8198E2-0DD9-E111-807A-E0CB4E19F970.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/0C46B727-A8D9-E111-9319-E0CB4E19F9BC.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/0C420C9C-BAD9-E111-9F78-E0CB4E29C51B.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/0C17984E-ACD9-E111-97EF-001EC9D53243.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/0A47AE1F-BFD9-E111-8AB4-20CF3019DF0C.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/067DA9E6-6CD8-E111-A752-001EC9D7FA28.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/065F2FF3-A2D8-E111-B772-90E6BA0D09CA.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/064F8638-51DA-E111-BA2F-00259074AE3E.root',
       '/store/data/Run2012A/MuEG/AOD/13Jul2012-v1/0000/04827A6C-9AD8-E111-8850-E0CB4EA0A906.root' ] );


secFiles.extend( [
               ] )

