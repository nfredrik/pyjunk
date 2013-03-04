#!/usr/bin/env sh

#set -x

PTH=$(cd $(dirname $0); pwd)
GLOB_COMMON_FUNCTION_LIB="${PTH}/common_functions_db.sh"

#-------------------------------------------------------------
# withinTime
#-------------------------------------------------------------
withinTime()
{

    NOW=$(date +"%H%M")
    MORNING='0600'
    EVENING='1900'

    if [[ $NOW < $EVENING ||  $NOW > $MORNING  ]]
    then
        echo "WARNING:Time now: ${NOW}. Later than: ${MORNING} and earlier than: ${EVENING}, , check if okey!"
        return 0
    fi

    return 1
}

#-------------------------------------------------------------
# functionDefined
#-------------------------------------------------------------
functionDefined()
{
    FUNCTION_NAME=$1

    if [[ -z "$FUNCTION_NAME" ]];
    then
        echo
        echo 'Error, Not defined:' $FUNCTION_NAME
        echo
        exit 42
    fi

    declare -F "$FUNCTION_NAME" > /dev/null 2>&1

    # Bug? very strange. If an variable is accessed in the library it
    # possible to call functions within the library othwise not...
    echo 'errorcode' $ERROR > /dev/null 2>&1
    ECODE=$?
    if [[ $ECODE != 0 ]];
    then
        echo
        echo 'Error, Could not find:' $FUNCTION_NAME $ECODE
        echo
        exit 42
    fi
}

#-------------------------------------------------------------
# loadCommonFunctions
#-------------------------------------------------------------
loadCommonFunctions()
{

    COMMON_FUNCTION_LIB=$1

    # Check that the files exists
    if [[ ! -s $COMMON_FUNCTION_LIB  ]];
    then
        echo
        echo 'ERROR:File empty or do not exist:' $COMMON_FUNCTION_LIB
        exit 42
    fi

    # Load common library functions
    source $COMMON_FUNCTION_LIB

    # verify that we have needed functions
    functionDefined checkFunction && checkFunction
}

#-------------------------------------------------------------
# checkFileExist
#-------------------------------------------------------------

checkFileExist()
{

    # Check that the files exists
    if [[ ! -s $1  ]];
    then
        echo
        echo 'ERROR:File empty or do not exist:' $1
        exit 42
    fi
}

#-------------------------------------------------------------
# loadVars
#-------------------------------------------------------------
loadVars()
{
    PTH=$(cd $(dirname $0); pwd)
    UTV_VARS="${PTH}/utv_settings.env"
    SYSTEST_VARS="${PTH}/systest_settings.env"
    ACCEPTENCE_VARS="${PTH}/accept_settings.env"
    PRODUCTION_VARS="${PTH}/prod_settings.env"
    HOSTNAME=$(hostname)
    #echo HOSTNAME $HOSTNAME

    case "$HOSTNAME" in

    'byggserver02' | 'utv1-appsrv100' |'utv2-appsrv100')

        #echo 'Load utv2-appsrv100 config file'
        source $UTV_VARS
        ;;

    'system1-appsrv100' |'system2-appsrv100'|'system3-appsrv100'|'system4-appsrv100'|'system5-appsrv100'|'system6-appsrv100'|'system7-appsrv100' \
)
        echo 'Load systest config file'
        checkFileExist $SYSTEST_VARS
        source $SYSTEST_VARS
        ;;

    'dh1-accept-appsrv100')
        echo 'Load acceptance config file'
        checkFileExist $ACCEPTENCE_VARS
        source $ACCEPTENCE_VARS
        ;;

    'dh1-prod-appsrv100' | 'dh2-prod-appsrv100')
        echo 'Load production config file'
        checkFileExist $PRODUCTION_VARS
        source $PRODUCTION_VARS
        ;;
    *)
        echo
        echo 'Did not find a configuration for this machine:${HOSTNAME}'
        exit 42
        ;;
    esac

#    echo  DATABASE_CFG_FILE  $DATABASE_CFG_FILE
#    echo  DPS_VALTAB $DPS_VALTAB
#    echo  OLTP_VALTAB $OLTP_VALTAB
#    echo  TTAB_USER $TTAB_USER
#    echo  IPCKILL $IPCKILL_PATH
#    echo  TRANSAR_PATH $TRANSAR_PATH
#    echo  TTAB_PATH $TTAB_PATH
}


#-------------------------------------------------------------
# echoRowsInTable
#-------------------------------------------------------------
echoRowsInTable()
{
    # Prereq: Every sql-file generated from sql developer shall
    # have this comment
    table=$(grep "REM INSERTING into" $1 | awk '{print $4}')
    echo -n "number of rows: "
    checkNoRows $table
}

#-------------------------------------------------------------
# commitTypdata
#-------------------------------------------------------------
commitTypdata()
{
    for sql in $(find . -name *.sql)
    do
        doCommit $sql
        echoRowsInTable $sql
    done
}

#-------------------------------------------------------------
# main
#-------------------------------------------------------------
main()
{

    # Load library file
    loadCommonFunctions $GLOB_COMMON_FUNCTION_LIB

    # Load library file
    loadVars

    # Check the environment
    checkEnvironment $DATABASE_CFG_FILE

    # Check arguments 
    # $1 - path to tarfile
    # $2 - directory where to unpack

    # Check that we have our arguments
    if [[ $# != 1 ]]
    then
        echo 'Usage:' `basename ${0}` ' <tarfile> <directory to unpack to>'
        exit $ERROR
    fi

    # Check if tarfile and path exists
    TARFILE=$1
#    DIRECTORY=$2
    if [[ ! -s $TARFILE ]]
    then
       echo "could not find tarfile"
       exit 42
    fi

#    if [[ ! -d $DIRECTORY ]]
#    then
#       echo "could not find directory!"
#       exit 42
#    fi

    DIRECTORY=$(mktemp -d)


    # Verify that tarfile okey
    tar tvf  $TARFILE  > /dev/null 2>&1

    if [[ $? != 0 ]]
    then
       echo "tarfile corrupt exiting!"
       rm -fr $DIRECTORY
       exit 42
    fi

    # Remember base
    pushd . > /dev/null
 
    # Unpack tarfile and put in path
    cp  $TARFILE $DIRECTORY

    cd $DIRECTORY

    # Remove old sql if same directory is used
    # rm -fr `find .  -name *.sql -type f`

    tar xvf  $TARFILE > /dev/null 2>&1


    # Check if within time
    withinTime

    if [[ $? == 0 ]]
    then
       yesOrNo 'typdata'
    fi

    # Okey to commit!
    commitTypdata
 
    # Back to base
    popd > /dev/null

    rm -fr $DIRECTORY
}

# Launch the main routine
main $@

