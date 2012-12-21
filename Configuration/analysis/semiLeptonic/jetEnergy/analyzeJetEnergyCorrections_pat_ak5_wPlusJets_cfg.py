execfile("TopAnalysis/Configuration/analysis/semiLeptonic/jetEnergy/analyzeJetEnergyCorrections_aod_ak5_anyBkg_cfg.py")

process.p1.remove(process.patDefaultSequence)

process.source.fileNames = ['/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_1.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_2.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_3.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_4.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_5.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_6.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_7.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_8.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_9.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_10.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_11.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_12.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_13.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_14.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_15.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_16.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_17.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_18.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_19.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_20.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_21.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_22.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_23.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_24.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_25.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_26.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_27.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_28.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_29.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_30.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_31.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_32.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_33.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_34.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_35.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_36.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_37.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_38.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_39.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_40.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_41.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_42.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_43.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_44.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_45.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_46.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_47.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_48.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_49.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_50.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_51.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_52.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_53.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_54.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_55.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_56.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_57.root',
                            '/store/user/snaumann/semiLep/wjets_v2/SemiLepPatTuple_58.root']
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_59.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_60.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_61.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_62.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_63.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_64.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_65.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_66.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_67.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_68.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_69.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_70.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_71.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_72.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_73.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_74.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_75.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_76.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_77.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_78.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_79.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_80.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_81.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_82.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_83.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_84.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_85.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_86.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_87.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_88.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_89.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_90.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_91.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_92.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_93.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_94.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_95.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_96.root',
#                            '/store/user/snaumann/semiLep/wjets/SemiLepPatTuple_97.root']

## total number of events, 200/pb: 529
##                         100/pb: 265
##                          50/pb: 132
process.maxEvents.input = -1

process.TFileService.fileName = 'analyzeJetEnergyCorrections_ak5_wjets.root'