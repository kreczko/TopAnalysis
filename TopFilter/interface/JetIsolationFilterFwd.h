#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

// isolation filter expansions for muons and electrons
#include "TopAnalysis/TopFilter/interface/JetIsolationFilter.h"

typedef JetIsolationFilter<std::vector<pat::Muon>     > MuonJetIsolationFilter;
typedef JetIsolationFilter<std::vector<pat::Electron> > ElecJetIsolationFilter;
