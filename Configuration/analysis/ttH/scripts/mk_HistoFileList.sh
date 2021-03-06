#!/bin/zsh



if [ $# -ge 2 ] ; then
  echo "Usage: $0"
  echo "Usage: $0 mva"
  echo "Usage: $0 <selectionRoot directory>"
  exit 1
fi


inputDir="selectionRoot"
outputDir="FileLists_plot"

if [[ "x$1" != "x" ]] ; then
    inputDir="$1"
fi


if [[ "$1" == mva ]] ; then
    inputDir="mvaInput"
    outputDir="FileLists_mva"
fi


mkdir -p ${outputDir}
rm ${outputDir}/HistoFileList_*


foreach sample (run qcd dyee dymumu dytautau ww wz zz wtolnu single ttbarbg ttbarsignal ttbarH ttbarW ttbarZ)
    foreach channel (ee emu mumu)
        foreach systematic (Nominal \
                            mH110 mH115 mH120 mH1225 mH1275 mH130 mH135 mH140
                           )
            if [ -d ${inputDir}/$systematic/$channel ] ; then
                ls -1 ${inputDir}/$systematic/$channel/${channel}_$sample*.root >> ${outputDir}/HistoFileList_$systematic\_$channel.txt
                ls -1 ${inputDir}/$systematic/$channel/${channel}_$sample*.root >> ${outputDir}/HistoFileList_$systematic\_combined.txt
            fi
        end
    end
end
