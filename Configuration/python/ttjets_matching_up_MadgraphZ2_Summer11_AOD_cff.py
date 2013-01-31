import FWCore.ParameterSet.Config as cms

###########################################################
# Dataset: TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola  #
# Events : 1062792 (68 files)                             # 
# eff    : 1.0                                            #
###########################################################

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [

"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/02EB2BC5-3BDB-E011-8AB4-001A64789D94.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/0C8E2249-46DB-E011-B825-001A6478AB00.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/0E4E97AD-2DDB-E011-A921-001A64789DEC.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/0E9F293A-27DB-E011-9C59-001A64789E6C.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/101BE4DC-46DB-E011-97FD-002590200B6C.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/10ABD2BD-28DB-E011-8F50-001A64787060.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/143032C2-45DB-E011-9FCD-002590200868.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/1626918F-26DB-E011-A04F-001A64789D10.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/18CF89B7-28DB-E011-9A5C-001A647894F4.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/18D0800E-2ADB-E011-981A-001A64789DE0.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/1C3631DF-48DB-E011-8CB5-001A64789E18.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/26152F1C-48DB-E011-ABE8-002590200A98.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/3077B57A-4CDB-E011-9D37-002590200918.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/3292447A-3CDB-E011-BCF1-002590200948.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/383F5252-2BDB-E011-84D2-003048673F08.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/3C84F277-3FDB-E011-87A6-002590200868.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/3E7E9368-3EDB-E011-915B-00259020093C.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/42CB21C5-39DB-E011-B57B-002590200AC0.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/44B74260-44DB-E011-8E8F-002590200970.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/48FD023F-CEDB-E011-8FE0-002590200898.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/563FC879-47DB-E011-86D4-002590200868.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/580F8562-3EDB-E011-A9F2-003048673F9E.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/646E51DC-3CDB-E011-9610-001A64789DF4.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/660D80CA-42DB-E011-9619-002590200B60.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/683A0415-40DB-E011-B913-001A64787064.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/68F312CB-49DB-E011-97C2-0025902009E8.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/6ABDCA55-4ADB-E011-8401-002590200898.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/6E27C87B-27DB-E011-8CFF-003048673F08.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/6ECBB18F-44DB-E011-B4F8-0025902008F0.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/7C8A1923-BDDB-E011-A134-0025902009CC.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/7CD045B4-28DB-E011-9913-001A64789E6C.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/82AEB860-48DB-E011-B565-001A64789E18.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/88582A79-45DB-E011-BEE1-002590200A80.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/8E677DA9-43DB-E011-90E5-002590200908.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/901CA9C5-3FDB-E011-8FC0-001A64789CF0.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/940683A4-48DB-E011-B9BC-002590200828.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/9476E211-3EDB-E011-874C-002590200824.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/966D7F18-29DB-E011-BE18-003048670B4A.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/9CAD39CE-27DB-E011-A373-001A64789D20.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/9CECFBE4-41DB-E011-B001-002590200898.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/9EEEEAFB-2DDB-E011-B7D7-001A6478ABA8.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/A09CAA15-27DB-E011-BF6C-001A64789E00.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/A0FB9ABF-28DB-E011-9699-001A6478933C.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/A6730B80-42DB-E011-886D-001A64789DEC.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/A6909A05-4DDB-E011-B3D8-0025902008A4.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/ACEDFEEB-3ADB-E011-99F4-001A6478ABB4.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/AE4A52C3-29DB-E011-AB23-001A64789E18.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/AEBEE124-29DB-E011-A27D-001A64787078.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/B61F4245-44DB-E011-A232-001A64789DEC.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/B88E3442-4DDB-E011-B0BD-001A64789D94.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/BA7F9E0A-41DB-E011-90DE-001A64789E18.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/BC1EBDCC-4BDB-E011-83D2-001A6478945C.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/BE518189-36DB-E011-BB27-003048673FC0.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/C04F0266-ABDB-E011-869F-003048673FEA.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/C8C65DB4-28DB-E011-9B99-001A647894DC.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/CAB29524-42DB-E011-AE6C-0025902008F4.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/D4D1AB76-47DB-E011-BC72-001A64787064.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/D6A7582E-38DB-E011-A547-001A64789D94.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/DAED32C7-3EDB-E011-8670-002590200878.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/DC570974-45DB-E011-A586-003048673F9E.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/E0954F66-48DB-E011-92BD-002590200970.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/E0C2EB5C-29DB-E011-8C3C-001A64789D10.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/E6C1553F-4BDB-E011-B9A5-002590200AE4.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/E816734D-41DB-E011-9358-002590200838.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/F05BBF2D-45DB-E011-BD31-001A64789DEC.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/F2E25110-51DB-E011-A80E-002590200908.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/F6690A1D-29DB-E011-9757-001A64789E00.root",
"/store/mc/Summer11/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/F81626F1-48DB-E011-AFEB-001A64789E20.root"

     ] );

secFiles.extend( [
               ] )
