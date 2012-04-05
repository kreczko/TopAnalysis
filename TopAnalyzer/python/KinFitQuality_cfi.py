import FWCore.ParameterSet.Config as cms

from TopQuarkAnalysis.TopObjectResolutions.stringResolutions_etEtaPhi_cff import *

analyzeKinFitQuality = cms.EDAnalyzer("KinFitQualityAnalyzer",
    ## input collectionA
    srcA = cms.InputTag("ttFullHadEvent"),
    ## input collectionB                            
    srcB = cms.InputTag("selectedPatJets"),                                         
    ## analyzer specific configurables
    analyze   = cms.PSet(
        ## choose TTree for output instead of histograms, if applicable
        useTree  = cms.bool(False),
        ## number of hypotheses for plot kinFit Chi2 and Prob
        numberOfHypos = cms.uint32( 1 ),
        ## resolutions used for the kinematic fit
        udscResolutions = udscResolution.functions,
        bResolutions    = bjetResolution.functions,
        ## resolution scale factors
        jetEnergyResolutionScaleFactors = cms.vdouble(1.0),
        jetEnergyResolutionEtaBinning = cms.vdouble(0.0,-1.0)
    )
)



