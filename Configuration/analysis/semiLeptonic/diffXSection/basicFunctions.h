#ifndef basicFunctions_h
#define basicFunctions_h

#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <cstring>
#include <map>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <math.h>

#include <TH1F.h>
#include <TH2F.h>
#include <TGraphErrors.h>
#include <THStack.h>
#include <TROOT.h>
#include <TFile.h>
#include <TCanvas.h>
#include <TLegend.h>
#include <TKey.h>
#include <TGraphAsymmErrors.h>

#include <TLine.h>
#include <TBox.h>
#include <TPaveLabel.h>
#include <TStyle.h>
#include <typeinfo>
#include <TF1.h>
#include <TBox.h>
#include <TGaxis.h>
#include <TError.h>

                 /*0:*/  /*1:*/  /*2:*/    /*3:*/    /*4:*/   /*5:*/    /*6:*/  /*7:*/  /*8,  9,  10*/ /* 11   ,  12     ,   13:  */
enum samples    {kSig  , kBkg  , kZjets  , kWjets  , kQCD   , kSTop   , kDiBos, kData , kWW, kWZ, kZZ, kSTops  , kSTopt  , kSToptW };
int color_ [] = {kRed+1, kRed-7, kAzure-2, kGreen-3, kYellow, kMagenta, 10    , kBlack, 10 , 10 , 10 , kMagenta, kMagenta, kMagenta};
int marker_[] = {20    , 22    , 29      , 23      , 21     , 27      , 28    , 20    , 28 , 28 , 28 , 27      , 27      , 27      };
enum systematicVariation {/* 0:*/sysNo          , /* 1:*/sysLumiUp       , /* 2:*/sysLumiDown       , /* 3:*/sysJESUp     , 
			  /* 4:*/sysJESDown     , /* 5:*/sysJERUp        , /* 6:*/sysJERDown        , /* 7:*/sysTopScaleUp, 
			  /* 8:*/sysTopScaleDown, /* 9:*/sysVBosonScaleUp, /*10:*/sysVBosonScaleDown, /*11:*/sysTopMatchUp, 
			  /*12:*/sysTopMatchDown, /*13:*/sysVBosonMatchUp, /*14:*/sysVBosonMatchDown, /*15:*/sysMuEffSFup , 
			  /*16:*/sysMuEffSFdown , /*17:*/sysISRFSRup     , /*18:*/sysISRFSRdown     , /*19:*/sysPileUp    ,
			  /*20:*/sysQCDup       , /*21:*/sysQCDdown      , /*22:*/sysSTopUp         , /*23:*/sysSTopDown  ,
			  /*24:*/sysBtagUp      , /*25:*/sysBtagDown     , /*26:*/sysDiBosUp        , /*27:*/sysDiBosDown};

bool newSpring11MC=true;
TString sysLabel(unsigned int sys)
{
  // this function returns a TString that corresponds 
  // to the systematic variation "sys" of the enumerator "systematicVariation"
  // modified quantities: none
  // used functions: none
  // used enumerators: none (label correspond to systematicVariation)

  TString systematicVariationlabel="";
  if(sys==0 )systematicVariationlabel="sysNo";
  if(sys==1 )systematicVariationlabel="sysLumiUp";
  if(sys==2 )systematicVariationlabel="sysLumiDown";
  if(sys==3 )systematicVariationlabel="sysJESUp";
  if(sys==4 )systematicVariationlabel="sysJESDown";
  if(sys==5 )systematicVariationlabel="sysJERUp";
  if(sys==6 )systematicVariationlabel="sysJERDown";
  if(sys==7 )systematicVariationlabel="sysTopScaleUp";
  if(sys==8 )systematicVariationlabel="sysTopScaleDown";
  if(sys==9 )systematicVariationlabel="sysVBosonScaleUp";
  if(sys==10)systematicVariationlabel="sysVBosonScaleDown";
  if(sys==11)systematicVariationlabel="sysTopMatchUp";
  if(sys==12)systematicVariationlabel="sysTopMatchDown";
  if(sys==13)systematicVariationlabel="sysVBosonMatchUp";
  if(sys==14)systematicVariationlabel="sysVBosonMatchDown";
  if(sys==15)systematicVariationlabel="sysMuEffSFup";
  if(sys==16)systematicVariationlabel="sysMuEffSFdown";
  if(sys==17)systematicVariationlabel="sysISRFSRup";
  if(sys==18)systematicVariationlabel="sysISRFSRdown";
  if(sys==19)systematicVariationlabel="sysPileUp";
  if(sys==20)systematicVariationlabel="sysQCDup";
  if(sys==21)systematicVariationlabel="sysQCDdown";
  if(sys==22)systematicVariationlabel="sysSTopUp";
  if(sys==23)systematicVariationlabel="sysSTopDown";
  if(sys==24)systematicVariationlabel="btagEffUp";
  if(sys==25)systematicVariationlabel="btagEffDown";
  if(sys==26)systematicVariationlabel="sysDiBosUp";
  if(sys==27)systematicVariationlabel="sysDiBosDown";
  // check if valid input was chosen
  if(systematicVariationlabel==""){
    std::cout << "ERROR: the chosen input for function sysLabel is not valid" << std::endl;
    std::cout << "max syst. variation: 20" << std::endl;
    std::cout << "max syst. variation: " << sys << std::endl;
    exit(1);
  }
  return systematicVariationlabel;
}

double effSFAB(int sys=sysNo, std::string decayChannel="unset")
{
  // this function returns the muon eff SF 
  // as derived from Z->mumu tag and probe method
  // modified quantities: NONE
  // used functions: NONE
  // used enumerators: NONE
  // "sys": if sysMuEffSFup/sysMuEffSFdown is
  // chosen, the corresponding systematic shifted
  // SF is returned

  // combined single muon SF Run A+B from tag and probe
  double result = -1.;
  if (decayChannel.compare("muon")==0) {
    result = 0.964155;
    if(newSpring11MC) result = 0.9581;
  } else if (decayChannel.compare("electron")==0) {
    result = 1.0;                   // TO BE DERIVED
    if(newSpring11MC) result = 1.0; // TO BE DERIVED
  }
  // errors for the derived SF
  double errorUp   = 0.03*result;
  double errorDown = 0.03*result;
  // return requestet SF
  if(sys==sysMuEffSFup  ) result+=errorUp;
  if(sys==sysMuEffSFdown) result-=errorDown;
  return result;
}

// BR correction for ttbar->lnuqq'bb'
double BRcorrectionSemileptonic = 0.985608;

void histogramStyle(TH1& hist, int sampleTyp, bool filled=true, double markersize=1.8, unsigned int color=0) 
{
  // this function configures the style of a TH1 histogram "hist"
  // using "sampleTyp" to identify the corresponding sample from
  // the enumerator samples definition and assign the corresponding
  // marker and color
  // modified quantities: hist
  // used functions: marker_, color_
  // used enumerators: samples
  // "filled": = 0: line only, =1: area under plot filled

  hist.SetStats(kFALSE);
  hist.SetLineWidth(1);
  hist.SetLineStyle(1);
  if(sampleTyp==kData || !filled){
    if(!filled)hist.SetLineWidth(3);
    hist.SetLineColor(color_[sampleTyp]);
    hist.SetMarkerColor(color_[sampleTyp]);
    if(sampleTyp==kQCD){
      hist.SetLineColor(kYellow+1);
      hist.SetMarkerColor(kYellow+1);
    }
    if(sampleTyp==kDiBos){
      hist.SetLineColor(kGray);
      hist.SetMarkerColor(kGray);
    }
    hist.SetMarkerStyle(marker_[sampleTyp]);
    hist.SetMarkerSize(markersize);
    hist.SetFillStyle(0);
  }
  else{
    hist.SetLineColor(kBlack);
    hist.SetFillColor(color_[sampleTyp]);
    hist.SetFillStyle(1001);
  }
  if(color!=0){
    hist.SetLineColor(color);
    hist.SetFillColor(color);
  }

}

void histStyle2D(TH2& hist, const TString titleHisto, const TString titleX, const TString titleY) 
{
  // this function configures the style of a TH2 histogram "hist"
  // modified quantities: hist
  // used functions: NONE
  // used enumerators: NONE
  // "titleHisto": set tite of the histo (drawn in upper left)
  // "titleX": title of the x-axis
  // "titleY": title of the y-axis

  hist.SetTitle(titleHisto);
  if(titleX!="") hist.GetXaxis()->SetTitle(titleX);
  hist.GetXaxis()->SetTitleSize ( 0.05 );
  hist.GetXaxis()->SetLabelColor(  1   );
  hist.GetXaxis()->SetLabelFont ( 62   );
  hist.GetXaxis()->SetLabelSize ( 0.04 );
  hist.GetXaxis()->SetNdivisions(  505 );
  hist.GetXaxis()->CenterTitle  ( true );
  if(titleY!="") hist.GetYaxis()->SetTitle(titleY);
  hist.GetYaxis()->SetTitleSize  ( 0.05 );
  hist.GetYaxis()->SetTitleColor (    1 );
  hist.GetYaxis()->SetTitleOffset(  1.1 );
  hist.GetYaxis()->SetTitleFont  (   62 );
  hist.GetYaxis()->SetLabelSize  ( 0.04 );
  hist.GetYaxis()->SetLabelFont  (   62 );
  hist.GetYaxis()->SetNdivisions (  505 );
  hist.GetYaxis()->CenterTitle   ( true );
  hist.SetStats(kFALSE);
}

double readLineFromFile(int line, TString file="crossSectionCalculation.txt")
{
  // this function to reads and returns a double value 
  // from a specific line "line" of the .txt-like file "file"
  // modified quantities: NONE
  // used functions: NONE
  // used enumerators: NONE

  // define variables
  std::ifstream finDouble (file);
  std::string readIn;
  // check if file exists
  if (!finDouble){
    std::cout << "can not open file " << file << std::endl;
    return -1;
  }
  // loop lines of the file
  for(int l=1; !finDouble.eof(); ++l){
    // save line content in readIn
    getline(finDouble, readIn);
    // convert your chosen line into double and return it
    if(l==line) return atof(readIn.c_str()); 
  }
  // if line is not found
  std::cout << "can not find line" << line << std::endl;
  return -1.;  
}

void canvasStyle(TCanvas& canv)
{
  // this function does the standard style 
  // configuration for the TCanvas "canv"
  // modified quantities: canv
  // used functions: NONE
  // used enumerators: NONE

  canv.SetFillStyle   ( 4000 );
  canv.SetLeftMargin  ( 0.20 );
  canv.SetRightMargin ( 0.05 );
  canv.SetBottomMargin( 0.15 );
  canv.SetTopMargin   ( 0.05 );
}

void axesStyle(TH1& hist, const char* titleX, const char* titleY, float yMin=-123, float yMax=-123, float titleSize=0.05, float yTitleOffset=1.2, float labelSize = 0.05)
{
  // this function configures the axis style of a TH1 histogram "hist"
  // modified quantities: hist
  // used functions: NONE
  // used enumerators: NONE
  // "titleX": title of the x-axis
  // "titleY": title of the y-axis
  // "yMin": minimum of the y axis
  // "yMax": maximum of the y axis
  // "yTitleSize": caption size of the y axis title
  // "yTitleOffset": offste of the y axis title
  // "xLabelSize": caption size of the y axis label

  hist.SetTitle("");
  hist.GetXaxis()->SetTitle(titleX);
  //hist.GetXaxis()->CenterTitle();
  hist.GetXaxis()->SetTitleSize  (titleSize);
  hist.GetXaxis()->SetTitleColor (1);
  hist.GetXaxis()->SetTitleOffset(1.1);
  hist.GetXaxis()->SetTitleFont  (62);
  hist.GetXaxis()->SetLabelSize  (labelSize);
  hist.GetXaxis()->SetLabelFont  (62);
  hist.GetXaxis()->SetNdivisions (505);
  hist.GetYaxis()->SetTitle(titleY);
  hist.GetYaxis()->SetTitleSize  (titleSize);
  hist.GetYaxis()->SetTitleColor (1);
  hist.GetYaxis()->SetTitleOffset(yTitleOffset);
  hist.GetYaxis()->SetTitleFont  (62);
  hist.GetYaxis()->SetLabelSize  (labelSize);
  hist.GetYaxis()->SetLabelFont  (62);
  //hist.GetYaxis()->CenterTitle   ( true);
  if(yMin!=-123) hist.SetMinimum(yMin);
  if(yMax!=-123) hist.SetMaximum(yMax);
}

template <class T>
void writeToFile(T output, TString file, bool append)
{
  // this function writes the content of "output"
  // into "file" which is of a type like .txt
  // "output" might be of type TString or double
  // modified quantities: file
  // used functions: NONE
  // used enumerators: NONE
  // "append": if false, "file" will be recreated and 
  // the existing "file" will be deleted

  // a) write into file
  if(!append){
    std::ofstream fout(file);
    fout << output << std::endl;
    fout.close();
  }
  // b) add output to the end of the file  
  if(append){
    std::ofstream fapp(file, ios::app);
    fapp << output << std::endl;;
    fapp.close();
  }
 }

void drawLine(const double xmin, const double ymin, const double xmax, const double ymax, const unsigned int color=kBlack, const double lineWidth=3.0, const unsigned int lineStyle=1)
{
  // this function draws a line withe the chosen coordinates, 
  // color and width into the active canvas
  // modified quantities: NONE
  // used functions: NONE
  // used enumerators: NONE
  TLine *line = new TLine();
  line->SetLineWidth(lineWidth);
  line->SetLineStyle(lineStyle);
  line->SetLineColor(color);
  line->DrawLine(xmin, ymin, xmax, ymax);
}

int roundToInt(double value, bool roundDown=false)
{
  // function to round an double "value" 
  // to an int and return this one
  // modified quantities: NONE
  // used functions: NONE
  // used enumerators: NONE
  // "roundDown": choose if you always want to round down

  // create output
  int outputInt=0;
  // take care of negative numbers
  if(value<0){
    std::cout << "no negative numbers allowed in roundToInt" << std::endl;
    return 0;
  }
  // get number before the digit
  for(int x=0; value>x; ++x){
    outputInt=x;
  }
  // see if the number behind the digit is > 0.5
  if((roundDown==false)&&(value-outputInt) >=0.5) return (outputInt+1);
  // return result
  return outputInt;
}

TString getTStringFromInt(int i)
{
  // function to convert an int "i" to 
  // a TString and return this one
  // modified quantities: NONE
  // used functions: NONE
  // used enumerators: NONE
  char result[20];
  sprintf(result, "%i", i);
  return (TString)result;
}

TString sampleLabel(unsigned int sample, const std::string decayChannel, bool TwoThousandEleven=false)
{
  // this function returns the name of the entered MC process
  // corresponding to the enumerator entry "sample" as defined in samples
  // modified quantities: NONE
  // used functions: NONE
  // used enumerators: samples

  // create output
  TString MCprocess;
  // list all MC process/sample names
  if(sample==kSig && decayChannel.compare("electron")==0) MCprocess="t#bar{t} (e prompt)";
  if(sample==kSig && decayChannel.compare("muon"    )==0) MCprocess="t#bar{t} (#mu prompt)";
  if(sample==kBkg    ) MCprocess="t#bar{t} other";
  if(sample==kSTop   ) MCprocess="single top";
  if(sample==kSToptW ) MCprocess="single top tW";
  if(sample==kSTops  ) MCprocess="single top s";
  if(sample==kSTopt  ) MCprocess="single top t";
  if(sample==kWjets  ) MCprocess="W+jets";
  if(sample==kZjets  ) MCprocess="Z+jets";
  if(sample==kDiBos  ) MCprocess="DiBoson";
  if(sample==kWW     ) MCprocess="WW";
  if(sample==kWZ     ) MCprocess="WZ";
  if(sample==kZZ     ) MCprocess="ZZ";
  if(sample==kQCD    ) MCprocess="QCD";
  if(sample==kData&&!TwoThousandEleven) MCprocess="2010 data";
  if(sample==kData&& TwoThousandEleven) MCprocess="2011 data";
  // return result
  return MCprocess;
}

TH1F* divideByBinwidth(TH1F* histo, bool calculateError=true)
{
  // function divides the #entries in every bin of the input plot "histo" 
  // by its binwidth and returns the result
  // the errors are recalculated if "calculateError"=1 is choosen
  // careful: not done for underflow/overflow
  // modified quantities: NONE
  // used functions: NONE
  // used enumerators: NONE

  // create output histo
  TH1F* outputHisto = (TH1F*)histo->Clone();
  // loop bins, excluding underflow and overflow
  for(int i=1; i<= histo->GetNbinsX(); i++){
    double binwidth=(double)(histo->GetBinWidth(i));
    // take care of bins width width 0
    // (these could not be filled and 
    // exist because of technical reasons only)
    if(binwidth!=0){
      // recalculate error
      double error = (double)(histo->GetBinError(i)) / binwidth;
      // recalculate bin content
      outputHisto->SetBinContent(i, ( (double)(histo->GetBinContent(i)) / binwidth) );
      if(calculateError) outputHisto->SetBinError(i, error);
    }
  }
  // return result
  return outputHisto;
}

void DrawLabel(TString text, const double x1, const double y1, const double x2, const double y2, double textSize=0)
{
  // function to directly draw a label into the active canvas
  // the coordinates of the window are: "x1", "y1", "x2", "y2"
  // the label will contain the text "text" and the textsize is "textSize"
  // modified quantities: the active canvas
  // used functions: NONE
  // used enumerators: NONE

  TPaveLabel *label = new TPaveLabel(x1, y1, x2, y2, text, "br NDC");
  label->SetFillStyle(0);
  label->SetBorderSize(0);
  if(textSize!=0) label->SetTextSize(textSize);
  label->SetTextAlign(12);
  label->Draw("same");
}

void scaleByFactor(TH1F*& histo, const double scaleValue)
{
  // function to scale the TH1F plot "histo" and its errors 
  // by an entered "scaleValue" correctly for each bin 
  // N'=N/L, sN'=sN/L
  // modified quantities: histo
  // used functions: NONE
  // used enumerators: NONE

  // scaling factor = 0?
  if(scaleValue==0) std::cout << "WARNING: scaling histogram by 0" << std::endl;
  // loop bins (including underflow and overflow)
  for(int bin=0; bin<=histo->GetNbinsX()+1; ++bin){
    double oldError = histo->GetBinError(bin);
    // scale bin value and error
    histo->SetBinContent(bin, histo->GetBinContent(bin)/scaleValue);
    histo->SetBinError  (bin, oldError                 /scaleValue);
  }
}

double lumiweight(unsigned int sample, double luminosity, unsigned int kSys, const std::string decayChannel)
{
  // this function derives the lumiweight for every standard MC 
  // sample "sample" based on the theoretical cross section, the 
  // number of generated events and the chosen "luminosity"
  // Furthermore, the BR correction is considered for ttbar signal
  // NOTE: enter luminosity IN / pb!!!!
  // modified quantities: NONE
  // used functions: BRcorrectionSemileptonic
  // used enumerators: samples, systematicVariation

  // function internal detail level of text output
  unsigned int verbose=0;
  // a) check if input is valid
  // sample existing?
  if(sample>kSToptW){
    std::cout << "ERROR: invalid sample label for lumiweight calculation, no scaling will be done" << std::endl;
    return 1.;
  }
  // valid luminosity entered?
  if(luminosity<=0){
    std::cout << "ERROR: chosen luminosity for lumiweight calculation is <= 0, no scaling will be done" << std::endl;
    return 1.;
  }
  // valid decayChannel entered?
  if(!(decayChannel.compare("muon")==0 || decayChannel.compare("electron")==0)){
    std::cout << "ERROR: chosen decaychannel does not correspond to electron or muon, no scaling will be done" << std::endl;
    return 1.;
  }
  // b) define in/output for weight calculation
  double crossSection=1;
  double Nevents=0;
  double weight =0;

  // c) fill #events in sample and cross sections (in / pb)
  // 2*ttbar MADGRAPH D6T Fall10
  if((sample==kSig)||(sample==kBkg)){
    crossSection=157.5;
    Nevents     =1306182.;
    if(newSpring11MC) Nevents     = 1286491;
    // systematic samples:
    if(kSys==sysTopScaleUp  ) Nevents=1153236;
    if(kSys==sysTopScaleDown) Nevents=1098971;
    if(kSys==sysTopMatchUp  ) Nevents=1036492;
    if(kSys==sysTopMatchDown) Nevents=938005;
    if(kSys==sysISRFSRup    ) Nevents=1394010;
    if(kSys==sysISRFSRdown  ) Nevents=1221664;
    if(kSys==sysPileUp      ) Nevents=1281237;
  }
  // W->lnu+jets MADGRAPH D6T Fall10
  if(sample==kWjets){
    crossSection=31314.;
    Nevents     =14805546.;
    if(newSpring11MC) Nevents     =14722996;
    // systematic samples:
    if(kSys==sysVBosonScaleUp  ) Nevents=6118255;
    if(kSys==sysVBosonScaleDown) Nevents=4842219;
    if(kSys==sysVBosonMatchUp  ) Nevents=10370368;
    if(kSys==sysVBosonMatchDown) Nevents=2706986;
    if(kSys==sysPileUp         ) Nevents=14766396;
  }
  // DY->ll+jets MADGRAPH D6T Fall10
  if(sample==kZjets){
    crossSection=3048.;
    Nevents     =2543727.;
    if(newSpring11MC) Nevents     =2543706;
    // systematic samples:
    if(kSys==sysVBosonScaleUp  ) Nevents=1329028;
    if(kSys==sysVBosonScaleDown) Nevents=1436150;
    if(kSys==sysVBosonMatchUp  ) Nevents=1667367;
    if(kSys==sysVBosonMatchDown) Nevents=1662884;
    if(kSys==sysPileUp         ) Nevents=2539858;
  }
  // QCD PYTHIA6 Z2 Fall10 
  if(sample==kQCD){
    crossSection=296600000.*0.00028550; // generator crossSection * prefilter efficiency
    Nevents     =29504866.;
    if(newSpring11MC) Nevents     =29434562;
    // if(kSys==sysPileUp) Nevents=8063288; // PU not completely patified
  }
  // single top->lnu (added singleTop, s,t,tW channel) MADGRAPH Z2 Fall10 
  if(sample==kSTop){
    crossSection=1.;         // this leads to a weight
    Nevents     =luminosity; // of 1.0 as kSTop is already weighted
  }
  if(sample==kSTops){
    crossSection=4.6*0.108*3; // correct theory XSec for leptonic decay only
    Nevents     =494967.;
    if(newSpring11MC) Nevents     = 494967; 
    // systematic samples:
    if(kSys==sysPileUp)Nevents=494967;
  }
  if(sample==kSTopt){
    crossSection=64.6*0.108*3; // correct theory XSec for leptonic decay only
    Nevents     =484060.;
    if(newSpring11MC) Nevents     = 484060;
    // systematic samples:
    if(kSys==sysPileUp)Nevents=484060;
  }
  if(sample==kSToptW){
    crossSection=10.6;
    Nevents     =494961.;
    if(newSpring11MC) Nevents     =489417;
    // systematic samples:
    if(kSys==sysPileUp)Nevents=494961;
  }
  // DiBoson (added diboson,WW,WZ,ZZ) PYTHIA6 Z2 Fall10
  if(sample==kDiBos){
    crossSection=1.;         // this leads to a weight
    Nevents     =luminosity; // of 1.0 as kDiBos is already weighted
  }
  if(sample==kWW){
    crossSection=43.0;
    Nevents     =2061760;
    // systematic samples:
    if(kSys==sysPileUp)Nevents=2061760;
  }
  if(sample==kWZ){
    crossSection=18.2;
    Nevents     =2194752;
    // systematic samples:
    if(kSys==sysPileUp)Nevents=2185664;
  }
  if(sample==kZZ){
    crossSection=5.9;
    Nevents     =2113368;
    // systematic samples:
    if(kSys==sysPileUp)Nevents=2113368;
  }
  // Data 
  if(sample==kData){
    crossSection=1.;         // this leads to a weight
    Nevents     =luminosity; // of 1.0 as data needs no weight
  }
  // d) calculate weight

  weight = luminosity / ( Nevents / crossSection );
  if(verbose>0){
    std::cout << "sample: " << sampleLabel(sample,decayChannel) << std::endl;
    std::cout << "systematic var.: " << sysLabel(kSys) << std::endl;
  }
  // GOSSIE FIXME WRONG diboson and QCD samples, now scaled to zero on purpose 
  if (decayChannel.compare("electron")==0) { if(sample==kWW || sample==kWZ || sample==kZZ || sample==kQCD) { weight = 0. ; } }
  double weight2=weight;
  if(verbose>1) std::cout << "weight before scaling: " << weight2 << std::endl;
  // e) systematic effects
  // e1) for ttbar->lnu: BR correction
  if(sample==kSig) weight *= BRcorrectionSemileptonic;
  // e2) systematic higher/lower BG
  double scale=0;
  // (i) more/less DiBoson
  if(sample==kWW||sample==kWZ||sample==kZZ||sample==kDiBos){ 
    scale=0.3;
    if(kSys==sysDiBosUp  ) weight*=(1.0+scale);
    if(kSys==sysDiBosDown) weight*=(1.0-scale);
  }
  // (ii) more/less QCD
  if(sample==kQCD){
    scale=0.5;
    if(kSys==sysQCDup  ) weight*=(1.0+scale);
    if(kSys==sysQCDdown) weight*=(1.0-scale);
  }
  // (iii) more/less single top
  if(sample==kSTops||sample==kSTopt||sample==kSToptW||sample==kSTop){
    scale=0.3;
    if(kSys==sysSTopUp  ) weight*=(1.0+scale);
    if(kSys==sysSTopDown) weight*=(1.0-scale); 
  }
  if(scale!=0&&verbose>0) std::cout << "possible scale factor: " << scale << std::endl; 
  // return result
  if(verbose>0){
    std::cout << "weight";
    if(verbose>1){
      if(weight!=weight2) std::cout << "(scaled)";
      if(weight==weight2) std::cout << "(not scaled)"; 
    }      
    std::cout << ": " << weight << std::endl;
    if(verbose>1) std::cout << "ratio: " << weight/weight2 << std::endl;
    if(weight!=weight2&&sample==kSig) std::cout << "(BR correction applied)" << std::endl;
  }  
  return weight;
}

TString getStringEntry(const TString inputTString, unsigned int entry=42, const TString seperateBy="/")
{ 
  // this function devides "inputTString" using "seperateBy" 
  // as seperator and returns the "entry"-th element
  // 42: default, means last element after seperator
  // modified quantities: NONE
  // used functions: NONE
  // used enumerators: NONE
  char *path, *element;
  // enable output for debugging
  bool verbose=false;
  // save inputstring in char* path
  string inputString=(std::string)inputTString;
  path = new char [inputString.size()+1];
  strcpy (path, inputString.c_str());
  //  path = (char*)inputTString.Data();
  // get pointer element to elements of path using seperateBy as seperator
  element=strtok (path,(char*)(seperateBy.Data()));
  // get vector with splittet elements
  std::vector<TString> result_;
  if(verbose){
  std::cout << "input: " << inputTString << std::endl;
  std::cout << "seperator: " << seperateBy << std::endl;
  std::cout << "splitted in the following elements:" << std::endl;
  }
  while(element!=NULL){
    if(verbose) std::cout << element << std::endl;
    string output="";
    output=output+element;
    result_.push_back((TString)output);
    element=strtok(NULL,(char*)(seperateBy.Data()));
  }
  delete[] path;
  delete[] element;
  // default configuration: get last entry
  if(entry==42) entry = (result_.size());
  // get requestet element
  if(verbose) std::cout << "requested " << "element #" << entry << " of " << result_.size() << std::endl;
  TString result="";
  // check if element exists
  if(entry<=result_.size()) result=result_[entry-1];
  else{
    std::cout << "warning - the requested element (" << entry <<") does not exist" << std::endl;
    std::cout << "the string "  << inputTString << " with seperator " << seperateBy << " gives only " <<  result_.size() << "elements!" << std::endl;
  }
  if(verbose) std::cout << "will return: " <<  result_[entry-1] << std::endl;
  // return output
  return result_[entry-1];
}

TString TopFilename(unsigned int sample, unsigned int sys, const std::string decayChannel)
{
  // this function contains the basic convention for the MC 
  // .root files and returns the correct names for choosen sample "sample" 
  // and systematic variation "sys"
  // modified quantities: NONE
  // used functions: NONE
  // used enumerators: samples, systematicVariation 

  TString fileName = "decayChannel_undefined" ;
  if (decayChannel.compare("muon")    ==0) fileName ="muonDiffXSec";
  if (decayChannel.compare("electron")==0) fileName ="elecDiffXSec";
  // name of data file is given directly in the .C file
  if(sample==kData) return ""; 
  // standard MC filenames
  if(sample==kSig   )fileName += "SigMadD6T";
  if(sample==kBkg   )fileName += "BkgMadD6T";
  if(sample==kWjets )fileName += "WjetsMadD6T";
  if(sample==kZjets )fileName += "ZjetsMadD6T";
  if(sample==kWW    )fileName += "WWPytia6Z2";
  if(sample==kWZ    )fileName += "WZPytia6Z2";
  if(sample==kZZ    )fileName += "ZZPytia6Z2";
  if(sample==kDiBos )fileName += "VVPytia6Z2";
  if(sample==kQCD   )fileName += "QCDPythiaZ2";
  if(sample==kSToptW)fileName += "SingleTopTWchannelMadZ2";
  if(sample==kSTops )fileName += "SingleTopSchannelMadZ2";
  if(sample==kSTopt )fileName += "SingleTopTchannelMadZ2";
  if(sample==kSTop  )fileName += "SingleTopMadD6T";
  // label for MC production cycle
  // note: we have no Diboson spring11 MC up to now
  if(newSpring11MC&&sample!=kWW&&sample!=kWZ&&sample!=kZZ) fileName += "Spring11";
  else fileName += "Fall10"  ;
  // take care of systematic variations
  // JES
  if(sys==sysJESUp  ) fileName += "JESup";
  if(sys==sysJESDown) fileName += "JESdown";
  // JER
  if(sys==sysJERUp  ) fileName += "JERup";
  if(sys==sysJERDown) fileName += "JERdown";
  // Pile Up
  // at the moment: no variation for QCD
  if(sys==sysPileUp&&sample!=kQCD) fileName += "PileUp";
  // larger ISR/FSR (top only)
  if((sys==sysISRFSRup  )&&((sample==kSig)||(sample==kBkg))) fileName += "ISRFSRup";
  if((sys==sysISRFSRdown)&&((sample==kSig)||(sample==kBkg))) fileName += "ISRFSRdown";
  // Scale
  // a) top
  if((sys==sysTopScaleUp  )&&((sample==kSig)||(sample==kBkg))) fileName+="ScaleUp";
  if((sys==sysTopScaleDown)&&((sample==kSig)||(sample==kBkg))) fileName+="ScaleDown";
  // b) V+jets
  if((sys==sysVBosonScaleUp  )&&((sample==kWjets)||(sample==kZjets))) fileName+="ScaleUp";
  if((sys==sysVBosonScaleDown)&&((sample==kWjets)||(sample==kZjets))) fileName+="ScaleDown";
  // Match
  // a) top
  if((sys==sysTopMatchUp  )&&((sample==kSig)||(sample==kBkg))) fileName+="MatchUp";
  if((sys==sysTopMatchDown)&&((sample==kSig)||(sample==kBkg))) fileName+="MatchDown";
  // b) V+jets
  if((sys==sysVBosonMatchUp  )&&((sample==kWjets)||(sample==kZjets))) fileName+="MatchUp";
  if((sys==sysVBosonMatchDown)&&((sample==kWjets)||(sample==kZjets))) fileName+="MatchDown";
  fileName+="PF.root";
  // return output
  return fileName;
}

void saveCanvas(const std::vector<TCanvas*> MyCanvas, const TString outputFolder, const TString pdfName, const bool savePdf=true, const bool saveEps=true )
{
  // introduce function that saves every single canvas in 
  // MyCanvas as ./outputFolder/CanvasTitle.eps and in addition 
  // all in one rootFile: ./outputFolder/pdfName.pdf
  // modified quantities: NONE
  // used functions: NONE
  // used enumerators: NONE

  // a) save all plots in one pdf
  if(savePdf){
    MyCanvas[0]->Print(outputFolder+pdfName+".pdf(", "pdf");
    for(unsigned int idx=1; idx<MyCanvas.size()-1; idx++){
      MyCanvas[idx]->Print(outputFolder+pdfName+".pdf", "pdf");   
    }
    MyCanvas[MyCanvas.size()-1]->Print(outputFolder+pdfName+".pdf)", "pdf");
  }
  // b) save every plot as pdf with title as name
  if(saveEps){
    for(unsigned int idx=0; idx<MyCanvas.size(); idx++){
      MyCanvas[idx]->Print(outputFolder+(TString)(MyCanvas[idx]->GetTitle())+".eps");      
    }
  }
}

std::map<unsigned int, TFile*> getStdTopAnalysisFiles( const TString inputFolder, const unsigned int systematicVariation, const TString dataFile, const std::string decayChannel)
{
  // this function returns a map containing all existing .root in "inputFolder"
  // corresponding to the choosen systematic variation "systematicVariation"
  // and the data file "dataFile" for which the direct path/name.root is needed 
  // The MC .root file names correspond to the standard names as defined in the 
  // function TopFilename
  // modified quantities: NONE
  // used functions: TopFilename
  // used enumerators: samples

  // open our standard analysis files and save them in a map
  std::map<unsigned int, TFile*> files_;
  // loop samples
  for(int sample = kSig; sample<=kSToptW; sample++){
    TString fileName;
    if(sample!=kData) fileName = inputFolder+"/"+TopFilename(sample, systematicVariation, decayChannel);
    if(sample==kData) fileName = dataFile; 
    // if file exists - save in map
    if((fileName!="no")&&(fileName!="")){ 
      TFile* file = new (TFile)(fileName);
      if(!(file->IsZombie())) files_[sample]= file;
    }
  }
  return files_;
}

void getAllPlots( std::map<unsigned int, TFile*> files_, const std::vector<TString> plotList_,  std::map< TString, std::map <unsigned int, TH1F*> >& histo_, std::map< TString, std::map <unsigned int, TH2F*> >& histo2_, const unsigned int N1Dplots, int& Nplots, const unsigned int verbose=0, const std::string decayChannel = "unset" )
{
  // this function searches for every plot listed in "plotList_" in all files listed in "files_",
  // saves all 1D histos into "histo_" and all 2D histos into "histo2_"
  // empty plots will be neglected
  // modified quantities: "histo_", "histo2_", "Nplots"
  // used functions: sampleLabel
  // used enumerators: samples
  // "N1Dplots": the #1D plots is needed as input to destinguish between 1D and 2D plots
  // "Nplots": the total # of plots is calclated
  // "verbose": set detail level of output ( 0: no output, 1: std output 2: output for debugging )

  // loop plots
  for(unsigned int plot=0; plot<plotList_.size(); ++plot){  
    // check if plot exists in any sample
    bool existsInAnySample=false;
    // loop samples
    for(unsigned int sample=kSig; sample<=kSToptW; ++sample){
      // check existence of sample
      if(files_.count(sample)!=0){ 
	// create plot container
	TH1* targetPlot;
	files_[sample]->GetObject(plotList_[plot], targetPlot);
	// Check existence of plot
	if(targetPlot) existsInAnySample=true;
      }
    }
    // end program and draw error if plot does not exist at all
    if(!existsInAnySample){
      std::cout << "ERROR: plot "+plotList_[plot]+" does not exist in any file!" << std::endl;
      exit(1);
    }
    else{
      // otherwise: get plots from sample
      // loop samples
      for(unsigned int sample=kSig; sample<=kSToptW; ++sample){
	// check if file exists
	// give warning if file does not exist
	if((files_.count(sample)==0)&&(plot==0)&&(verbose>0)) std::cout << "file for " << sampleLabel(sample,decayChannel) << " does not exist- continue and neglect this sample" << std::endl;
	if(files_.count(sample)>0){
	  // create plot container
	  TH1* targetPlot;
	  if(verbose>0){ 
	    std::cout << "sample: " << sample << ", " << files_[sample]->GetName() << std::endl;
	    std::cout << "plot: " << plot << ", " << plotList_[plot] << std::endl;
	  }
	  files_[sample]->GetObject(plotList_[plot], targetPlot);
	  // Check if plot exits
	  // give warning if plot does not exist
	  if((!targetPlot)&&(verbose>0)) std::cout << "can not find plot "+plotList_[plot] << " in file "+(TString)(files_[sample]->GetName()) << " - continue and neglect this plot" << std::endl;
	  if(targetPlot){
	    // check if plot is empty
	    bool emptyPlot=false;
	    if((plot<N1Dplots )&&((((TH1*)(files_[sample]->Get(plotList_[plot])))->GetEntries())==0.)) emptyPlot=true;
	    if((plot>=N1Dplots)&&((((TH2*)(files_[sample]->Get(plotList_[plot])))->GetEntries())==0.)) emptyPlot=true;
	    if(emptyPlot && verbose>0) std::cout << "plot "+plotList_[plot] << " in file "+(TString)(files_[sample]->GetName()) << " is empty- continue and neglect this plot" << std::endl;
	    // to avoid problems with samples where no event is passing the selection we will drop this requirement by now
	    emptyPlot=false;
	    if(!emptyPlot){
	      // save plot in corresponding map
	      if(plot<N1Dplots ) histo_ [plotList_[plot]][sample] = (TH1F*)(files_[sample]->Get(plotList_[plot]));
	      if(plot>=N1Dplots) histo2_[plotList_[plot]][sample] = (TH2F*)(files_[sample]->Get(plotList_[plot]));
	      // count every existing 2D plot (every sample is counted separetly as it will be drawn into an own canvas)
	      if(plot>=N1Dplots) Nplots++;
	    }
	  }
	}
      }
      // count every existing type of 1D plots (neglect #samples here as they well be drawn into the same canvas)
      if((plot<N1Dplots)&&(histo_.count(plotList_[plot])>0)) Nplots++;
    }
  }
}

void scaleByLuminosity(const std::vector<TString> plotList_,  std::map< TString, std::map <unsigned int, TH1F*> >& histo_, std::map< TString, std::map <unsigned int, TH2F*> >& histo2_, const unsigned int N1Dplots, const double luminosity, const unsigned int verbose=1, const int systematicVariation=sysNo, const std::string decayChannel = "unset")
{
  // this function scales every histo in histo_ and histo2_ to the corresponding luminosity
  // Additionally the mu eff SF is applied
  // modified quantities: "histo_", "histo2_"
  // used functions: sampleLabel, effSFAB 
  // used enumerators: samples
  // "N1Dplots": the #1D plots is needed as input to destinguish between 1D and 2D plots
  // "verbose": set detail level of output ( 0: no output, 1: std output 2: output for debugging )
  // "luminosity": [/pb]
  // "systematicVariation": specify systematic variation corresponding to enum systematicVariation

  // loop samples
  for(unsigned int sample=kSig; sample<=kSToptW; ++sample) {
    // loop plots 
    for(unsigned int plot=0; plot<plotList_.size(); ++plot){
      // a) 1D
      // check if 1D plot exists
      if((plot<N1Dplots)&&(histo_.count(plotList_[plot])>0)&&(histo_[plotList_[plot]].count(sample)>0)){
	if(verbose>1) std::cout << std::endl << "plot: "+plotList_[plot] << " for sample " << sampleLabel(sample,decayChannel) << ":" << std::endl;
	if(verbose>1) std::cout << "#events before weighting: " << histo_[plotList_[plot]][sample]->Integral(0, histo_[plotList_[plot]][sample]->GetNbinsX()+1) << std::endl;
	// scale MC samples to same luminosity
	double weight = lumiweight(sample, luminosity, systematicVariation, decayChannel);
	histo_[plotList_[plot]][sample]->Scale(weight);
	if(verbose>1) std::cout << "weight: " << weight << std::endl;
	if(verbose>1) std::cout << "#events after weighting: " << histo_[plotList_[plot]][sample]->Integral(0, histo_[plotList_[plot]][sample]->GetNbinsX()+1) << std::endl;
	// apply eff. SF for MC
	if(sample!=kData) histo_[plotList_[plot]][sample]->Scale(effSFAB(systematicVariation,decayChannel));
      }
      // b) 2D
      // check if 2D plot exists
      if((plot>=N1Dplots)&&(histo2_.count(plotList_[plot])>0)&&(histo2_[plotList_[plot]].count(sample)>0)){
	if(verbose>1) std::cout << std::endl << "plot: "+plotList_[plot] << " for sample " << sampleLabel(sample,decayChannel) << ":" << std::endl;
	if(verbose>1) std::cout << "#events before weighting: " << histo2_[plotList_[plot]][sample]->Integral(0, histo2_[plotList_[plot]][sample]->GetNbinsX()+1, 0, histo2_[plotList_[plot]][sample]->GetNbinsY()+1) << std::endl;
	// scale MC samples to same luminosity
	double weight = lumiweight(sample, luminosity, systematicVariation, decayChannel);
	histo2_[plotList_[plot]][sample]->Scale(weight);
	if(verbose>1) std::cout << "weight: " << weight << std::endl;
	if(verbose>1) std::cout << "#events after weighting: " << histo2_[plotList_[plot]][sample]->Integral(0, histo2_[plotList_[plot]][sample]->GetNbinsX()+1, 0, histo2_[plotList_[plot]][sample]->GetNbinsY()+1) << std::endl;
	// apply eff. SF for MC
	if(sample!=kData) histo2_[plotList_[plot]][sample]->Scale(effSFAB(systematicVariation,decayChannel));
      }
    }
  }
}

void AddSingleTopAndDiBoson(const std::vector<TString> plotList_,  std::map< TString, std::map <unsigned int, TH1F*> >& histo_, std::map< TString, std::map <unsigned int, TH2F*> >& histo2_, const unsigned int N1Dplots, const unsigned int verbose=1, bool reCreate=false, const std::string decayChannel = "unset")
{
  // this function creates plots for all diboson and all single 
  // top samples combined if the combined SingleTop and DiBoson 
  // samples do not exist as .root file. 
  // Every plot in "plotList_" existing in each of the three 
  // sTop/ diBoson files will be combined and saved in the histo_ 
  // and histo2_ maps
  // NOTE: all plots from the samples are considered to be weighted 
  // to the same luminosity before 
  // modified quantities: "histo_", "histo2_"
  // used functions: sampleLabel
  // used enumerators: samples
  // "N1Dplots": the #1D plots is needed as input to destinguish between 1D and 2D plots
  // "verbose": set detail level of output ( 0: no output, 1: std output 2: output for debugging )
  // "reCreate": choose if you want to create the combined plot from the 
  // single plots if it alredy exists. Careful: the old one will be deleted

  if(verbose>0) std::cout << std::endl;
  // loop plots 
  for(unsigned int plot=0; plot<plotList_.size(); ++plot){
    // loop STop and DiBoson
    for(unsigned int sample=kSTop; sample<=kDiBos; ++sample){
      if(verbose>1) std::cout << "plot " << plotList_[plot] << ": " << std::endl;
      // mark first plot found
      bool first=true;
      // check that combined plot does not already exist
      // if existing and reCreate==1, it will be overwritten
      bool combinedplotExists=false;
      if((plot<N1Dplots )&&(histo_ [plotList_[plot]].count(sample)>0)) combinedplotExists=true;
      if((plot>=N1Dplots)&&(histo2_[plotList_[plot]].count(sample)>0)) combinedplotExists=true;
      if(reCreate==1) combinedplotExists=false;
      if((combinedplotExists==true)&&(verbose>0)){
	std::cout << "combined plot " << plotList_[plot];
	std::cout << " for sample " << sampleLabel(sample,decayChannel);
	std::cout << " already exists, will keep this one" << std::endl;
      }
      if(!combinedplotExists){
	// loop all three subchannels
	unsigned int firstSubChannel=kSTops;
	if(sample==kDiBos) firstSubChannel=kWW;
	for(unsigned int subSample=firstSubChannel; subSample<=firstSubChannel+2; ++subSample){
	  // check if plot exists for the subchannel
	  bool subPlotExists=false;
	  if((plot<N1Dplots )&&(histo_ [plotList_[plot]].count(subSample)>0)) subPlotExists=true;
	  if((plot>=N1Dplots)&&(histo2_[plotList_[plot]].count(subSample)>0)) subPlotExists=true;
	  if((subPlotExists==false)&&(verbose>0)){
	    std::cout << "plot " << plotList_[plot];
	    std::cout << " does not exist for subSample ";
	    std::cout << sampleLabel(subSample,decayChannel) << std::endl;
	  }
	  if(subPlotExists){
	    // add histo
	    // a) 1D 
	    if(plot<N1Dplots){
	      if(first ) histo_[plotList_[plot]][sample]   =  (TH1F*)histo_[plotList_[plot]][subSample]->Clone();
	      if(!first) histo_[plotList_[plot]][sample]->Add((TH1F*)histo_[plotList_[plot]][subSample]->Clone());
	    }
	    // b) 2D
	    if(plot>=N1Dplots){
	      if(first ) histo2_[plotList_[plot]][sample]   =  (TH2F*)histo2_[plotList_[plot]][subSample]->Clone();
	      if(!first) histo2_[plotList_[plot]][sample]->Add((TH2F*)histo2_[plotList_[plot]][subSample]->Clone());
	    }
	    // indicate that already one plot is found
	    first=0;
	    // print out information 
	    if(verbose>0){
	      std::cout << "will add " << plotList_[plot];
	      std::cout << " from " << sampleLabel(subSample,decayChannel) << std::endl;
	    }
	  }
	}
      }
    }
  }
}
		       
void createStackPlot(const std::vector<TString> plotList_, std::map< TString, std::map <unsigned int, TH1F*> >& histo_, const unsigned int plot, const unsigned int N1Dplots, const unsigned int verbose=1, const std::string decayChannel="muon")
{
  // this function will transform the histogram "plotList_"["plot"] 
  // within "histo_" into stacked plots. 
  // modified quantities: "histo_"
  // used functions: sampleLabel
  // used enumerators: samples
  // "verbose": set detail level of output ( 0: no output, 1: std output 2: output for debugging )
  // "N1Dplots": the #1D plots is needed as input to destinguish between 1D and 2D plots

  // loop samples backwards
  for(int sample=kDiBos-1; sample>=kSig; --sample){
    // check if plot exists
    if((plot<N1Dplots)&&(histo_.count(plotList_[plot])>0)&&(histo_[plotList_[plot]].count(sample)>0)){
      // check if previous plot also exists
      if(histo_[plotList_[plot]].count(sample+1)>0){
	histo_[plotList_[plot]][sample]->Add((TH1F*)histo_[plotList_[plot]][sample+1]->Clone());
	if(verbose>1) std::cout << "add "+plotList_[plot] << " plot for " << sampleLabel(sample,decayChannel) << " and " << sampleLabel(sample+1,decayChannel) << std::endl;
	if(verbose>1) std::cout << "this new stacked plot contains now " <<  histo_[plotList_[plot]][sample]->Integral(0, histo_[plotList_[plot]][sample]->GetNbinsX()+1) << " events" << std::endl;
      }
    }
  }
}

float modulo(const float a, const float b)
{
  // this function calculates a modulo b 
  // where a and b are float
  // modified quantities: none
  // used functions: none
  // used enumerators: none
  // "a": dividend
  // "b": divisor
  
  // round a and b to the 3rd decimal place
  // this should prevent errors due to rounding effects
  float astar=ceil(a*1000.-0.5)/1000.;
  float bstar=ceil(b*1000.-0.5)/1000.;
  //  std::cout << std::endl << astar << " modulo ";
  //  std::cout << bstar << std::endl;
  float rest=astar-bstar;
  if(rest<0){
    std::cout << "can not compute " << astar << " modulo " << bstar << std::endl;
    std::cout << "because " << astar << " < " << bstar << std::endl;
    exit(1);
  }
  for(float n=1; rest>0; n++){
    rest=astar-n*bstar;
    if(rest<0){
      rest = astar-(n-1.)*bstar;
      break;
    }
  }
  return rest;
}

void reBinTH1F(TH1F& histoUnbinned, const std::vector<double> &binlowerEdges_, const unsigned int verbose=0)
{
  // this function rebins an histogram using a variable binning
  // modified quantities: "histoUnbinned"
  // ATTENTION: histoUnbinned needs to have an initial equidistant binning
  // used functions: modulo
  // used enumerators: none
  // "histoUnbinned": plot to be binned
  // "binlowerEdges": vector containing all lower bin edges starting at xaxis.min, ending with xaxis.max
  // "verbose": set detail level of output ( 0: no output, 1: std output 2: output for debugging )

  unsigned int NinitialBins=histoUnbinned.GetNbinsX();
  double xMin=histoUnbinned.GetBinLowEdge(1);
  double xMax=histoUnbinned.GetBinLowEdge(NinitialBins+1);
  if(verbose>1){
    std::cout << "plot: "  << histoUnbinned.GetName() << std::endl;
    std::cout << "min: " << xMin << std::endl;
    std::cout << "max: " << xMax << std::endl;
    std::cout << "N(initial bins): " << NinitialBins << std::endl;
  }
  // check if chosen binning is valid
  // 1) N(bins)
  if(NinitialBins<=binlowerEdges_.size()){
    std::cout << "histo " << histoUnbinned.GetName() << " can not be rebinned" << std::endl;
    std::cout << "N(chosen bins) < N(initial bins)!" << std::endl;
    exit(1);
  }
  // 2) coarseness of chosen binning
  //  double initialBinWidth=(xMax-xMin)/(double)NinitialBins;
  double initialBinWidth = (double)(roundToInt(10000.*histoUnbinned.GetBinWidth(1)))/10000.;

  if(verbose>1) std::cout << "initial binwidth: " << initialBinWidth << std::endl;
  if(binlowerEdges_.size()>1){
    for(unsigned int finalBin=1; finalBin<binlowerEdges_.size()-1; ++finalBin){
      double finalBinWidth=binlowerEdges_[finalBin]-binlowerEdges_[finalBin-1];
      if(verbose>1){
	std::cout << "bin #" << finalBin << ": ";
	std::cout << std::setprecision(20) << std::fixed << finalBinWidth << " modulo ";
	std::cout << std::setprecision(20) << std::fixed << initialBinWidth;
	std::cout << " = " << modulo(finalBinWidth, initialBinWidth) << std::endl;
      }
      if(modulo(finalBinWidth, initialBinWidth)!=0){
	std::cout << "histo " << histoUnbinned.GetName() << " can not be rebinned" << std::endl;
	std::cout << "the ininital binning is to coarse for the chosen binning!" << std::endl;
	std::cout << "attention: probably error in modulo function," << std::endl;
	std::cout << "bin #" << finalBin << " of the choosen binning has ";
	std::cout << "finalBinWidth modulo initialBinWidth of " << modulo(finalBinWidth,initialBinWidth) << std::endl;
	exit(1);
      }
    }
  }
  // fill vector entries in array
  // because TH1F constructer needs an array
  unsigned int arraySize=42;
  double * binLowerEdgeArray = new double[arraySize];
  if(binlowerEdges_.size()>arraySize){
    std::cout << "histo " << histoUnbinned.GetName() << " can not be rebinned" << std::endl;
    std::cout << "the function reBinTH1F can deal with at most " << arraySize << " bins" << std::endl;
    exit(1);
  }
  for(unsigned int arrayEntry=0; arrayEntry<arraySize; ++arrayEntry){
    if(arrayEntry<binlowerEdges_.size()){
      binLowerEdgeArray[arrayEntry]=binlowerEdges_[arrayEntry];
        if(verbose>1) std::cout << "array entry #" << arrayEntry << ": " << binLowerEdgeArray[arrayEntry] << " ";
    }
    else binLowerEdgeArray[arrayEntry]=binlowerEdges_[binlowerEdges_.size()-1];
  }
  if(verbose>1) std::cout << std::endl;
  // TH1F* histoBinned = new TH1F( histoUnbinned.GetName(), histoUnbinned.GetTitle(), arraySize-1, binLowerEdgeArray);
  if(verbose>1) std::cout << "N(bins) before rebinning: " << histoUnbinned.GetNbinsX() << std::endl;
  histoUnbinned = *(TH1F*)histoUnbinned.Rebin(arraySize-1, histoUnbinned.GetName(), binLowerEdgeArray);
  if(verbose>1){
    std::cout << "N(bins) after rebinning: " << histoUnbinned.GetNbinsX() << " (should be " << arraySize-1 << ")" << std::endl;
    std::cout << "from which only " << binlowerEdges_.size() << " bins are used" << std::endl;
    std::cout << "the rest will be ignored and exists only for technical reasons" << std::endl;
  }
  delete binLowerEdgeArray;
}

bool plotExists(std::map< TString, std::map <unsigned int, TH1F*> > histo_, const TString plotName, const unsigned int sample)
{
  // this function checks the existence of an specific 
  // entry "histo_[plotName][sample]" in the map "histo_"
  // that contains all 1D plots
  // modified quantities: none
  // used functions: none
  // used enumerators: none

  bool result=false;
  if((histo_.count(plotName)>0)&&(histo_[plotName].count(sample)>0)){
    result=true;
  }
  return result;
}

void equalReBinTH1(const int reBinFactor, std::map< TString, std::map <unsigned int, TH1F*> > histo_, const TString plotName, const unsigned int sample)
{
  // this uses an equal rebinning (factor "reBinFactor") 
  // for an specific entry "histo_[plotName][sample]" 
  // in the map "histo_" that contains all 1D plots
  // modified quantities: histo_[plotName][sample]
  // used functions: plotExists
  // used enumerators: none

  if(plotExists(histo_, plotName, sample)){
    (histo_[plotName][sample])->Rebin(reBinFactor);
  }

}


std::map<TString, std::vector<double> > makeVariableBinning()
{
  // this function creates a map with the hard coded 
  // bin values for variable binning
  // NOTE: it is important to quote the overflow bin 
  // of the initial binning as last bin here!!!
  // otherwise dividing per binwidth function 
  // might later give nan and histo wouldn't be drawn
  // modified quantities: none
  // used functions: none
  // used enumerators: none

  std::map<TString, std::vector<double> > result;
  std::vector<double> bins_;

  
  // pt(top)
  double topPtBins[]={0., 60., 120., 200., 280., 400., 800.};
  bins_.insert( bins_.begin(), topPtBins, topPtBins + sizeof(topPtBins)/sizeof(double) );
  result["topPt"]=bins_;
  //  result["analyzeTopPartonLevelKinematics/topPt"  ]=bins_;
  bins_.clear();
  // y(top)
  double topYBins[]={-5., -2.5, -1.5, -1., -0.5, 0., 0.5, 1., 1.5, 2.5, 5.};
  bins_.insert( bins_.begin(), topYBins, topYBins + sizeof(topYBins)/sizeof(double) );
  result["topY"]=bins_;
  //  result["analyzeTopPartonLevelKinematics/topY"  ]=bins_;
  bins_.clear();
  // pt(ttbar)
  double ttbarPtBins[]={0., 20., 60., 110., 200., 300.};
  bins_.insert( bins_.begin(), ttbarPtBins, ttbarPtBins + sizeof(ttbarPtBins)/sizeof(double) );
  result["ttbarPt"]=bins_;
  //  result["analyzeTopPartonLevelKinematics/ttbarPt"  ]=bins_;
  bins_.clear();
  // y(ttbar)
  double ttbarYBins[]={-5., -1.3, -0.9, -0.6, -0.3, 0., 0.3, 0.6, 0.9, 1.3, 5.};
  bins_.insert( bins_.begin(), ttbarYBins, ttbarYBins + sizeof(ttbarYBins)/sizeof(double) );
  result["ttbarY"]=bins_;
  //  result["analyzeTopPartonLevelKinematics/ttbarY"  ]=bins_;
  bins_.clear();
  // m(ttbar)
  double ttbarMassBins[]={0., 345., 410., 480., 580., 750., 1200.};
  bins_.insert( bins_.begin(), ttbarMassBins, ttbarMassBins + sizeof(ttbarMassBins)/sizeof(double) );
  result["ttbarMass"]=bins_;
  //  result["analyzeTopPartonLevelKinematics/ttbarMass"  ]=bins_;
  bins_.clear();
  
  return result;

}

template <class T>
unsigned int positionInVector(std::vector<T> vec_, T object)
{  
  // this function returns the position
  // of element object in vector vec_
  // modified quantities: none
  // used functions: none
  // used enumerators: none

  // loop vector elements
  for(unsigned int element=0; element<vec_.size(); ++element)
    {
      // ask for requested element
      if(vec_[element]==object){
	return element;
      }
    }
  // return -1 if requested element is not found
  std::cout << "requested element " << object << " is not found in  vector" << std::endl;
  return -1;
}

void DivideYieldByEfficiencyAndLumi(TH1F* yield, TH1F* efficiency, double luminosity, bool includeEffError)
{
  // this function divides yield by efficiency
  // and calculates the correct error in each bin based
  // on gaussian error propagation
  // modified quantities: yield
  // used functions: none
  // used enumerators: none

  // check if #bins are the same
  if(yield->GetNbinsX()!=efficiency->GetNbinsX()){
    std::cout << "#bins in yield and efficiency plots are not the same!" << std::endl;
    exit(1);
  }
  // loop all bins
  for(int bin=1; bin<=yield->GetNbinsX(); ++bin){
    double content  = yield     ->GetBinContent(bin);
    double eff      = efficiency->GetBinContent(bin);
    double binwidth = yield     ->GetBinWidth  (bin);
    double events   = binwidth*content;
    // value (events/binwidth/eff/lumi)
    double xSec = content/(eff*luminosity);
    // error 
    double effError=efficiency->GetBinError(bin);
    if(!includeEffError) effError=0;
    double xSecError = 1/(binwidth*luminosity)*sqrt( ((events)/(eff*eff)) + ((events*effError)/(eff*eff))* ((events*effError)/(eff*eff)) );
    // check if efficiency is 0
    if(eff==0){
      xSec=0;
      xSecError=0;
    }
    // set value and error
    yield->SetBinContent(bin, xSec     );
    yield->SetBinError  (bin, xSecError);
  }
}

template <class T>
void saveToRootFile(const TString& outputFile, const T& object, const bool& overwrite=false, const unsigned int& verbose=1, const TString& folder="")
{
  // this function saves objects of class T
  // (such as TH1) in an output rootfile with name outputFile
  // modified quantities: outputFile
  // used functions: none
  // used enumerators: none

  bool saveObject=true;
  // check if file exist
  TFile* file = TFile::Open(outputFile, "UPDATE");
  // if not exist: create
  if(!file){
    if(verbose>1) std::cout << "file " << outputFile << " does not exist, will be created" << std::endl;
    file = new TFile(outputFile, "RECREATE");
  }
  // check if file is broken
  if(file->IsZombie()){
    std:: cout << "file " << outputFile << " is broken" << std::endl;
    // if broken: don't save object
    saveObject=false;
  }
  else{
    // if not broken: open file
    file->cd();
    // create folder if it does not exist
    if(folder!=""){
      if(verbose>1) std::cout << "check existence of directory " << folder << std::endl;
      // see how many subfolders are within folder
      unsigned int Nfolders=folder.CountChar(*"/")+1;
      if(verbose>1) std::cout << "these are " << Nfolders << " subdirectories" << std::endl;
      // loop subdirectories
      for(unsigned int subfolderNumber=1; subfolderNumber<=Nfolders; ++subfolderNumber){
	TString subfolder= getStringEntry(folder, subfolderNumber, "/");
	if(gDirectory->GetDirectory(subfolder)==0){
	  if(verbose>1) std::cout << "subfolder " << subfolder  << " not existing - will create it" << std::endl;
	  gDirectory->mkdir(subfolder);
	}
	else if(verbose>1) std::cout << "subfolder " << subfolder  << " is already existing" << std::endl;
	// go to directory
	gDirectory->cd(subfolder);
      }
    }
    // if you don't want to overwrite, check if object exists
    int count=-1;
    if(!overwrite){
      TString saveObjectName=(TString)object->GetTitle();
      if(verbose>1) std::cout << "searching for object " << saveObjectName << std::endl;
      // loop all objects in file
      TList * list = gDirectory->GetListOfKeys();
      while( list->At( count+1 ) != list->Last()){
	++count;
	TObject *folderObject = list->At(count);
	TString folderObjectName = (TString)folderObject->GetName();
	if(verbose>1) std::cout << "candidate #" << count+1 << ": " << folderObjectName << std::endl;
	// check if object you want to save is already existing
	// by comparing the names
	if(folderObjectName==saveObjectName){
	  if(verbose>1){
	    std::cout << "already exists in file " << outputFile << std::endl;
	    std::cout << "will keep the old one!" << std::endl << std::endl;
	  }
	  saveObject=false;
	  break;
	}
      }
    }
  }
  // save object
  if(saveObject){
    if(verbose>0){
      std::cout << "saving object " << (TString)object->GetTitle();
      std::cout << " to file " << outputFile;
      if(folder!="") std::cout << " ( folder " << folder << " )";
      std::cout << std::endl << std::endl;
    }
    // overwrite existing
    object->Write(object->GetTitle(), TObject::kOverwrite);
  }
  // close file
  file->Close();
}

void drawRatio(const TH1* histNumerator, TH1* histDenominator, const Double_t& ratioMin, const Double_t& ratioMax, unsigned int verbose=0, const std::vector<double> err_=std::vector<double>(0))
{
  // this function draws a pad with the ratio of 'histNumerator' and 'histDenominator'
  // the range of the ratio is 'ratioMin' to 'ratioMax'
  // to the systematic variation "sys" of the enumerator "systematicVariation"
  // per default only the gaussian error of the 'histNumerator' is considered:
  // (error(bin i) = sqrt(histNumerator->GetBinContent(i))/histDenominator->GetBinContent(i))
  // if 'err_' is present and its size equals the number of bins in the histos,
  // its values are considered as error for the ratio
  // NOTE: x Axis is transferred from histDenominator to the bottom of the canvas
  // modified quantities: none
  // used functions: none
  // used enumerators: none 

  // check that histos have the same binning
  if(histNumerator->GetNbinsX()!=histDenominator->GetNbinsX()){
    std::cout << "error when calling drawRatio - histos have different number of bins" << std::endl;
    return;
  }
  if(verbose>1){
    std::cout << "building ratio plot of " << histNumerator->GetName();
    std::cout << " and " << histDenominator->GetName() << std::endl;
  }
  // create ratio 
  TH1F* ratio = (TH1F*)histNumerator->Clone();
  ratio->Divide(histDenominator);
  // calculate error for ratio
  // a) from err_
  if(err_.size()==(unsigned int)histNumerator->GetNbinsX()){
    if(verbose>0) std::cout << "ratio error from vector" << std::endl;
    for(int bin=1; bin<=histNumerator->GetNbinsX(); bin++){
      ratio->SetBinError(bin, err_[bin-1]);
    }
  }
  else{
    // b) default: only gaussian error of histNumerator
    if(verbose>0) std::cout << "ratio error from statistical error of " << histNumerator->GetName() << " only" << std::endl;
    for(int bin=1; bin<=histNumerator->GetNbinsX(); bin++){
      ratio->SetBinError(bin, sqrt(histNumerator->GetBinContent(bin))/histDenominator->GetBinContent(bin));
    }
  }
  // get some values from old pad
  Int_t     logx = gPad->GetLogx();
  Double_t  left = gPad->GetLeftMargin();
  Double_t right = gPad->GetRightMargin();
  // y:x size ratio for canvas
  double canvAsym = 4./3.;
  // ratio size of pat with plot and pat with ratio
  double ratioSize = 0.36;
  // change old pad
  gPad->SetBottomMargin(ratioSize);
  gPad->SetRightMargin(right);
  gPad->SetLeftMargin(left);
  gPad->SetBorderMode(0);
  gPad->SetBorderSize(0);
  gPad->SetFillColor(10);
  // create new pad for ratio plot
  TPad *rPad;
  rPad = new TPad("rPad","",0,0,1,ratioSize+0.001);
  rPad->SetFillStyle(0);
  rPad->SetFillColor(0);
  rPad->SetBorderSize(0);
  rPad->SetBorderMode(0);
  rPad->Draw();
  rPad->cd();
  rPad->SetLogy(0);
  rPad->SetLogx(logx);
  rPad->SetTicky(1);
  // configure ratio plot
  double scaleFactor = 1./(canvAsym*ratioSize);
  ratio->SetStats(kFALSE);
  ratio->SetMarkerSize(0.1);
  ratio->SetTitle("");
  ratio->SetMaximum(ratioMax);
  ratio->SetMinimum(ratioMin);
  ratio->SetLineWidth(1);
  // configure axis of ratio plot
  ratio->GetXaxis()->SetTitleSize(histDenominator->GetXaxis()->GetTitleSize()*scaleFactor*1.3);
  ratio->GetXaxis()->SetTitleOffset(histDenominator->GetXaxis()->GetTitleOffset()*0.9);
  ratio->GetXaxis()->SetLabelSize(histDenominator->GetXaxis()->GetLabelSize()*scaleFactor*1.4);
  ratio->GetXaxis()->SetTitle(histDenominator->GetXaxis()->GetTitle());
  ratio->GetXaxis()->SetNdivisions(histDenominator->GetNdivisions());
  ratio->GetYaxis()->CenterTitle();
  ratio->GetYaxis()->SetTitle("#frac{N_{data}}{N_{MC}}");
  ratio->GetYaxis()->SetTitleSize(histDenominator->GetYaxis()->GetTitleSize()*scaleFactor);
  ratio->GetYaxis()->SetTitleOffset(histDenominator->GetYaxis()->GetTitleOffset()/scaleFactor);
  ratio->GetYaxis()->SetLabelSize(histDenominator->GetYaxis()->GetLabelSize()*scaleFactor);
  ratio->GetYaxis()->SetLabelOffset(histDenominator->GetYaxis()->GetLabelOffset()*3.3);
  ratio->GetYaxis()->SetTickLength(0.03);
  ratio->GetYaxis()->SetNdivisions(505);
  ratio->GetXaxis()->SetRange(histDenominator->GetXaxis()->GetFirst(), histDenominator->GetXaxis()->GetLast());
  // delete axis of initial plot
  histDenominator->GetXaxis()->SetLabelSize(0);
  histDenominator->GetXaxis()->SetTitleSize(0);
  // draw ratio plot
  ratio->DrawClone("pe1 X0");
  ratio->SetMarkerSize(1.2);
  ratio->DrawClone("pe1 X0 same");
  rPad->SetTopMargin(0.0);
  rPad->SetBottomMargin(0.15*scaleFactor);
  rPad->SetRightMargin(right);
  gPad->SetLeftMargin(left);
  gPad->RedrawAxis();
  // draw grid
  rPad->SetGrid(1,1);

  // draw a horizontal lines on a given histogram
  // a) at 1
  Double_t xmin = ratio->GetXaxis()->GetXmin();
  Double_t xmax = ratio->GetXaxis()->GetXmax();
  TString height = ""; height += 1;
  TF1 *f = new TF1("f", height, xmin, xmax);
  f->SetLineStyle(1);
  f->SetLineWidth(1);
  //  f->SetLineColor(lcolor);
  f->Draw("L same");
  // b) at upper end of ratio pad
  TString height2 = ""; height2 += ratioMax;
  TF1 *f2 = new TF1("f2", height2, xmin, xmax);
  f2->SetLineStyle(1);
  f2->SetLineWidth(1);
  f2->Draw("L same");
}




#endif
