#!/usr/bin/env sh
#
# Mål: Att få en ren kompilering i MicroFocus-miljö med inga eller små beroenden
# på HPs byggmiljö. Wrappern, superpre.so, kommer vi inte ifrån men det andra kanske
#
#  120824:  Cobol går att bygga från Jenkins! Här använder man antcobolBuild som kommer från .cobolBuild.
#  TODO: - bygg bort build checkouten
#        - definera vad alla ställen som pekar på /tmp  idag
#        - oracle creds, flexibla... idag BYGGDB03   
#        - Sätt alla hw-pather som variabler, exvis till procob, java osv
#

# 120828 - Det som vi är beroende av idag (som idag ligger under .../fwk/build):
#    superpre.so       -  wrapper for att anropa procob
#    compilcob.procob  -  argument till procob
#    compilcob.cobopt  -  kompilatordirektiv, kan inte att dom skickas till kompilatorn dock. kolla med HP
#          Skrev TR här. compilcob.cobopt kopierat till directives-file and it's included in antcobolBuild

#
# TODO
#
#   Howto remove COBOPT first assignment?
#   remove tmp dir ...
#   specify variables/constants? for TUXEDO and MQ includes 
#   try to remove copopt.txt
#   move compilcob.cobopt to directives and include in antcobolBuild
#   hardcoded path to New_Configuration.bin.
#

set -x

# Get the workspace filepath from Jenkins
export WORKSPACE=$1

export BUILDFILE=$2

export TMP=$WORKSPACE/tmp

# Create a tmpdir for list files. 
# This an work around for an error superpre.so. Remove this when corrected. Check TR 31971  
if [[ ! -d $TMP ]]; then
   mkdir $TMP
fi

# From compilcob.config from before ... Need to be define at this point funny ....
COBOPT=0

# Place for lst-files
export HOME_APLIC_LST=$TMP

# Intermediate files
export COMPILCOB_TMP=$TMP

# We need to place the linage files somewhere
export HOME_APLIC_LINAGE=$TMP

# Tells where the wrapper for procob resides
export COBPATH=$WORKSPACE/build

# Tells where the copybooks resides, tuxedo includes first followed by mq  and the rest
export COBCPY=/u01/app/oracle/product/11gR1/tux_1/tuxedo11gR1/cobinclude:/srv/mq/opt/mqm/inc:$WORKSPACE/include:$WORKSPACE/src/pgm/system:${WORKSPACE}/src/pgm/include:$WORKSPACE/src/pgm/PROD/UCPROC:$WORKSPACE/src/pgm/RDMS/DEFS


# Oracle creds for byggserver02 database
export ORACLE_USER=bygg_user
export ORACLE_PWD=bygguser
export ORACLE_DB=BYGGDB03

# Set COBOPT
export TMPDIR=$WORKSPACE/pgm/
export COBOPT=${WORKSPACE}/src/cobopt.txt > ${COBOPT}

cat > ${COBOPT} <<!FIN
-C "p(superpre) preprocess(cobsql) COBSQLTYPE==ora NOMAKESYN end-cobsql config==${WORKSPACE}/build/compilcob.procob USERID==${ORACLE_USER}/${ORACLE_PWD}@${ORACLE_DB} p(cp) s sy endp"
-C LISTPATH($TMP)
-C LIST()
-C VERBOSE
!FIN

# The generated cobopt-file need to be in New_Configuration.bin to make linking work ... funny

cp ${WORKSPACE}/src/cobopt.txt ${WORKSPACE}/src/New_Configuration.bin/

# Launch ant !

export MFJAR=/opt/microfocus/VisualCOBOL2.0/lib/mfant.jar
export CLASSPATH=$MFJAR:/usr/lib64/jvm/java-1_6_0-ibm-1.6.0/jre/lib


ant -nice 10  -lib $MFJAR  -f $BUILDFILE
