import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
    '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/FC6C5EFC-C7DD-DF11-81D3-0030487E4EFE.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/F455A7DE-29DE-DF11-91C0-0015172C0925.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/F400654D-2ADE-DF11-9DAA-E0CB4E55363A.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/F2E4F45F-E2DD-DF11-BF07-001E0B62D9AC.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/F0E7620F-C9DD-DF11-B53B-90E6BA442F07.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/EA40853B-D2DD-DF11-983E-003048678A44.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/E4ECA4DC-1ADE-DF11-BA79-001F296534E6.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/D4ADA45A-28DE-DF11-8D10-003048CAA6B0.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/D03EBFBA-D0DD-DF11-8ED3-E0CB4E55365F.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/CE714E7A-CEDD-DF11-9671-001E682F260A.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/C0BB8B06-E2DD-DF11-B3C0-00145E5523ED.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/BACD49C7-C0DD-DF11-967C-E0CB4E19F975.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/B84674DC-AFDD-DF11-AA00-00145E552252.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/B68C30D4-E9DD-DF11-8B81-00145E551D30.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/B405F525-CBDD-DF11-A648-0030487CB568.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/96F2F089-BFDD-DF11-BF02-001F2965444E.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/92C511E6-09DE-DF11-BBE5-001F2965E2B8.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/8E51B719-71DE-DF11-AD24-0015172C091C.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/8E491944-D9DD-DF11-8676-001E68A991F4.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/88535CEE-B0DD-DF11-AC57-00248C9BA59A.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/84B056DE-26DE-DF11-83E4-00145E551AF9.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/80FB25A0-5DDE-DF11-8BF6-003048CAA6B0.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/7C0144F3-26DE-DF11-905B-001E682F1D6C.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/7AC96EB3-D0DD-DF11-91D5-485B39800BDF.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/7AB2530D-B3DD-DF11-ABE3-00261834B53D.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/700AD990-DEDD-DF11-9271-00145E551CD6.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/6ED2F297-D4DD-DF11-9B51-00261834B653.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/6E66ACF5-DDDD-DF11-978A-003048D47662.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/662CB5C9-BBDD-DF11-A927-485B39800B65.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/64A32F00-C8DD-DF11-9AEA-001517357D32.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/62A876B1-DBDD-DF11-A577-485B39800B77.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/5A688CC7-C0DD-DF11-AB4D-485B39800B8D.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/522BA3EB-D4DD-DF11-B400-00D0680BF9B4.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/50285807-27DE-DF11-86C4-A4BADB3CF272.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/4E27D1B6-BBDD-DF11-98B4-00261834B569.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/4E197C03-C8DD-DF11-B876-E0CB4E55363C.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/4AB5A3EF-B7DD-DF11-869D-00151725602D.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/48823217-68DE-DF11-8963-00D0680BF9A2.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/484014EC-F3DD-DF11-9876-001D09FD0D10.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/46B10AAA-D4DE-DF11-947F-E0CB4E19F9A2.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/42B629D4-C7DD-DF11-8451-001E68A9934C.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/3A1E0F17-D5DE-DF11-998A-003048CECBC2.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/3638C7DE-E5DD-DF11-A6EF-001D096752BA.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/26B95FF4-B7DD-DF11-86B0-0030487C31C6.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/1CB62435-E7DD-DF11-9E7F-00145E5520E7.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/186B8F80-CFDE-DF11-9F73-001F2965D25E.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0003/060F8468-B7DD-DF11-A924-001A4D5FEEB0.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/F8467CC4-93DD-DF11-BB1D-001E682F25C8.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/EEC2EE08-93DD-DF11-9490-E0CB4E55363E.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/EE87FB3D-B4DD-DF11-AECF-00145E55369B.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/EE230D15-80DD-DF11-8413-001F2965F212.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/DA3DABA5-A0DD-DF11-9EEE-003048C5D1D2.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/D68078E6-A3DD-DF11-AA6A-001517256207.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/D25BAC64-98DD-DF11-BCDC-001A4D5FE6D2.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/CEBCE4A5-85DD-DF11-9432-E0CB4E1A1198.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/CA98D6AC-BEDD-DF11-9F36-90E6BA442F35.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/B82D4EC8-B7DD-DF11-A202-00221993098A.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/B006BB8B-61DD-DF11-BDB8-00261834B5F1.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/A417DF92-C7DD-DF11-8585-485B39800C32.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/A08EAC4E-7BDD-DF11-9E88-00261834B5A2.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/9C767BAE-AEDD-DF11-8A25-00D0680BF8D6.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/98B58B20-56DD-DF11-AE59-485B39800BE3.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/9241CF6F-74DD-DF11-A056-003048C5D908.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/8E81071E-B6DD-DF11-8CFE-001E688E628A.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/8AB8D480-94DD-DF11-ADF9-A4BADB3D00FF.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/8A986E70-A3DD-DF11-B969-003048CEB072.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/86494999-7ADD-DF11-BF0C-485B39800C32.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/84DECC43-91DD-DF11-B3DC-001F296564C6.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/7A2D913F-AADD-DF11-AE4E-E0CB4E29C4E7.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/74E23277-9ADD-DF11-AAEB-0015172560BD.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/74BA24B5-8DDD-DF11-A346-00145E5519CF.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/74B3419B-5FDD-DF11-92F1-00261834B60E.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/70EB212B-89DD-DF11-8357-00D0680BF9A2.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/687B3A66-80DD-DF11-B698-00145E5523ED.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/66F19541-80DD-DF11-8817-90E6BA19A241.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/6685BE28-A0DD-DF11-8FD8-001A4BA83FA4.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/64FB5BF4-8BDD-DF11-83BD-003048CECACA.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/649F75BA-85DD-DF11-A524-485B39800C05.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/62FF793B-8EDD-DF11-AED4-E0CB4EA0A91E.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/608DB606-AADD-DF11-8C76-485B39800B93.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/60058659-7EDD-DF11-BECB-0030487DF78A.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/5CE4D345-91DD-DF11-8FCF-0015172561DA.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/5868A086-9ADD-DF11-B7B6-E0CB4E5536AA.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/569A12C3-84DD-DF11-9DFB-00238B172271.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/4C128F74-7FDD-DF11-80F6-E0CB4E4408C3.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/48E6DB18-A0DD-DF11-94EA-E0CB4E29C4CB.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/46AEA8C7-A4DD-DF11-A03A-90E6BA0D09AA.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/40660ABA-85DD-DF11-94A2-E0CB4E29C50B.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/3EF2C3F8-9EDD-DF11-A125-485B39800B96.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/36D217DC-99DD-DF11-8974-001E68A9948A.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/3683D658-A8DD-DF11-9EE9-E0CB4EA0A909.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/36106186-9ADD-DF11-A4D2-90E6BA442F41.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/2C2B3154-A5DD-DF11-A299-001517357DEE.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/263BCA09-93DD-DF11-8129-E0CB4E1A1152.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/24A85970-5ADD-DF11-9EA3-90E6BA442F15.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/22FAD9EE-A6DD-DF11-8D58-001A4D5FEA46.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/1C063247-91DD-DF11-848C-00151724B660.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/1C03699A-69DD-DF11-88F6-001517255E7A.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/1AD96414-84DD-DF11-AC2C-00145E551712.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/12D5CCDE-A8DD-DF11-8B7E-00248CB320A5.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/12B69895-63DD-DF11-97BF-001F29651428.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/12129F7C-A1DD-DF11-8BCE-00D0680BF982.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/0A3ADAE5-5FDD-DF11-8D7E-00261834B65A.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/08021ACE-7BDD-DF11-BC5F-00145E55226D.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0002/04519B38-4FDD-DF11-B060-E0CB4E5536BE.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0001/948735A2-34DD-DF11-B3F3-E0CB4E19F972.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0001/62579CDC-4ADD-DF11-B460-90E6BA442F41.root',
        '/store/mc/Fall10/TTJets_TuneD6T_smallerISRFSR_7TeV-madgraph-tauola/AODSIM/START38_V12-v1/0001/4A12811C-38DD-DF11-AE18-001EC9D7FA10.root'
    ] );


secFiles.extend( [

    ] )