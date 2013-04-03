#==============================================================================             
# Copyright (c) 2012, Bolagsverket AB. All rights reserved.
# title           : common_functions_db
# description     : Library for common functions used by the database scripts
#                   to update a database
# author          : fsv
# date            :20120709
# version         :0.1    
#==============================================================================

ERROR=42
OK=0

#-------------------------------------------------------------
# myExit(). Take care of Ctrl-C
# requires that $DB_ORACLE is defined
#-------------------------------------------------------------
myExit()
{
    echo
    echo 'You hit Ctrl-C, Nothing committed to:' ${DB_ORACLE}
}

trap 'myExit; exit ${ERROR}' SIGINT SIGQUIT

#-------------------------------------------------------------
# correctUser()
#-------------------------------------------------------------
correctUser()
{
   echo HOSTNAME $HOSTNAME

   case "$HOSTNAME" in

   'byggserver02' | 'utv1-appsrv100' |'utv2-appsrv100')
       return
       ;;
   *)
      if [[ $(id -un) != "urfapp" ]] ;
      then
           printErrorAndExit 'ERROR:You must be urfapp execute this script!'
       fi
       ;;
   esac
}

#-------------------------------------------------------------
# assert
# argument1 - condition
# argument2 - lineno
#-------------------------------------------------------------

assert ()                 #  If condition false,
{                         #+ exit from script
                          #+ with appropriate error message.

  if [ -z "$2" ]          #  Not enough parameters passed
  then                    #+ to assert() function.
    echo "Assertion failed:  \"$1\""
    echo "File \"$0\", line $lineno"    # Give name of file and line number.
    exit 42
  fi

  lineno=$2

  if [ ! $1 ] 
  then
    echo "Assertion failed:  \"$1\""
    echo "File \"$0\", line $lineno"    # Give name of file and line number.
    exit $E_ASSERT_FAILED
  fi  
}

#-------------------------------------------------------------
# checkFunction()
#-------------------------------------------------------------
checkFunction()
{
    true
}

#-------------------------------------------------------------
# yesOrNo()
# argument1 : sql script o be committed
#-------------------------------------------------------------
yesOrNo()
{

    while true
    do
        echo
        echo -n  'Do you want '$1 'to be committed to:' $DB_ORACLE '? [Y/n] '

        read CONFIRM
        
        case $CONFIRM in
            y|Y|'') 
              break ;;
            n|N)
              echo 'You declined. No commit to' $DB_ORACLE ' done'
              exit 42
              ;;
            *) echo "That is not valid input. Try again!"
        esac
    done
}

#-------------------------------------------------------------
# printErrorAndExit
# arguments : error text to be echoed
#-------------------------------------------------------------
printErrorAndExit()
{
    echo
    echo
    for var in "$@"
    do
        echo -n "$var"
    done
    echo 
    echo
    echo

    exit $ERROR
}

#-------------------------------------------------------------
# Check sqlfile
# argument1 : sql script o be checked
#-------------------------------------------------------------
checkSQLfile()
{
     SQLFILE=$1

     SUFFIX=$(echo $SQLFILE |awk -F . '{if (NF>1) {print $NF}}')

    # Check if sqlfile has correct suffix
    if [[ Z$SUFFIX != 'Zsql' ]];
    then
        printErrorAndExit 'ERROR:Wrong type of file:' $SQLFILE
    fi

    # Check if the sqlfile exist and not empty
    if [[ ! -s $SQLFILE  ]]; 
    then
        printErrorAndExit 'ERROR:File empty or do not exist:' $SQLFILE
    fi
}

#-------------------------------------------------------------
# checkProgram
# argument1: Executable binary
#-------------------------------------------------------------
checkBinary()
{
    BINARY=$(which $1)

    if [[ ! -s $BINARY && -x $BINARY ]]; 
    then
        printErrorAndExit 'ERROR: Not found or not executable:' $BINARY
    fi
}
#-------------------------------------------------------------
# checkSQLPlus()
# arguments: none
#-------------------------------------------------------------
checkSQLPlus()
{
    SQLPLUS=$(which sqlplus)

    if [[ ! -s $SQLPLUS && -x $SQLPLUS ]]; 
    then
        printErrorAndExit 'ERROR:sqlplus not found or not executable:' $SQLPLUS
    fi
}

#-------------------------------------------------------------
# Load database creds
# argument1 : file including creds for the database
# returns: connection string CONNECTION_STRING (global variable)
#-------------------------------------------------------------
loadDatabaseCreds()
{

    DATABASE_CFG=$1

    if [[ ! -s $DATABASE_CFG ]];
    then
        printErrorAndExit "ERROR: Could not find database configuration file : $DATABASE_CFG"
    fi

    # Read configuration file
    source $DATABASE_CFG
    
    # Make sure that variables are defined
    if [[ ! -n "$USER_ORACLE" ]];
    then
        printErrorAndExit "ERROR: Could not find user information in  configuration file: $DATABASE_CFG"
    fi

    if [[ ! -n "$PASS_ORACLE" ]];
    then
        printErrorAndExit "ERROR: Could not find pwd information in configuration file: $DATABASE_CFG"
    fi

    if [[ ! -n "$DB_ORACLE" ]];
    then
        printErrorAndExit "ERROR: Could not find database information in configuration file: $DATABASE_CFG"
    fi

    # Put everything together
    CONNECTION_STRING=$USER_ORACLE/$PASS_ORACLE@$DB_ORACLE
}
 
#-------------------------------------------------------------
# check database()
# requires that $CONNECTION_STRING is defined!
#-------------------------------------------------------------
# TODO:
# If not defined in tnsnames.ora? what to do?
checkDatabase()
{
    connectionStringDefined
   
    assert $CONNECTION_STRING $LINENO

    TMP="select * from user_tablespaces where TABLESPACE_NAME='RDMS_DATA';  exit;"
    echo $TMP | sqlplus $CONNECTION_STRING  > /dev/null 2>&1

    ERRORCODE=$?
    # Check the return code from SQL Plus
    if [ $ERRORCODE != 0 ]
    then
      printErrorAndExit "ERROR: Failed to connect to $DB_ORACLE mismatch with tnsnames.ora? ,  ErrorCode: $ERRORCODE"
    fi
}

#-------------------------------------------------------------
# checkNoRows()
# argument1 : table to check
#-------------------------------------------------------------
checkNoRows()
{
    connectionStringDefined
    ROWS="select count(*) from ${1};"
    echo $ROWS | sqlplus $CONNECTION_STRING | awk '/^[ \t]+[[:digit:]]/ {gsub(/ */,"",$0); print $0 } '
}

#-------------------------------------------------------------
# doCommit()
# requires that $CONNECTION_STRING is defined!
#-------------------------------------------------------------
doCommit()
{
    connectionStringDefined

    # Go ahead, do it
    sqlplus $CONNECTION_STRING < ${1} > /dev/null 2>&1

    ERRORCODE=$?

    # Check the return code from SQL Plus
    if [ $ERRORCODE != 0 ]
    then
      printErrorAndExit "ERROR: The SQL Plus Command Failed. ErrorCode: $ERRORCODE"
    fi
    
    echo
    echo
    echo $1  "successfully committed!"
    echo
}

#-------------------------------------------------------------
# connectionStringDefined()
#-------------------------------------------------------------
connectionStringDefined()
{
    if [[ ! -n "$CONNECTION_STRING" ]];
    then
        printErrorAndExit "ERROR: Connection string not defined"
    fi
}

#-------------------------------------------------------------
# checkEnvironment()
# argument : $1 File with database creds
#-------------------------------------------------------------
checkEnvironment()
{
    # Check SQLPlus
    checkSQLPlus

    # Load connection string variables for database
    assert $1 $LINENO
    loadDatabaseCreds $1

    # Make sure that the database is up and running
    checkDatabase
}


