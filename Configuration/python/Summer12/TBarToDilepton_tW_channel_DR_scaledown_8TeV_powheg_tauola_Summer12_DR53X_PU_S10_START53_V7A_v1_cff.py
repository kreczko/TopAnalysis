import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/0217A5B1-C8D9-E111-A789-0030487F9297.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/025BF9F6-D6D9-E111-8BA4-0030487F92AD.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/02B04D76-BDD9-E111-BD75-0030487F929F.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/08A02922-CCD9-E111-AD71-003048C69316.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/0E5BF5B9-F2D9-E111-892D-0030487F1665.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/10137B7A-5BDA-E111-B977-0030487F1A73.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/10F9841B-D5D9-E111-8408-0030487F1BCF.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/023D281D-DCD9-E111-8FE3-0030487E52A5.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/02BB2739-D4D9-E111-98E7-003048D4DEA6.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/189290EF-E5D9-E111-BD0A-0030487FA60D.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/0876E690-FCD9-E111-B546-0030487D5DB7.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/1A7F8986-EED9-E111-B0BF-003048C6931C.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/0E7B3AD6-C6D9-E111-95B2-0030487FA4C5.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/1EEEDB46-CDD9-E111-A8E0-0030487FA60B.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/22A2C1DD-CFD9-E111-BD57-0030487D5EAD.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/242A4BB2-CED9-E111-853D-0030487D5DBF.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/16897F75-B3D9-E111-B1AB-0030487F172B.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/16C25CB8-31DA-E111-93B7-0030487D5EAD.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/26C13A47-E3D9-E111-ABBC-0030487D5EAD.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/28A3CC3A-F7D9-E111-B9B8-0030487F9351.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/2A771FA1-C7D9-E111-9842-0030487E4ED5.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/18F010D2-93D9-E111-A331-0030487FA609.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/2C06DF9C-B7D9-E111-83CB-003048C693FC.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/1AFCB48E-C5D9-E111-81CE-0030487D5DB5.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/2CCB79C1-9CD9-E111-BBA0-003048D439A0.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/32ADC3AC-FCD9-E111-B014-0030487D5D53.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/38168B82-FFD9-E111-AFC5-002481E0EA70.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/242FF006-DFD9-E111-889C-0030487D5E49.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/382EE96A-BFD9-E111-B930-0030487D70FD.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/24460786-FFD9-E111-9524-0030487F92AB.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/3ADDA9F0-EAD9-E111-9EB4-0030487FA607.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/2AA55F32-45DA-E111-8654-0030487F1731.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/3EA92D7D-D3D9-E111-BE56-0030487E4EC5.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/2C122A20-E2D9-E111-81EA-0030487D5E67.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/4404EE0E-20DA-E111-A73F-0030487F16F9.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/4469AE53-EDD9-E111-AD01-0030487E4ED3.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/46AC347B-D2D9-E111-BC06-0030487E54B7.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/4813E4AC-E7D9-E111-AEFD-0030487F1BD5.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/381F88B3-C3D9-E111-B4E3-0030487F132D.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/4C53D194-CED9-E111-8E2A-0030487F9331.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/4C7AFA42-CBD9-E111-B4AB-003048C69316.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/4E0A9D2D-D4D9-E111-9D00-0030487D70FF.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/38CB3574-C2D9-E111-96A8-0030487F92A5.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/3CEED88C-07DA-E111-8E76-0030487F1C51.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/3EDC815E-38DA-E111-AE8D-0030487F1A49.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5C3AB436-DAD9-E111-8155-0030487F16F7.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5C4287D4-C5D9-E111-BA38-0030487D70FF.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5C512360-DAD9-E111-A5B5-0030487F933F.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/488C33BC-00DA-E111-A2CF-003048C69292.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/605BFCF5-D0D9-E111-BDA2-0030487F16BF.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/4E217309-E8D9-E111-973E-0030487F1655.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/625DA406-C4D9-E111-A86F-0030487D8633.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/58E73E43-D6D9-E111-9019-003048C68A84.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/689509AF-AAD9-E111-80D0-0030487D605B.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/68A9F650-E4D9-E111-936E-0030487F1731.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5C1C8DDA-EED9-E111-9BC3-0030487E54B7.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/6A23AD7D-C1D9-E111-A515-0030487F92A5.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/5CDEE8E4-C6D9-E111-9276-0030487DE7BD.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/6242162B-C1D9-E111-BD66-0030487F1735.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/6EF6B0D5-DED9-E111-9276-0030487F92A9.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/7022851E-D5D9-E111-9117-0030487D5DA3.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/7083CA13-D0D9-E111-BD7B-0030487D5EBB.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/741FE18A-B1D9-E111-A920-0030487D5EAD.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/74DA7FCB-52DA-E111-810E-0030487F1C4F.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/6290152B-DDD9-E111-AC80-0030487F88EB.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/7AC5B8B4-F9D9-E111-93EA-0030487F1717.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/68B858CB-F8D9-E111-B190-0030487F929B.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/80AF7487-DAD9-E111-B3B3-003048C6928E.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/6A8DEB82-D2D9-E111-B620-0030487F1667.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/82016A19-F0D9-E111-9F53-0030487D5DB7.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/82501809-E5D9-E111-A879-0030487F1C4F.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/6ABE4FA5-DED9-E111-B5EA-0030487F92B3.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/84B66B41-BAD9-E111-960B-0030487DE7C5.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/86276CBA-D2D9-E111-89AB-0030487F1665.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/78038926-C1DA-E111-A17B-0030487D5DA5.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/8E2EEAF4-E7D9-E111-AF71-0030487F1A49.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/8E963432-D0D9-E111-8C86-003048C69416.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/7CB6BC30-B9D9-E111-A5BB-003048C692F2.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/82011B4B-CCD9-E111-8B9A-0030487D8633.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/82AB6A08-C0D9-E111-A8BD-0030487D70FD.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/8C43DA77-FDD9-E111-B55A-0030487D5DA9.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/90255FB9-A1D9-E111-839B-0030487F1309.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/90C846A1-0BDA-E111-97C7-0030487E0A29.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/90F76C34-F1D9-E111-A8FC-00215AEDFD12.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/9217DD60-BFD9-E111-A749-0030487F1653.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/9A72AA2E-DAD9-E111-AC53-003048C68A98.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/9246217C-03DA-E111-9C22-0030487D70FD.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/94630E7D-BFD9-E111-8D43-0030487F1C51.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/94CBDDEB-DCD9-E111-9D15-0030487F1A73.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/96C8B95D-EAD9-E111-8A42-0030487F92FF.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/9A9A0343-AED9-E111-AECD-0030487F1BD5.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/9C7BBA65-ECD9-E111-A0F8-0030487F92A9.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/ACA2D330-D6D9-E111-9134-003048C6931C.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/ACE0768A-C8D9-E111-999D-0030487D5DBD.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/AE9580BF-D7D9-E111-9220-0030487F1735.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/9E98E100-D9D9-E111-B563-003048C68A80.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/A00C4D98-D3D9-E111-B64A-0030487D5DB1.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B0FEC894-08DA-E111-BD67-003048C693F0.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/A0A083DE-FED9-E111-A474-0030487F938F.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/A8A2CFC9-0DDA-E111-A6B0-0030487D5D6B.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B873F167-DBD9-E111-AA38-0030487FA609.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/AEE3D037-E4D9-E111-BF63-0030487F92B1.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B0D22D8B-C5D9-E111-ADE0-0030487F910D.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B64F6FBF-D6D9-E111-A33F-0030487F164F.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B691AF2A-BCD9-E111-97D9-003048D4399C.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/B88CF79B-F6D9-E111-80A6-0030487D5E75.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/BA14D01E-48DA-E111-8F22-0030487EBB27.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C0A1DE89-D2D9-E111-8CBC-003048C66180.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C222442B-02DA-E111-8A7B-002481E7636A.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C4B370AC-DFD9-E111-9093-0030487F92B3.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/BA9374C2-F4D9-E111-8A95-0030487D7105.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C6DC4703-DCD9-E111-A62B-0030487FA609.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/BCFB3A9F-FBD9-E111-8F3F-0030487E0A29.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C8CC1D08-CED9-E111-B453-0030487D5DBF.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/BEEAA90C-D9D9-E111-81A0-003048D4393E.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/CC256877-DFD9-E111-8AD7-0030487D5E49.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/CC27BB65-ECD9-E111-90FB-0030487F92A9.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C026D5FD-BFD9-E111-B0BE-0030487F1653.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C650D0A0-A6D9-E111-9636-003048C69046.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D07729E4-CED9-E111-8712-0030487D5D89.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/C6FA3A7B-EED9-E111-AAF1-0030487F1BE5.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D2FFFDF1-DFD9-E111-9A6A-0030487F1C55.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D4B8602B-CAD9-E111-ACA9-0030487D5D89.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D4FF185E-E3D9-E111-B577-003048C69316.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/CAB04B04-C8D9-E111-949C-0030487D811F.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/CC8AB3C9-B4D9-E111-A5B4-0030487E4EC7.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D6B1D6EB-BBD9-E111-84E0-0030487FA60D.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/CEBCD981-C5D9-E111-8D8C-0030487F1657.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D81FCDB4-C3D9-E111-8B15-0030487D70FF.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/DC73EFCD-F3D9-E111-89DC-0030487D5EA1.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/DCA7B2CC-C6D9-E111-A153-003048D4DFAA.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D0C83D64-F8D9-E111-BE03-0030487F9351.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/E2264FEC-D0D9-E111-BD3C-0030487EA3DD.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/E48D5676-D6D9-E111-8F95-0030487D5EAD.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D62BDF88-05DA-E111-91F3-0030487D86CB.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/E84479B0-D2D9-E111-89C9-0030487D5EBB.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D641C4C4-CED9-E111-A2C5-0030487FA607.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/D6EFE3B9-CAD9-E111-A332-0030487F1715.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/E8BA3FE4-C6D9-E111-B27E-0030487D70FF.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/E8DED8E8-D7D9-E111-8FB3-0030487F1BD3.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/E09C6535-CBD9-E111-8FB8-003048C693E4.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/EC49BD59-C3D9-E111-BCCF-003048C692E4.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/E841C459-E1D9-E111-B5C5-0030487D5DB7.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/F43E65F1-FED9-E111-9DDE-003048D4DFA4.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/F4942873-E1D9-E111-932C-0030487D5EA1.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/E858F76B-CBD9-E111-9D08-0030487F1A67.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/F6E93C0E-CCD9-E111-BCDE-0030487F172B.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/E88D4B4F-CDD9-E111-92FE-0030487D8633.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/EA6DCF49-D1D9-E111-AA78-0030487F910D.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/EE6BB01D-D9D9-E111-B955-003048C68A8E.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/F4FB14C6-F9D9-E111-A32C-0030487D814B.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/FA8EE023-28DA-E111-BD7B-0030487F1735.root',
       '/store/mc/Summer12_DR53X/TBarToDilepton_tW-channel-DR_scaledown_8TeV-powheg-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/FE0D550E-CED9-E111-8B43-0030487D5D89.root' ] );


secFiles.extend( [
               ] )
