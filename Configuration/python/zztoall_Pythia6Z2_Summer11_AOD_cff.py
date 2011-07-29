import FWCore.ParameterSet.Config as cms

################################################################################
# Dataset: /ZZ_TuneZ2_7TeV_pythia6_tauola/Summer11-PU_S4_START42_V11-v1/AODSIM # 
# Events : 4187885                                                             #
# eff    : 1.0                                                                 #
################################################################################


maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource", fileNames = cms.untracked.vstring( *(
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/FE6EADE6-BFAC-E011-BBCC-00261894387A.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/FE33217A-BCAC-E011-9273-003048678F62.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/FCB26DEA-CDAC-E011-9E56-002618943831.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/F6701462-D9AC-E011-933D-003048679076.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/F603E718-DBAC-E011-A6F2-002618943954.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/F4B29F33-BAAC-E011-AB1D-00248C0BE014.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/F4905BAC-D9AC-E011-838E-001A92971B08.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/F449FA76-BCAC-E011-92CA-0026189438CC.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/F425D0F2-BBAC-E011-A88F-002618943905.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/F214D2D7-E2AC-E011-BC8C-001A92971BBE.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/EE00760D-BDAC-E011-9A36-003048678B8E.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/EC3BC67A-BCAC-E011-AE00-0030486792DE.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/E8ED0C56-B5AC-E011-AEBB-0018F3D095FA.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/E893A03A-BAAC-E011-8105-001A92971BBE.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/E69263E7-B1AC-E011-BADA-003048678FB4.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/E671429D-BBAC-E011-8DD9-003048678FC4.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/E6128D83-DAAC-E011-B3B3-0018F3D095FA.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/E4FB754F-B7AC-E011-ADC3-00261894387E.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/E4E3634C-B7AC-E011-9844-003048678FEA.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/E4A8A6FE-B1AC-E011-AAC8-00248C0BE018.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/E2EF15FF-CFAC-E011-897F-003048678FC4.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/E2857381-BEAC-E011-B422-002618943821.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/E0724912-B3AC-E011-9867-00261894393B.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/E025DD07-B3AC-E011-BE33-002618943957.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/DE088C85-BEAC-E011-AD3B-003048678C9A.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/D6DF5CCC-BEAC-E011-9240-001A92971B04.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/D616495F-AEAC-E011-A8C1-00261894388A.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/D4367609-AFAC-E011-AAE9-00304867C1BA.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/D2CBFA7E-B8AC-E011-A2E2-0026189438E9.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/D2729752-B5AC-E011-B5FA-003048678AF4.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/D03B5016-B3AC-E011-91D3-003048678FE6.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/CE5629F3-BBAC-E011-BED6-002354EF3BD2.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/CCF08671-CAAC-E011-86E1-00304867915A.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/CC5E3BE3-B3AC-E011-8926-002354EF3BD2.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/CABF6C3D-CEAC-E011-A9E9-002618943959.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/CA326DBF-BAAC-E011-A9CE-003048678AC0.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/CA14D299-B7AC-E011-86A2-003048678FC4.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/C8053739-BAAC-E011-84D1-003048678ED4.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/C6688CBE-BAAC-E011-89E1-003048678FEA.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/C634C5E7-B9AC-E011-9861-003048678FE0.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/C43AF00F-B3AC-E011-906B-002618943935.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/C2968FBA-AFAC-E011-B819-002618943856.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/C24F20F2-B0AC-E011-B2C2-002618943914.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/C23929C6-BCAC-E011-86E2-00261894398B.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/C0A0D585-BEAC-E011-98C8-003048678FC4.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/C019F10B-BDAC-E011-BB75-00304867906C.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/BEE2F5D6-E4AC-E011-BE1E-003048678BAC.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/BED72DDD-B1AC-E011-BF24-002618943836.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/BEAAFAF2-B0AC-E011-A300-002618943934.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/BEA0769D-ADAC-E011-8707-00261894389E.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/BE28C10C-C1AC-E011-8F9D-002618FDA263.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/BC914F76-BCAC-E011-B71C-0026189438BC.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/BADD2A5A-BDAC-E011-848B-002354EF3BD2.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/BAC3D9DD-B3AC-E011-8B0F-0026189438FE.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/BA9BE4E9-B5AC-E011-B28D-0018F3D0960A.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/B6F6FEEF-BBAC-E011-81B9-002618943964.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/B668AEDB-B3AC-E011-8F9B-0026189438BF.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/B440E138-DAAC-E011-A555-002618943821.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/B0BD399F-BBAC-E011-BF80-00261894397E.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/B087A22B-C0AC-E011-9EFD-002354EF3BE3.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/B006B955-B5AC-E011-A178-00304867920C.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/AEEEF938-BAAC-E011-9611-003048679228.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/AE3691AC-DFAC-E011-82B4-00261894394F.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/AC1451CA-BCAC-E011-A49A-0018F3D095FA.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/AABA539C-B7AC-E011-9FA9-00304867918A.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/AA909972-B6AC-E011-AE91-002618943915.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/AA8F1253-BDAC-E011-A27F-00248C65A3EC.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/A8F5CCC9-BEAC-E011-8E2C-003048678B8E.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/A8086E2E-BAAC-E011-8A9A-0026189437F8.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/A800F883-D8AC-E011-A7BF-003048678F84.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/A4FC55EE-D1AC-E011-B6D7-00304867916E.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/A4BEA2F5-B1AC-E011-AC74-002354EF3BDC.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/A2FFCFB5-B2AC-E011-A285-00261894393E.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/A2DDB753-BDAC-E011-BCE9-00261894393A.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/A2A1D00A-BBAC-E011-BE2E-0026189438BC.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/A28EE4C0-C2AC-E011-ADCB-00304867915A.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/A252AEE2-B3AC-E011-AA23-0018F3D096A4.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/A05AA9C3-AEAC-E011-8FCE-003048678E52.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/9CED8F38-BAAC-E011-A034-00304867906C.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/9CA04E3A-BAAC-E011-B1D4-001A92971BD6.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/9C7141DC-B3AC-E011-BD6B-002354EF3BD2.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/9A959F1B-B3AC-E011-AD1A-003048678C62.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/9A05D69D-B7AC-E011-830B-002618943821.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/94E6279F-BBAC-E011-A309-00261894395F.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/92975A4E-B7AC-E011-A8B2-003048678B18.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/90F955AB-DBAC-E011-BD05-002618943954.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/90120A2A-B8AC-E011-A192-003048678AC0.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/8E613E80-B8AC-E011-ACCF-002618943975.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/8E0A7636-D6AC-E011-A5E0-003048679180.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/8ACC9955-C1AC-E011-B4FE-00261894382D.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/8ABC2986-D4AC-E011-8659-00304867915A.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/8A54B8AA-CFAC-E011-9AAA-002618943856.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/88C8922A-B8AC-E011-A584-0026189438E0.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/887729F4-C1AC-E011-A8D4-00304867915A.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/86A6AFDB-B3AC-E011-B70D-003048679084.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/864D5498-B5AC-E011-8579-003048678BAA.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/84912704-CBAC-E011-8A7D-002618943821.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/80F56227-C6AC-E011-AD5D-0030486792BA.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/80E13AF6-DDAC-E011-A936-0026189438BD.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/80A86572-B6AC-E011-B7B0-00261894397D.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/80626F5B-D7AC-E011-9FCE-002618943966.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/7E31782C-B8AC-E011-BBD4-00261894389E.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/7AABA785-BEAC-E011-ABD6-0026189438BC.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/783B5EE5-B5AC-E011-BC5C-002618943821.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/76BC306F-C6AC-E011-BE2C-003048678AC0.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/74DDC109-F4AC-E011-9388-001A92971B08.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/727CF406-AFAC-E011-A698-00304867BFAE.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/70EFDF7D-B8AC-E011-AD33-0026189438CC.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/7056FD84-BEAC-E011-8113-0030486792AC.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/6E9D853C-D0AC-E011-994E-003048678AC0.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/6E7F7279-C4AC-E011-AC69-00248C0BE014.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/6E2008A1-BBAC-E011-90B2-003048678F62.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/6CA3D97B-C0AC-E011-9909-00304867918A.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/6C3B6A00-DCAC-E011-91E5-001A92971B08.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/6AB8AFE3-BFAC-E011-811F-003048678B3C.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/689781F3-B0AC-E011-A602-003048B95B30.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/688BD47C-B8AC-E011-9CCC-002354EF3BD0.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/6862CF10-C1AC-E011-B868-002618943821.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/66C25C79-C2AC-E011-8F84-003048D3FC94.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/668508A0-B9AC-E011-AB5F-002354EF3BCE.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/6680CBB9-AFAC-E011-AEDE-002618943826.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/6415A2D0-ACAC-E011-A480-00261894389A.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/62A18B71-B6AC-E011-9E80-0030486790B8.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/60C4E3C2-BEAC-E011-9CE6-003048678ED4.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/60B9BDEC-BBAC-E011-B2A8-002618943809.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/5EE1299D-B5AC-E011-BC3B-001A92971BD6.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/5E0521A9-D9AC-E011-BBB9-00261894388A.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/5C2B47CB-B8AC-E011-B86B-001A92971BBE.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/58FA414D-B7AC-E011-A776-002618943966.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/58C391FC-D5AC-E011-9C23-002618943921.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/58C0292B-B8AC-E011-96C8-002618FDA208.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/5877E2BD-BAAC-E011-8DC5-00304867916E.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/56A8B03B-D6AC-E011-A869-003048678AC0.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/5665849D-BBAC-E011-A114-0030486792DE.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/563DD1E8-B9AC-E011-A081-002354EF3BDF.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/54AE519F-B9AC-E011-817C-0026189438E0.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/54419E9B-B5AC-E011-82E5-002618943966.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/529CB7EF-C1AC-E011-9335-002354EF3BD0.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/50D25205-C9AC-E011-B149-001A92971B90.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/503B5B9D-B5AC-E011-BEF6-002354EF3BDB.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/4EF69903-EEAC-E011-B981-001A92971B08.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/4CDE27F3-DFAC-E011-B37A-002618943916.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/4CCA1EB6-B2AC-E011-B83A-00304867902C.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/4C92EB1A-E1AC-E011-B2F0-003048678AC0.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/4C52B181-B8AC-E011-AFE2-00261894397E.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/4C385C6D-E1AC-E011-B22E-003048678B1A.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/4AE49FC1-B8AC-E011-B3F5-00304867BFA8.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/4AB39641-DCAC-E011-A2AE-002618943921.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/4A108F54-B5AC-E011-9FF2-00304867916E.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/48F843E6-B5AC-E011-A279-002618943940.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/4832BE55-B5AC-E011-88F4-002618943821.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/48205D40-DEAC-E011-9302-002618943894.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/46F65F2B-B8AC-E011-8D16-00261894397F.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/46989097-B5AC-E011-ABEB-00261894387E.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/467418EE-D7AC-E011-BAF6-002618943885.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/465B179F-B9AC-E011-8140-002618943981.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/44D2ACA2-B0AC-E011-BB95-00261894395A.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/447BAAE8-B9AC-E011-8468-001A92971BD8.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/442D207C-CCAC-E011-B7F9-00304867BFAE.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/42C0A798-B5AC-E011-81D2-003048B95B30.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/42092FC4-BEAC-E011-A3BB-0030486790B8.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/3CF1ED9E-BBAC-E011-A0E6-0026189438BC.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/3C89EAA0-BBAC-E011-9157-00304867918A.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/3A689AA4-B7AC-E011-B3F3-0026189437FA.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/3883689D-B9AC-E011-B470-002618943862.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/36F856A0-CDAC-E011-BA60-002354EF3BCE.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/32450471-B6AC-E011-9E6B-002618FDA208.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/2E9DC3A0-B9AC-E011-9C38-002618943948.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/2E03B531-B8AC-E011-A174-00304867915A.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/2CF37451-B3AC-E011-83ED-002618943915.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/2C81386C-D3AC-E011-AABA-003048678FE4.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/2AC7B1B0-D1AC-E011-9E83-0030486790B8.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/24EFA0AC-D3AC-E011-81D9-001BFCDBD160.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/24D13D42-CEAC-E011-A838-001A92971BDC.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/24B98BE3-B5AC-E011-AC86-00304867BFAE.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/240B37E7-B9AC-E011-8EA8-003048678BAA.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/22E5B97E-B8AC-E011-BD39-002618943845.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/2297549C-B7AC-E011-814E-003048678EE2.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/20C70BB7-B2AC-E011-8044-003048678AE2.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/209D419F-B9AC-E011-9EFE-002618943916.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/1EAEA5A2-BBAC-E011-AD7C-0026189438CC.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/1E688E3B-D0AC-E011-A1AD-00304867915A.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/1C7CA3C8-BCAC-E011-8A0D-00261894396F.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/1A9939C4-BAAC-E011-8623-00304867920C.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/1A4DDE13-B3AC-E011-8F66-002354EF3BD2.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/18FC97C6-BCAC-E011-9170-0026189438EF.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/16ECC66E-B6AC-E011-980E-003048678FEA.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/169DEB9C-B7AC-E011-8951-0026189438EB.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/16469C0B-BDAC-E011-89E9-002618943916.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/147246C3-C2AC-E011-A817-0018F3D09704.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/145200A0-B0AC-E011-AEA5-0030486792B4.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/128482BB-C4AC-E011-BC64-0026189438CC.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/106B15F4-D7AC-E011-A48C-00248C0BE01E.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/1039BEC3-BEAC-E011-A361-002618943956.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/0EADD757-C7AC-E011-BE62-00261894383E.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/0E37FF5D-DDAC-E011-9161-0026189437F0.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/0ADCE0A2-BBAC-E011-BCCC-0026189438E9.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/0A46EAE1-B3AC-E011-B9AD-00261894385A.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/0A2DFDF3-BBAC-E011-A7DE-0026189438E8.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/084BCD9F-B0AC-E011-860A-0030486790B8.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/0430599D-B9AC-E011-9375-0026189438A9.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/0411BBB6-B2AC-E011-BF97-002354EF3BDC.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/02CAE4BE-BAAC-E011-BFEE-002354EF3BDA.root',
'/store/mc/Summer11/ZZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/02620D22-D3AC-E011-AF10-00304867916E.root'
    ) )
)
