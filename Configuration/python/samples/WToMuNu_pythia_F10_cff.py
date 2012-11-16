####################################################################################################################################
#  
#          dataset name: /WToMuNu_TuneZ2_7TeV-pythia6/dammann-Fall10-PAT-v2-43e23e1dee19d970b0c8344e9053309f/USER
#               DBS URL: https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_02_writer/servlet/DBSServlet
#            global tag: START38_V13::All
#         mother sample: /WToMuNu_TuneZ2_7TeV-pythia6/Fall10-START38_V12-v1/AODSIM
#      number of events: 5323040
#         cross section: 10438
#  generator efficiency: 1.0000
#
####################################################################################################################################

import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_9_2_xNO.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_99_2_oIw.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_98_2_pZP.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_97_2_B6J.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_96_2_TyG.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_95_2_5b2.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_94_2_sxC.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_93_2_94O.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_92_2_8Vw.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_91_2_Qod.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_90_2_xM8.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_8_2_YXT.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_89_2_Zc5.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_88_2_kGv.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_87_2_VmC.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_86_2_bt8.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_85_2_C6U.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_84_2_FsU.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_83_2_sEl.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_82_2_KxZ.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_81_2_mEw.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_80_2_KMS.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_7_2_gWd.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_79_2_EGI.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_78_2_GhB.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_77_2_9Tu.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_76_2_lfn.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_75_2_IAX.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_74_2_rEZ.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_73_2_XzG.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_72_2_Zr4.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_71_2_knT.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_70_2_5D4.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_6_2_LGv.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_69_2_82C.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_68_2_531.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_67_2_wWr.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_66_2_iei.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_65_3_eS8.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_64_2_mmU.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_63_2_8UC.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_62_2_6uW.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_61_2_UPr.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_60_2_6HT.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_5_2_04F.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_59_3_l6n.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_58_2_lXA.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_57_2_r88.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_56_2_arb.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_55_2_QON.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_54_2_geN.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_53_2_SIH.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_52_2_zhm.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_51_2_6Bi.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_50_2_faW.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_4_2_vbF.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_49_2_Pu5.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_48_2_BIZ.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_47_2_l30.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_46_2_YSI.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_45_2_Nf6.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_44_2_oY9.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_43_2_0t7.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_42_2_2rr.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_41_2_a7k.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_40_2_TgM.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_3_2_uBm.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_39_2_mVC.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_38_2_0dx.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_37_2_pkY.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_36_2_Pzo.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_35_2_JEL.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_34_2_JCS.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_33_2_jZP.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_32_2_z4k.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_31_2_1DV.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_30_2_D4r.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_2_2_GUn.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_29_2_wdy.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_28_2_ZJl.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_27_2_HKA.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_26_2_qnN.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_25_2_wvB.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_24_2_bdX.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_23_2_6hi.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_22_2_PFS.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_21_2_iWK.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_20_2_kwX.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_1_2_OYE.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_19_2_doY.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_18_2_wAL.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_17_2_ssu.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_16_3_QAh.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_15_2_beT.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_14_2_btf.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_13_2_q0N.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_12_2_oet.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_11_2_9gX.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_10_2_Kfp.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_107_2_f9O.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_106_2_I4C.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_105_2_Nt5.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_104_2_j5R.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_103_2_zQi.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_102_2_mww.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_101_2_Mg1.root',
       '/store/user/dammann/WToMuNu_TuneZ2_7TeV-pythia6/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_100_2_RjV.root' ] );


secFiles.extend( [
               ] )
