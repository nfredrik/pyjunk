#!/usr/bin/env sh
#
# Copyright Bolagverket AB
#

set -x

# Get the workspace filepath and buildfile from Jenkins
export JENKINS_HOME=$1
export WORKSPACE=$2
export BUILDFILE=$3
export ORACLE_CONN=$4

export TMP=$WORKSPACE/tmp

# Create a tmpdir for list files and intermediate files  
if [[ ! -d $TMP ]]; then
   mkdir $TMP
fi

# Place for lst-files,Intermediate files and linage files
export HOME_APLIC_LST=$TMP
export COMPILCOB_TMP=$TMP
export HOME_APLIC_LINAGE=$TMP

# Tells where the wrapper for procob resides
export COBPATH=$WORKSPACE/build

# Tells where the copybooks resides, tuxedo includes first followed by mq and the rest
export TUXEDOINC=/u01/app/oracle/product/11gR1/tux_1/tuxedo11gR1/cobinclude
export MQINC=/srv/mq/opt/mqm/inc	
export HPFWKINC=$WORKSPACE/include

export COBCPY=$TUXEDOINC:$MQINC:$HPFWKINC:$WORKSPACE/src/pgm/SYSTEM:$WORKSPACE/src/pgm/include:$WORKSPACE/src/pgm/PROD/UCPROC:\
$WORKSPACE/src/pgm/RDMS/DEFS:$WORKSPACE/src/pgm/PROD/LKSCRE:$WORKSPACE/src/pgm/PROD/FISCRE:$WORKSPACE/src/pgm/PROD/PNSCRE:\
$WORKSPACE/src/pgm/PROD/BGSCRE:$WORKSPACE/src/pgm/PROD/NBSCRE:$WORKSPACE/src/pgm/PROD/LVSCRE:$WORKSPACE/src/pgm/PROD/EXSCRE:\
$WORKSPACE/src/pgm/PROD/AVSCRE:$WORKSPACE/src/pgm/PROD/ARSCRE:$WORKSPACE/src/pgm/PROD/FASCRE:$WORKSPACE/src/pgm/PROD/FOSCRE:\
$WORKSPACE/src/pgm/PROD/FFSCRE:$WORKSPACE/src/pgm/PROD/UHSCRE:$WORKSPACE/src/pgm/PROD/FSSCRE:$WORKSPACE/src/pgm/PROD/INSCRE:\
$WORKSPACE/src/pgm/PROD/KKSCRE:$WORKSPACE/src/pgm/PROD/OVSCRE:$WORKSPACE/src/pgm/PROD/BOSCRE:$WORKSPACE/src/pgm/PROD/RESCRE:\
$WORKSPACE/src/pgm/PROD/LISCRE:$WORKSPACE/src/pgm/PROD/STSCRE

echo COBCPY $COBCPY

# Set COBOPT
export COBOPT=$(cat <<EOF
-C "p(superpre) preprocess(cobsql) COBSQLTYPE==ora NOMAKESYN end-cobsql config==${WORKSPACE}/build/compilcob.procob USERID==${ORACLE_CONN} p(cp) s sy endp"
-C LISTPATH($TMP)
-C LIST()
-C VERBOSE
EOF
)

echo COBOPT  $COBOPT


# Launch ant, complete or single
export MFJAR=/opt/microfocus/VisualCOBOL2.0/lib/mfant.jar
export CLASSPATH=$MFJAR:/usr/lib64/jvm/java-1_6_0-ibm-1.6.0/jre/lib

if [[ -z "$5" ]]; then
    ant -nice 10  -lib $MFJAR  -f $BUILDFILE

else
    for module in "${@:5}"
    do
        FILEPATH=$($JENKINS_HOME/getmod.py $WORKSPACE/test.pkl $module)
        ant -nice 10  -lib $MFJAR  -f $BUILDFILE New_Configuration.FileCompile -Dfilename=$FILEPATH -Dfile.basename=$module
    done
fi