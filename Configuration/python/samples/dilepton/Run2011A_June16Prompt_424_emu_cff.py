import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_9_3_r0F.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_99_2_qov.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_98_2_bvy.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_97_1_uSC.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_96_1_1mR.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_95_1_TQL.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_94_2_LPn.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_93_2_wBM.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_92_2_vGH.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_91_1_kbg.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_90_2_U71.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_8_1_bBq.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_89_4_xKj.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_88_3_G2Q.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_87_2_fQ2.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_86_3_IwI.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_85_2_BKa.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_84_2_kly.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_83_1_dML.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_82_2_bN0.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_81_4_fVs.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_80_2_u8F.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_7_2_PlO.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_79_1_Cz8.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_78_1_Jml.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_77_1_b9b.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_76_2_O2n.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_75_2_l4K.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_74_2_TtD.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_73_1_UiK.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_72_2_9y4.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_71_2_0St.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_70_2_HnZ.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_6_1_ZrE.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_69_3_ef7.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_68_1_f6F.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_67_1_iU8.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_66_3_vwA.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_65_1_EnX.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_64_2_m3c.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_63_4_vJf.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_62_1_or7.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_61_2_Aph.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_60_2_x3Q.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_5_1_n6j.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_59_2_hf3.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_58_2_T2f.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_57_2_foB.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_56_2_Eqh.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_55_1_KtZ.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_54_2_Vg8.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_53_1_vBi.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_52_1_S5N.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_51_2_1Nm.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_50_3_ghL.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_4_1_xBu.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_49_2_DpA.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_48_1_pAP.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_47_1_OlP.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_46_2_LP7.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_45_3_wbX.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_44_1_PTr.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_43_1_ZXy.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_42_2_qDE.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_41_2_LZD.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_40_4_9gw.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_3_1_m52.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_39_1_lvD.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_38_2_Ro7.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_37_2_POX.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_36_2_MBA.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_35_2_oc0.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_34_1_SBD.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_33_1_iGv.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_32_1_rz1.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_31_1_wp2.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_30_1_NjR.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_2_1_jAr.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_29_2_GXA.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_28_2_1Mq.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_27_2_dkN.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_272_2_k46.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_271_2_jZ8.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_270_1_mIt.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_26_2_ZrI.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_269_2_w2n.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_268_1_51x.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_267_3_R64.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_266_3_lDZ.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_265_1_rF7.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_264_1_a5K.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_263_2_cJh.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_262_3_J4p.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_261_2_RWA.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_260_1_Bf2.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_25_1_R3V.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_259_2_DgL.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_258_2_TI8.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_257_3_5Pm.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_256_2_YGW.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_255_1_flR.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_254_2_9CK.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_253_1_fxB.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_252_3_CCJ.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_251_2_i9i.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_250_2_23l.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_24_1_lum.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_249_2_RwU.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_248_1_uw8.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_247_2_aP4.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_246_3_6ys.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_245_1_OQT.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_244_1_vfe.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_243_2_KQt.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_242_2_XYV.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_241_3_PoR.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_240_4_oAQ.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_23_2_wH9.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_239_1_XXw.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_238_1_hEe.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_237_2_R6q.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_236_1_a6g.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_235_2_DgX.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_234_1_1A3.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_233_1_jvq.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_232_1_kMb.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_231_2_2iY.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_230_1_GIZ.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_22_2_5dp.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_229_1_qtu.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_228_1_3lH.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_227_1_Tml.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_226_1_OK5.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_225_1_xQf.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_224_1_NPN.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_223_2_9IZ.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_222_1_QnK.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_221_2_IjZ.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_220_1_GCg.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_21_2_6Al.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_219_1_Bce.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_218_3_kZm.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_217_2_vgS.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_216_2_eNe.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_215_2_QdC.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_214_2_hGh.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_213_2_S3t.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_212_4_SO8.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_211_1_b07.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_210_1_UlL.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_20_1_QHC.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_209_2_UWQ.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_208_2_4g5.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_207_1_gpC.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_206_2_dwc.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_205_3_0Ox.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_204_3_xwe.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_203_2_GSz.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_202_2_6E2.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_201_1_xEM.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_200_2_wes.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_1_1_xVX.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_19_3_VkP.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_199_1_zPB.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_198_3_JRb.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_197_2_WSc.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_196_1_3X5.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_195_4_ney.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_194_2_0QB.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_193_2_R1i.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_192_2_zHx.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_191_2_Bgh.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_190_1_ZkO.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_18_2_0xE.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_189_2_4mG.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_188_2_jSa.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_187_1_JP2.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_186_2_1bA.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_185_2_KMF.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_184_2_sOZ.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_183_1_h3L.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_182_1_tYs.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_181_1_lIT.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_180_4_q3J.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_17_2_fCg.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_179_2_lAX.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_178_2_2du.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_177_2_jSy.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_176_2_Ko9.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_175_2_QzD.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_174_1_UEJ.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_173_2_lS1.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_172_2_obK.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_171_1_Ua3.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_170_2_P6k.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_16_2_OlO.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_169_3_LsC.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_168_3_0TP.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_167_2_sCM.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_166_3_oDV.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_165_4_Ymd.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_164_4_KLF.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_163_1_AQD.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_162_4_9ws.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_161_3_5lD.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_160_2_Rsq.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_15_2_Yl1.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_159_4_fyB.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_158_1_s2L.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_157_2_uTw.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_156_2_9qH.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_155_2_SjW.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_154_3_WUl.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_153_2_LZw.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_152_2_2kX.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_151_2_9oh.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_150_2_jUO.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_14_2_EQz.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_149_2_otf.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_148_1_sYP.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_147_2_AL6.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_146_2_xTn.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_145_2_eXB.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_144_3_4pe.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_143_2_bu6.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_142_1_I9K.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_141_1_Qc0.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_140_1_P4B.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_13_2_VRk.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_139_1_GIB.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_138_2_weo.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_137_1_jRP.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_136_2_4x9.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_135_2_cph.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_134_1_Qrc.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_133_1_7rq.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_132_1_1Dl.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_131_1_H83.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_130_2_Ndz.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_12_4_sYp.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_129_2_7tO.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_128_1_1kc.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_127_2_68a.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_126_3_BvB.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_125_2_P9T.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_124_1_Af8.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_123_3_iQZ.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_122_2_VJC.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_121_1_PO5.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_120_2_jpk.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_11_2_z6g.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_119_1_izd.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_118_2_TN0.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_117_2_CfX.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_116_1_RsP.root' ] );
readFiles.extend( [

       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_115_1_W2d.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_114_1_HAY.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_113_1_off.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_112_2_94Y.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_111_2_JFB.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_110_1_aZV.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_10_3_bgi.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_109_1_SvV.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_108_2_oqG.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_107_2_WyE.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_106_1_8Jr.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_105_2_r1D.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_104_1_gJU.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_103_1_plK.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_102_1_KkP.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_101_3_cTi.root',
       '/store/user/blutz/MuEG/Run2011A_PromtReco_v4_424_emu_PAT_June16_160404_166502/d70e42597b7ef38d15fdbbcb27072b07/patTuple_100_1_K2M.root' ] );


secFiles.extend( [
               ] )
