#ifndef KIN_RECO_H
#define KIN_RECO_H

#include <TLorentzVector.h>
#include "classes.h"

struct TtDilepEvtSolution {
    TLorentzVector lp, lm;
    TLorentzVector jetB, jetBbar;
    size_t jetB_index, jetBbar_index;
    TLorentzVector met;
    TLorentzVector Wplus, Wminus;
    TLorentzVector top, topBar;
    TLorentzVector neutrino, neutrinoBar;
    TLorentzVector ttbar;
    double recMtop;
    double weight;
};

class TF2;

/*
  \class   TtFullLepKinSolver TtFullLepKinSolver.h "TopQuarkAnalysis/TopKinFitter/interface/TtFullLepKinSolver.h"
  
  \brief   Class to calculate solutions for neutrino momenta in dileptonic ttbar events and related probability weights

  Class to calculate solutions for neutrino momenta in dileptonic ttbar events and related probability weights.
  A fourth-order polynomial in p_x(nu) is used with coefficients that are functions of the top-quark mass.
  If physical (non-imaginary) solutions are found, the neutrino momenta are compared to the expected neutrino spectrum
  (from simulation) to obtain a probability weight for each solution.
  This class is based on a code by Jan Valenta.
  
**/

class TtFullLepKinSolver {

public:
    struct NeutrinoSolution {
        double weight;
        TLorentzVector neutrino;
        TLorentzVector neutrinoBar; 
    };

public:

    /// construct with mass range
    TtFullLepKinSolver(const std::vector< double >& nupars, double mW, double mB);

    ///
    TtDilepEvtSolution 
    GetKinSolution(const TLorentzVector& leptonMinus, const TLorentzVector& leptonPlus, 
                const TLorentzVector &b, const TLorentzVector &bbar, 
                const TLorentzVector &met, double topMass);

private:
    NeutrinoSolution 
    getNuSolution(const TLorentzVector& LV_antilepton, 
                  const TLorentzVector& LV_lepton, 
                  const TLorentzVector& LV_b, 
                  const TLorentzVector& LV_bbar,
                  const TLorentzVector& LV_met,
                  double mt);

    
  ///
    void FindCoeff(const TLorentzVector& al, 
                   const TLorentzVector& l,
                   const TLorentzVector& b_al,
                   const TLorentzVector& b_l,
                   const double mt, const double mat, const TLorentzVector& met,
                   double* q_coeff);
    ///
    void NeutrinoRec(double sol);
    
    /// use the parametrized event shape to obtain the solution weight.
    double WeightSolfromShape() const;
    ///
    int quartic(double* q_coeff, double* q_sol) const;
    ///
    int cubic(const double* c_coeff, double* c_sol) const;
    ///
    double sqr(const double x) const {return (x*x);}
    
    ///
    const double mw;
    ///
    const double mb;
    ///
    std::vector<double> nupars_;
    
    double C;
    double D;
    double F;
    double pom;
    double k16;
    double k26;
    double k36;
    double k46;
    double k56;
    double k51;
    double k61;
    double m1;
    double m2;
    double m3;
    double n1;
    double n2;
    double n3;
    
    ///
    TLorentzVector LV_n, LV_n_, LV_t, LV_t_, LV_tt_t, LV_tt_t_;  
    /// provisional
    TLorentzVector genLV_n, genLV_n_;  
        
};


//Kinematic solution maker
std::vector< TtDilepEvtSolution > 
GetKinSolutions(const LV& leptonMinus, const LV& leptonPlus, 
                const VLV* jets, const std::vector<double>* btags,
                const LV* met);

#endif
