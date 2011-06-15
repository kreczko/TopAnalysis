import FWCore.ParameterSet.Config as cms

def prependPF2PATSequence(process, pathnames = [''], options = dict()):

    ## output all options and set defaults
    print 'options used by prependPF2PATSequence:'
    print 'runOnMC:', options.setdefault('runOnMC', True)
    #print 'postfix:', options.setdefault('postfix', '')
    print 'runOnOLDcfg:', options.setdefault('runOnOLDcfg', False)
    print 'cutsMuon:', options.setdefault('cutsMuon', 'abs(eta) < 2.5 & pt > 10.')
    print 'cutsElec:', options.setdefault('cutsElec', 'et > 20 & abs(eta) < 2.5')
    print 'pfIsoConeMuon:', options.setdefault('pfIsoConeMuon', 0.3)
    print 'pfIsoConeElec:', options.setdefault('pfIsoConeElec', 0.3)
    print 'pfIsoValMuon:', options.setdefault('pfIsoValMuon', 0.2)
    print 'pfIsoValElec:', options.setdefault('pfIsoValElec', 0.13)

    ## postfixes are NOT supported right now
    postfix='' #options['postfix']

    ## Standard Pat Configuration File
    process.load("PhysicsTools.PatAlgos.patSequences_cff")

    ## this needs to be re-run to compute rho for the L1Fastjet corrections
    from RecoJets.JetProducers.kt4PFJets_cfi import kt4PFJets
    process.kt6PFJets = kt4PFJets.clone(src='pfNoElectron', doAreaFastjet=True, doRhoFastjet=True, rParam=0.6)

    ## create a good vertex collection
    pvSelection = cms.PSet(
          minNdof = cms.double( 4.)
        , maxZ    = cms.double(24.)
        , maxRho  = cms.double( 2.)
        )

    process.goodOfflinePrimaryVertices = cms.EDFilter(
        "PrimaryVertexObjectFilter" # checks for fake PVs automatically
        , filterParams = pvSelection
        , filter       = cms.bool(False) # use only as producer
        , src          = cms.InputTag('offlinePrimaryVertices')
        )

    process.goodOfflinePrimaryVerticesWithBS = cms.EDFilter(
        "PrimaryVertexObjectFilter" # checks for fake PVs automatically
        , filterParams = pvSelection
        , filter       = cms.bool(False) # use only as producer
        , src          = cms.InputTag('offlinePrimaryVerticesWithBS')
        )

    ## only added as the usePF2PAT function needs it to work, is deleted immediately afterwards
    process.out = cms.OutputModule("PoolOutputModule",
                                   fileName = cms.untracked.string('dummyFile.root'),
                                   outputCommands = cms.untracked.vstring('drop *')
                                   )

    ## run the full PF2PAT sequence
    from PhysicsTools.PatAlgos.tools.pfTools import usePF2PAT
    usePF2PAT( process
             , runPF2PAT      = True
             , runOnMC        = options['runOnMC']
             , jetAlgo        = 'AK5'
             , postfix        = postfix
             , jetCorrections = ( 'AK5PFchs'
                                , cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute'])
                                )
             )
   
    delattr(process,'out')

    ##
    ## customize PAT
    ##

    from PhysicsTools.PatAlgos.tools.coreTools import removeSpecificPATObjects, removeCleaning
    removeSpecificPATObjects(process, ['Taus', 'Photons'], False, postfix)
    removeCleaning(process, False, postfix)

    ## in case of postfix the pfPileUp and pfNoPileUp collections may not get one
    from PhysicsTools.PatAlgos.tools.helpers import massSearchReplaceAnyInputTag
    massSearchReplaceAnyInputTag(getattr( process, 'patPF2PATSequence' + postfix), 'pfPileUp'   + postfix, 'pfPileUp')
    massSearchReplaceAnyInputTag(getattr( process, 'patPF2PATSequence' + postfix), 'pfNoPileUp' + postfix, 'pfNoPileUp')

    ## make selection for the pf candidates
    from TopAnalysis.TopUtils.particleFlowSetup_cff import pfSelectedChargedHadrons, pfSelectedNeutralHadrons, pfSelectedPhotons

    setattr(process, 'pfSelectedChargedHadrons'+postfix, pfSelectedChargedHadrons.clone())
    setattr(process, 'pfSelectedNeutralHadrons'+postfix, pfSelectedNeutralHadrons.clone())
    setattr(process, 'pfSelectedPhotons'       +postfix, pfSelectedPhotons.clone()       )

    ## add selected pf candidates to the sequence
    getattr(process, 'patPF2PATSequence' + postfix).replace(getattr(process,'pfAllPhotons'+postfix),
                                                            getattr(process,'pfAllPhotons'+postfix)*
                                                            getattr(process,'pfSelectedChargedHadrons'+postfix)*
                                                            getattr(process,'pfSelectedNeutralHadrons'+postfix)*
                                                            getattr(process,'pfSelectedPhotons'+postfix)
                                                            )

    ## removal of unnecessary modules
    getattr(process, 'patPF2PATSequence' + postfix).remove(getattr(process,'patPFParticles'+postfix))
    getattr(process, 'patPF2PATSequence' + postfix).remove(getattr(process,'patCandidateSummary'+postfix))

    getattr(process, 'patPF2PATSequence' + postfix).remove(getattr(process,'selectedPatPFParticles'+postfix))
    getattr(process, 'patPF2PATSequence' + postfix).remove(getattr(process,'selectedPatCandidateSummary'+postfix))
    getattr(process, 'patPF2PATSequence' + postfix).remove(getattr(process,'countPatElectrons'+postfix))
    getattr(process, 'patPF2PATSequence' + postfix).remove(getattr(process,'countPatMuons'+postfix))
    getattr(process, 'patPF2PATSequence' + postfix).remove(getattr(process,'countPatLeptons'+postfix))
    getattr(process, 'patPF2PATSequence' + postfix).remove(getattr(process,'countPatJets'+postfix))
    getattr(process, 'patPF2PATSequence' + postfix).remove(getattr(process,'countPatPFParticles'+postfix))

    ## embedding of resolutions into the patObjects
    process.load("TopQuarkAnalysis.TopObjectResolutions.stringResolutions_etEtaPhi_cff")


    ##
    ## customize muons
    ##

    ## switch muons to be originating from the primary vertex
    getattr(process, 'pfSelectedMuons'+postfix).src = 'pfMuonsFromVertex'+postfix

    ## apply selection for muons
    getattr(process, 'pfSelectedMuons'+postfix).cut = options['cutsMuon']

    ## calculate isolation only for (kinematically) selected pfMuons
    getattr(process,'isoDepMuonWithCharged'+postfix).src = 'pfSelectedMuons'+postfix
    getattr(process,'isoDepMuonWithNeutral'+postfix).src = 'pfSelectedMuons'+postfix
    getattr(process,'isoDepMuonWithPhotons'+postfix).src = 'pfSelectedMuons'+postfix
    ## calculate isolation only based on selected pfCandidates
    getattr(process,'isoDepMuonWithCharged'+postfix).ExtractorPSet.inputCandView = 'pfSelectedChargedHadrons'
    getattr(process,'isoDepMuonWithNeutral'+postfix).ExtractorPSet.inputCandView = 'pfSelectedNeutralHadrons'
    getattr(process,'isoDepMuonWithPhotons'+postfix).ExtractorPSet.inputCandView = 'pfSelectedPhotons'

    ## adapt isolation cone for muons
    getattr(process,"isoValMuonWithNeutral"+postfix).deposits[0].deltaR = cms.double(options['pfIsoConeMuon'])
    getattr(process,"isoValMuonWithCharged"+postfix).deposits[0].deltaR = cms.double(options['pfIsoConeMuon'])
    getattr(process,"isoValMuonWithPhotons"+postfix).deposits[0].deltaR = cms.double(options['pfIsoConeMuon'])
    
    ## adapt isolation cut
    getattr(process, 'pfIsolatedMuons'+postfix).combinedIsolationCut = options['pfIsoValMuon']
    
    ## use beamspot for dB calculation
    getattr(process, 'patMuons'+postfix).usePV = False
    
    ## embedding of resolutions into the patObjects
    process.patMuons.addResolutions = True
    process.patMuons.resolutions = cms.PSet( default = cms.string("muonResolution") )

    ##
    ## customize electrons
    ##

    ## add CiC electron ID
    process.load('RecoEgamma.ElectronIdentification.cutsInCategoriesElectronIdentificationV06_cfi')
    process.eidCiCSequence = cms.Sequence(
        process.eidVeryLooseMC  *
        process.eidLooseMC      *
        process.eidMediumMC     *
        process.eidTightMC      *
        process.eidSuperTightMC *
        process.eidHyperTight1MC
        )

    ## embed CiC electron ID into patElectrons
    getattr(process,'patElectrons'+postfix).electronIDSources = cms.PSet(
        eidVeryLooseMC   = cms.InputTag("eidVeryLooseMC"),
        eidLooseMC       = cms.InputTag("eidLooseMC"),
        eidMediumMC      = cms.InputTag("eidMediumMC"),
        eidTightMC       = cms.InputTag("eidTightMC"),
        eidSuperTightMC  = cms.InputTag("eidSuperTightMC"),
        eidHyperTight1MC = cms.InputTag("eidHyperTight1MC")
        )

    ## switch input of pfElectrons to collection without muons
    getattr(process,'pfAllElectrons'+postfix).src = 'pfNoMuon'+postfix

    ## switch muons to be originating from the primary vertex
    getattr(process, 'pfSelectedElectrons'+postfix).src = 'pfElectronsFromVertex'+postfix

    ## apply selection for electrons (they are the source of the pat::electrons)
    getattr(process,'pfSelectedElectrons'+postfix).cut = options['cutsElec']

    ## calculate isolation only for (kinematically) selected pfElectrons
    getattr(process,'isoDepElectronWithCharged'+postfix).src = 'pfSelectedElectrons'+postfix
    getattr(process,'isoDepElectronWithNeutral'+postfix).src = 'pfSelectedElectrons'+postfix
    getattr(process,'isoDepElectronWithPhotons'+postfix).src = 'pfSelectedElectrons'+postfix
    ## calculate isolation only based on selected pfCandidates
    getattr(process,'isoDepElectronWithCharged'+postfix).ExtractorPSet.inputCandView = 'pfSelectedChargedHadrons'
    getattr(process,'isoDepElectronWithNeutral'+postfix).ExtractorPSet.inputCandView = 'pfSelectedNeutralHadrons'
    getattr(process,'isoDepElectronWithPhotons'+postfix).ExtractorPSet.inputCandView = 'pfSelectedPhotons'

    ## adapt isolation cone for electrons
    getattr(process,"isoValElectronWithNeutral"+postfix).deposits[0].deltaR = cms.double(options['pfIsoConeElec'])
    getattr(process,"isoValElectronWithCharged"+postfix).deposits[0].deltaR = cms.double(options['pfIsoConeElec'])
    getattr(process,"isoValElectronWithPhotons"+postfix).deposits[0].deltaR = cms.double(options['pfIsoConeElec'])

    ## adapt isolation cut
    getattr(process,'pfIsolatedElectrons'+postfix).combinedIsolationCut = options['pfIsoValElec']

    ## use beamspot for dB calculation
    getattr(process, 'patElectrons'+postfix).usePV = False

    ## embedding of resolutions into the patObjects
    process.patElectrons.addResolutions = True
    process.patElectrons.resolutions = cms.PSet( default = cms.string("elecResolution") )


    ##
    ## customize taus
    ##

    ## remove the full pftau sequence as it is not needed for us
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'pfTauPFJets08Region'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'pfTauPileUpVertices'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'pfTauTagInfoProducer'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'pfJetsPiZeros'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'pfJetsLegacyTaNCPiZeros'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'pfJetsLegacyHPSPiZeros'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'pfTausBase'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'pfTausBaseDiscriminationByLeadingTrackFinding'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'pfTausBaseDiscriminationByIsolation'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'pfTausBaseDiscriminationByLeadingPionPtCut'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'pfTaus'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'pfNoTau'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'shrinkingConePFTauDiscriminationByLeadingTrackFinding'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'shrinkingConePFTauDiscriminationByLeadingTrackPtCut'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'shrinkingConePFTauDiscriminationByLeadingPionPtCut'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'shrinkingConePFTauDiscriminationByIsolation'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'shrinkingConePFTauDiscriminationByTrackIsolation'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'shrinkingConePFTauDiscriminationByECALIsolation'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'shrinkingConePFTauDiscriminationByIsolationUsingLeadingPion'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'shrinkingConePFTauDiscriminationByTrackIsolationUsingLeadingPion'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'shrinkingConePFTauDiscriminationByECALIsolationUsingLeadingPion'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'shrinkingConePFTauDiscriminationAgainstElectron'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'shrinkingConePFTauDiscriminationAgainstMuon'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'shrinkingConePFTauDiscriminationByTaNC'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'shrinkingConePFTauDiscriminationByTaNCfrOnePercent'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'shrinkingConePFTauDiscriminationByTaNCfrHalfPercent'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'shrinkingConePFTauDiscriminationByTaNCfrQuarterPercent'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'shrinkingConePFTauDiscriminationByTaNCfrTenthPercent'+postfix))

    ##
    ## customize photons
    ##

    ## remove the photons match
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'photonMatch'+postfix))

    ##
    ## customize jets
    ##

    ## switchmodules to correct sources
    massSearchReplaceAnyInputTag(getattr( process, 'patPF2PATSequence' + postfix), 'pfNoTau' + postfix, 'pfJets' + postfix)

    ## remove soft lepton taggers, which would have needed more RECO collections as input
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'softMuonTagInfosAOD'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'softMuonBJetTagsAOD'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'softMuonByPtBJetTagsAOD'+postfix))
    getattr( process, 'patPF2PATSequence' + postfix).remove(getattr(process,'softMuonByIP3dBJetTagsAOD'+postfix))
    
    getattr(process,'patJets'+postfix).tagInfoSources = []
    getattr(process,'patJets'+postfix).discriminatorSources.remove(cms.InputTag("softMuonBJetTagsAOD"+postfix))
    getattr(process,'patJets'+postfix).discriminatorSources.remove(cms.InputTag("softMuonByPtBJetTagsAOD"+postfix))
    getattr(process,'patJets'+postfix).discriminatorSources.remove(cms.InputTag("softMuonByIP3dBJetTagsAOD"+postfix))
    
    ## embedding of resolutions into the patObjects
    process.patJets.addResolutions = True
    process.patJets.resolutions = cms.PSet(
        default = cms.string("udscResolutionPF"),
        bjets = cms.string("bjetResolutionPF"),
        )


    ##
    ## customize MET
    ##

    ## re-configure and create MET
    getattr(process,'pfMET'+postfix).src = 'pfNoPileUp'

    ## embedding of resolutions into the patObjects
    process.patMETs.addResolutions = True
    process.patMETs.resolutions = cms.PSet( default = cms.string("metResolutionPF") )

    ##
    ## let it run
    ##

    ## define sequence with all modules in
    process.pf2pat = cms.Sequence(
        process.goodOfflinePrimaryVertices *
        process.goodOfflinePrimaryVerticesWithBS *
        process.eidCiCSequence *
        getattr( process, 'patPF2PATSequence' + postfix)
        )

    ## add kt6PFJets for rho calculation needed for L1FastJet correction
    process.pf2pat.replace( getattr(process,'patJetCorrFactors'+postfix)
                          , process.kt6PFJets * getattr(process,'patJetCorrFactors'+postfix)
                          )

    ##
    ## output all options and set defaults
    ##

    print '==================================================='
    print '|||||||||||||||||||||||||||||||||||||||||||||||||||'
    print '==================================================='
    print 'options used by prependPF2PATSequence:'
    print 'runOnMC:', options.setdefault('runOnMC', True)
    #print 'postfix:', options.setdefault('postfix', '')
    print 'runOnOLDcfg:', options['runOnOLDcfg']
    print 'cutsMuon:', options['cutsMuon']
    print 'cutsElec:', options['cutsElec']
    print 'pfIsoConeMuon:', options['pfIsoConeMuon']
    print 'pfIsoConeElec:', options['pfIsoConeElec']
    print 'pfIsoValMuon:', options['pfIsoValMuon']
    print 'pfIsoValElec:', options['pfIsoValElec']
    print '==================================================='
    print '|||||||||||||||||||||||||||||||||||||||||||||||||||'
    print '==================================================='

    ## append pf2pat sequence to all paths in pathnames
    if pathnames == ['']:
        pathnames = process.paths_().keys()

    print 'prepending PF2PAT sequence to paths:', pathnames
    for pathname in pathnames:
        ## use only good vertices
        massSearchReplaceAnyInputTag(process.pf2pat, 'offlinePrimaryVertices'      , 'goodOfflinePrimaryVertices')
        massSearchReplaceAnyInputTag(process.pf2pat, 'offlinePrimaryVerticesWithBS', 'goodOfflinePrimaryVerticesWithBS')
        process.goodOfflinePrimaryVertices.src       = 'offlinePrimaryVertices'
        process.goodOfflinePrimaryVerticesWithBS.src = 'offlinePrimaryVerticesWithBS'
        massSearchReplaceAnyInputTag(getattr(process,pathname), 'offlinePrimaryVertices'      , 'goodOfflinePrimaryVertices')
        massSearchReplaceAnyInputTag(getattr(process,pathname), 'offlinePrimaryVerticesWithBS', 'goodOfflinePrimaryVerticesWithBS')
        
        ## replace everything from the old selection with the newly generated collections
        if options['runOnOLDcfg']:
            massSearchReplaceAnyInputTag(getattr(process,pathname), 'selectedPatJetsAK5PF', 'selectedPatJets')
            massSearchReplaceAnyInputTag(getattr(process,pathname), 'patMETsPF', 'patMETs')
            massSearchReplaceAnyInputTag(getattr(process,pathname), cms.InputTag('scaledJetEnergy', 'selectedPatJetsAK5PF', process.name_()), cms.InputTag('scaledJetEnergy', 'selectedPatJets', process.name_()))

        ## finaly insert the sequence into all (given) paths
        getattr(process, pathname).insert(0,process.pf2pat)

    if 'postfix' in options:
        print 'POSTFIXES ARE NOT SUPPORTED AT THE MOMENT, THIS OPTION IS IGNORED'
