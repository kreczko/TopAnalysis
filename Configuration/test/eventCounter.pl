#!/usr/bin/env/ perl

# script to run over a list of input files (use of wildcard is allowed) and
# to grep different cuts. These cuts are expected to be named AND ordered as:
#
#   (1) muonEtaCut
#   (2) muonPtCut
#   (3) jetsEtaCut
#   (4) jetsPtCut
#
# It sums num1 ... num8 before and after the cut was applied and puts the
# result out to screen.

# get list of input files
my @myfiles = @ARGV;

# initialize error counters
my $err1   = 0;

# initialize event counters
my $nom1   = 0;
my $nom2   = 0;
my $nom3   = 0;
my $nom4   = 0;
my $nom5   = 0;
my $nom6   = 0;
my $nom7   = 0;
my $nom8   = 0;

my $denom1 = 0;
my $denom2 = 0;
my $denom3 = 0;
my $denom4 = 0;
my $denom5 = 0;
my $denom6 = 0;
my $denom7 = 0;
my $denom8 = 0;

# loop over each file and accumulate the event numbers
foreach my $file (@myfiles) {

    # print current file name
    print "... processing file $file \n";

    # get the grep output from the shell

    my @semiLepMuonEta = `grep semiLepMuonEta $file | grep 'out of'`;
    my @semiLepMuonPt  = `grep semiLepMuonPt  $file | grep 'out of'`;
    my @semiLepJetsEta = `grep semiLepJetsEta $file | grep 'out of'`;
    my @semiLepJetsPt  = `grep semiLepJetsPt  $file | grep 'out of'`;

    # check the pattern and extract the numbers, if succesful
    # accumulate else voice error message ; first occurrence
    # semi leptonic second dileptonic preselection
    my $failed = 0;
    if($semiLepMuonEta[0] =~ /\w\s+:\s+(\d+)\s+\(\s+(\d+\.?\d*)\)\s+\w+\s\w+\s+(\d+)\s+\(\s+(\d+\.?\d*)\)/) {
      $nom1   = $nom1   + $1;
      $denom1 = $denom1 + $3;
    } else {
      $failed = 1;
      print ">> ERROR: didn't find semiLepMuonEta from $file <<\n";
    };
    if($semiLepMuonPt[0]  =~ /\w\s+:\s+(\d+)\s+\(\s+(\d+\.?\d*)\)\s+\w+\s\w+\s+(\d+)\s+\(\s+(\d+\.?\d*)\)/) {
      $nom2   = $nom2   + $1;
      $denom2 = $denom2 + $3;
    } else {
      $failed = 1;
      print ">> ERROR: didn't find semiLepMuonPt  from $file <<\n";
    };
    if($semiLepJetsEta[0] =~ /\w\s+:\s+(\d+)\s+\(\s+(\d+\.?\d*)\)\s+\w+\s\w+\s+(\d+)\s+\(\s+(\d+\.?\d*)\)/) {
      $nom3   = $nom3   + $1;
      $denom3 = $denom3 + $3;
    } else {
      $failed = 1;
      print ">> ERROR: didn't find semiLepJetsEta from $file <<\n";
    };
    if($semiLepJetsPt[0]  =~ /\w\s+:\s+(\d+)\s+\(\s+(\d+\.?\d*)\)\s+\w+\s\w+\s+(\d+)\s+\(\s+(\d+\.?\d*)\)/) {
      $nom4   = $nom4   + $1;
      $denom4 = $denom4 + $3;
    } else {
      $failed = 1;
      print ">> ERROR: didn't find semiLepJetsPt  from $file <<\n";
    };
    if($failed == 1){ $err1 = $err1 + 1 }
  }; # end loop over files

# output record
print "\n";
print "----------------------------------------------";
print "\n  Accumulated errors    :\n";
print "----------------------------------------------";
print "\n";
print "  N/A record: \t $err1 \n";
print "----------------------------------------------";
print "\n  Accumulated statistics:\n";
print "----------------------------------------------";
print "\n            \t before: \t after: \n";
print "  muonEtaCut: \t $denom1 \t\t $nom1 \n";
print "  muonPtCut : \t $denom2 \t\t $nom2 \n";
print "  jetsEtaCut: \t $denom3 \t\t $nom3 \n";
print "  jetsPtCut : \t $denom4 \t\t $nom4 \n";
print "----------------------------------------------\n";

exit;
