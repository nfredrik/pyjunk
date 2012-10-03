
set -x 

TAG_NAME=$1
WORKSPACE=$2
DPS=$3
DB=$4
TUXEDO=$5
PGM=$6

DELIVERY=/program/Arkiv-Leveranser

#######################################################################
assert ()                 #  If condition false,
{                         #+ exit from script
                          #+ with appropriate error message.
    E_PARAM_ERR=98
    E_ASSERT_FAILED=99


    if [ -z "$2" ]          #  Not enough parameters passed
    then                    #+ to assert() function.
        return $E_PARAM_ERR   #  No damage done.
    fi

    LINENO=$2

    if [ ! $1 ] 
    then
      echo "Assertion failed:  \"$1\""
      echo "File \"$0\", line $LINENO"    # Give name of file and line number.
      exit $E_ASSERT_FAILED
    fi  
}

#######################################################################



# $1  -  name of module, tag
# $2  -  name of module, i.e DPS, ECL 
# $3  -  path to temporary directory
doIt()
{
    TAG_NAME=$1
    TAG_NAME_MODULE=${TAG_NAME}_$2
    TMP_DEST=$3

    DELIVERY_DIR=${DELIVERY}/${TAG_NAME}
    
    SMALL=$(echo $2 |  tr '[:upper:]' '[:lower:]')
    
    # Remove all subversion stuff
    rm -fr `find ${TMP_DEST}  -name .svn -type d`
    
    assert $? $LINENO

    # assert "5 -lt 4"  $LINENO

    # Assign to right owner and group
    sudo chown -R urfapp:framework $TMP_DEST
    
    # Make a package
    cd tmp
    rm -fr $TAG_NAME_MODULE.tar
    tar cvf $TAG_NAME_MODULE.tar $SMALL/$TAG_NAME  


    if [[ ! -d ${DELIVERY_DIR} ]]; then
        mkdir -p $DELIVERY_DIR
    fi
    
    # Copy to delivery directory
    mv $TAG_NAME_MODULE.tar $DELIVERY_DIR
    sudo chown  urfapp:framework $DELIVERY_DIR/$TAG_NAME_MODULE.tar
    
    cd ..
    
    # Back again to be able to remove
    sudo chown -R jenkins:users $TMP_DEST
    
    # remove all temporary stuff
    rm -fr $TMP_DEST

}
#######################################################################





####################################################
echo 'PGM!'
####################################################

    #  Check if there's any PGM to deliver
    if [[ $PGM = true ]]; then
    
        TMP_DEST=tmp/pgm/$TAG_NAME
        TMP_DEST_SO=$TMP_DEST/cobol/so
    
        # Create the destination directory if not already there
        if [[ ! -d $TMP_DEST_SO ]]; then
            mkdir -p $TMP_DEST_SO 
        fi
    
        # Copy shared object files
        cp $WORKSPACE/src/fwk/us/cobol/so/*.so $TMP_DEST_SO  

        #    cp $WORKSPACE/pgm/New_Configuration.bin/*.so $TMP_DEST_SO  
    
        doIt $TAG_NAME PGM $TMP_DEST

    else
       echo 'No PGM to deliver'
    fi

####################################################
echo 'DPS!'
####################################################

    #  Check if there's any DPS to deliver
    if [[ $DPS = true ]]; then

        TMP_DEST=$WORKSPACE/tmp/dps/$TAG_NAME

        # Create the destination directory if not already there
        if [[ ! -d $TMP_DEST ]]; then
            mkdir -p $TMP_DEST
        fi

        cp -r  $WORKSPACE/src/dps/* $TMP_DEST

        doIt $TAG_NAME DPS $TMP_DEST

    else
       echo 'No DPS to deliver'
    fi


####################################################
echo 'DB!'
####################################################

    #  Check if there's any DB to deliver
    if [[ $DB = true ]]; then

        TMP_DEST=$WORKSPACE/tmp/db/$TAG_NAME

        # Create the destination directory if not already there
        if [[ ! -d $TMP_DEST ]]; then
            mkdir -p $TMP_DEST
        fi

        cp -r  $WORKSPACE/src/db/* $TMP_DEST

        chmod ugo+x $(find . -name *.sh)

        doIt $TAG_NAME DB $TMP_DEST

    else
       echo 'No DB to deliver'
    fi

####################################################
echo 'TUXEDO!'
####################################################

    #  Check if there's any DB to deliver
    if [[ $TUXEDO = true ]]; then

       echo 'TUXEDO to deliver!!!'
    else
       echo 'No TUXEDO to deliver'
    fi


    exit 0