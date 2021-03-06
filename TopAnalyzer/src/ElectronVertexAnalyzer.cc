#include "TopAnalysis/TopAnalyzer/interface/ElectronVertexAnalyzer.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Utilities/interface/EDMException.h"
#include <TopAnalysis/TopAnalyzer/interface/PUEventWeight.h>



ElectronVertexAnalyzer::ElectronVertexAnalyzer(const ParameterSet& cfg)
{
  vertices_ = cfg.getParameter<InputTag>    ("vertices" );
  electrons_= cfg.getParameter<InputTag>    ("electrons");
  beamspot_ = cfg.getParameter<InputTag>    ("beamspot" );
  ndof_     = cfg.getParameter<unsigned int>("ndof"     );
  rho_      = cfg.getParameter<double>      ("rho"      );
  z_        = cfg.getParameter<double>      ("z"        );
  weight_   = cfg.getParameter<InputTag>("weight");
}

ElectronVertexAnalyzer::~ElectronVertexAnalyzer()
{
}

void
ElectronVertexAnalyzer::beginJob()
{
  edm::Service<TFileService> fs;
  if( !fs ){
    throw edm::Exception( edm::errors::Configuration,
                          "TFile Service is not registered in cfg file" );
  }

  multi_= fs->make<TH1D>( "multi", "N of Vertices", 10,-0.5,9.5);
  multi_->GetXaxis()->SetTitle("N_{vrtcs}");
  multi_->GetYaxis()->SetTitle("N");

  goodMulti_= fs->make<TH1D>( "goodMulti", "N of good Vertices", 10,-0.5,9.5);
  goodMulti_->GetXaxis()->SetTitle("N_{vrtcs}");
  goodMulti_->GetYaxis()->SetTitle("N");


  posX_= fs->make<TH1D>( "posX", "Vertex x-Position", 400,-2.,2.);
  posX_->GetXaxis()->SetTitle("x [cm]");
  posX_->GetYaxis()->SetTitle("N / 0.01cm");

  posY_= fs->make<TH1D>( "posY", "Vertex y-Position", 400,-2.,2.);
  posY_->GetXaxis()->SetTitle("y [cm]");
  posY_->GetYaxis()->SetTitle("N / 0.01cm");

  posZ_= fs->make<TH1D>( "posZ", "Vertex z-Position", 1000,-50.,50.);
  posZ_->GetXaxis()->SetTitle("z [cm]");
  posZ_->GetYaxis()->SetTitle("N / 0.1cm");

  posRho_= fs->make<TH1D>( "posRho", "Vertex #rho-Position", 500,-2.5,2.5);
  posRho_->GetXaxis()->SetTitle("#rho [cm]");
  posRho_->GetYaxis()->SetTitle("N / 0.01cm");


  posXerr_= fs->make<TH1D>( "posXerr", "Vertex x-Position Error", 100,0.,1.);
  posXerr_->GetXaxis()->SetTitle("#delta x [cm]");
  posXerr_->GetYaxis()->SetTitle("N / 0.01cm");

  posYerr_= fs->make<TH1D>( "posYerr", "Vertex y-Position Error", 100,0.,1.);
  posYerr_->GetXaxis()->SetTitle("#delta y [cm]");
  posYerr_->GetYaxis()->SetTitle("N / 0.01cm");

  posZerr_= fs->make<TH1D>( "posZerr", "Vertex z-Position Error", 100,0.,1.);
  posZerr_->GetXaxis()->SetTitle("#delta z [cm]");
  posZerr_->GetYaxis()->SetTitle("N / 0.01cm");


  nTracks_= fs->make<TH1D>( "nTracks", "Number of Tracks at Vertex", 200,0,200);
  nTracks_->GetXaxis()->SetTitle("N_{tracks}");
  nTracks_->GetYaxis()->SetTitle("N");

  nDof_= fs->make<TH1D>( "nDof", "N_{dof} at Vertex", 200,0,200);
  nDof_->GetXaxis()->SetTitle("N_{dof}");
  nDof_->GetYaxis()->SetTitle("N");

  chi2_= fs->make<TH1D>( "chi2", "#chi^2 of Vertices", 200,0,200);
  chi2_->GetXaxis()->SetTitle("#chi^2");
  chi2_->GetYaxis()->SetTitle("N");

  nchi2_= fs->make<TH1D>( "nchi2", "#chi^2/N_{dof} of Vertices", 200,0,20);
  nchi2_->GetXaxis()->SetTitle("#chi^2/N_{dof}");
  nchi2_->GetYaxis()->SetTitle("N");

  dzEl_= fs->make<TH1D>( "dzEl", "z-Distance el,Vrtx", 200,0,20);
  dzEl_->GetXaxis()->SetTitle("#Delta z [cm]");
  dzEl_->GetYaxis()->SetTitle("N");

  dxyEl_= fs->make<TH1D>( "dxyEl", "xy-Distance el,Vrtx", 400,0.,2.);
  dxyEl_->GetXaxis()->SetTitle("#Delta xy [cm]");
  dxyEl_->GetYaxis()->SetTitle("N");

  position3D_= fs->make<TH3D>( "position3D", "Position of good Vertices", 1000,-50.,50.,100,-5.,5.,100,-5.,5.);
  position3D_->GetXaxis()->SetTitle("z [cm]"); // this is NO typo!
  position3D_->GetYaxis()->SetTitle("x [cm]");
  position3D_->GetZaxis()->SetTitle("y [cm]");
}

void
ElectronVertexAnalyzer::analyze(const Event& evt, const EventSetup&)
{
  double weight = getPUEventWeight(evt, weight_);
  Handle<std::vector<reco::Vertex> > vertices;
  evt.getByLabel(vertices_, vertices);

  multi_->Fill(vertices->size(), weight);

  int i=0;
  for(VertexCollection::const_iterator vrtx = vertices->begin(); vrtx!= vertices->end(); ++vrtx) {

    bool isFake = vrtx->isFake();
    unsigned int ndof    = vrtx->ndof();
    unsigned int ntracks = vrtx->tracksSize();
    double rho  = vrtx->position().rho();
    double z    = vrtx->position().z();
    double chi2 = vrtx->chi2();
    double nchi2= chi2/ndof;

    if(!isFake && ndof>ndof_ && fabs(z)<z_ && rho<rho_){
      i++;

      posX_  ->Fill(vrtx->x(), weight);
      posY_  ->Fill(vrtx->y(), weight);
      posZ_  ->Fill(z, weight);
      posRho_->Fill(rho, weight);

      posXerr_->Fill(vrtx->xError(), weight);
      posYerr_->Fill(vrtx->yError(), weight);
      posZerr_->Fill(vrtx->zError(), weight);

      nTracks_->Fill(ntracks, weight);
      nDof_   ->Fill(ndof, weight);
      chi2_   ->Fill(chi2, weight);
      nchi2_  ->Fill(nchi2, weight);

      position3D_->Fill(vrtx->z(),vrtx->x(),vrtx->y(), weight); // this is NO typo!

      Handle<std::vector<pat::Electron> > electrons;
      evt.getByLabel(electrons_, electrons);

      Handle<reco::BeamSpot> pBeamSpot;
      evt.getByLabel(beamspot_, pBeamSpot);


      for(std::vector<pat::Electron>::const_iterator electron = electrons->begin(); electron!= electrons->end(); ++electron) {
        dzEl_->Fill(fabs(electron->vz()-z), weight);

        // TO BE FIXED
        double ip=-999.;
        if (pBeamSpot.isValid()) {
          const reco::BeamSpot *bspot = pBeamSpot.product();
          const math::XYZPoint bspotPosition = bspot->position();
          ip = fabs(electron->gsfTrack()->dxy(bspotPosition));
        }  else
          ip = fabs(electron->gsfTrack()->dxy());
        dxyEl_->Fill(ip, weight);
      }

    }
  }
  goodMulti_->Fill(i, weight);
}

void
ElectronVertexAnalyzer::endJob()
{
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE( ElectronVertexAnalyzer );
