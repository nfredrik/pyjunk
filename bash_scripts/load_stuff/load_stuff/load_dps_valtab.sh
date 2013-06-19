#!/usr/bin/env ksh 
#==============================================================================             
# Copyright (c) 2012, Bolagsverket AB. All rights reserved.
# title           :load_dps_valtab.sh
# description     :This script will commit a DPS_VALTAB.sql to database specified
#                  in a configuration file. Alter DATABASE_CFG_FILE  to run against
#                   developement, system test, acceptence or production
# author          :fsv
# date            :20120709
# version         :0.1    
#==============================================================================


PTH=$(cd $(dirname $0); pwd)
GLOB_COMMON_FUNCTION_LIB="${PTH}/common_functions_db.sh"

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
    echo HOSTNAME $HOSTNAME

    case "$HOSTNAME" in

    'byggserver02' | 'utv1-appsrv100' |'utv2-appsrv100')

        echo 'Load utv2-appsrv100 config file'
        source $UTV_VARS
        ;;

    'system1-appsrv100' |'system2-appsrv100'|'system3-appsrv100'|'system4-appsrv100'|'system5-appsrv100'|'system6-appsrv100'|'system7-appsrv100' )
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

    echo  DATABASE_CFG_FILE  $DATABASE_CFG_FILE 
    echo  DPS_VALTAB $DPS_VALTAB
    echo  OLTP_VALTAB $OLTP_VALTAB
    echo  TTAB_USER $TTAB_USER
    echo  IPCKILL $IPCKILL_PATH
    echo  TRANSAR_PATH $TRANSAR_PATH
    echo  TTAB_PATH $TTAB_PATH
}

#-------------------------------------------------------------
# loadAlterSqls
#-------------------------------------------------------------
loadAlterSqls()
{

    ASCREENS=$(ls $ALTER_SCREENS/*.sql | wc |awk '{print $1}' ) 

    if [[  $ASCREENS -eq 0  ]]; 
      then
          echo 
          echo 'WARNING:could not find any alter scripts'
          exit 42
    fi

    for sqlfile in  $(ls $ALTER_SCREENS/*.sql)
    do
        echo 'Commiting:' $(basename $sqlfile)
        doCommit $sqlfile
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

    # Check that it's exactly one argument!
    if [[ $# != 0 ]]
    then
        echo 'Usage:' `basename ${0}`
        exit $ERROR
    fi
 
    # Check that DPS_VALTAB.sql exists
    checkSQLfile $DPS_VALTAB

    # Check number of rows before
    echo -n 'Numbers of rows before:'
    checkNoRows "dps_valtab"
 
    # Make sure that the user wants to commit to _this_ database!
    yesOrNo $DPS_VALTAB


    # It was okey go for it!
    doCommit $DPS_VALTAB

    # Check number of rows after
    echo -n 'Numbers of rows after:'
    checkNoRows "dps_valtab"

    # Check if HP-SCREENS.sql and screens.sql needs to be commited
    yesOrNo "HP-SCREENS.sql and screens.sql"

    doCommit $HP_SCREENS
    doCommit $SCREENS

    # Check if all alter sqls  needs to be commited
    yesOrNo "all alter scripts"
    loadAlterSqls
    
    exit $OK
}

# Launch the main routine
main $@

