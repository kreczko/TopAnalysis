from TopAnalysis.Configuration.defines import sizes 
from TopAnalysis.Configuration.defines import source

######################################################################
## PAT Tuples:
## -----------
## /ZZ/Winter09_IDEAL_V12_FastSim_v1/GEN-SIM-DIGI-RECO
##
## Events      :     13443 (200000 processed)
## xsec(pb)  LO:       7.1
## xsec(pb) NLO:       NAN
## eff         :      1.00
######################################################################
sizes ['zzx0_0'] = 13443
source['zzx0_0'] ='\'/store/user/dammann/zz/patTuple_PATv2_zz_1.root\','
source['zzx0_0']+='\'/store/user/dammann/zz/patTuple_PATv2_zz_2.root\','
source['zzx0_0']+='\'/store/user/dammann/zz/patTuple_PATv2_zz_3.root\','
source['zzx0_0']+='\'/store/user/dammann/zz/patTuple_PATv2_zz_4.root\''

