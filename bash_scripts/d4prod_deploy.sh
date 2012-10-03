
set -x 

TAG_NAME=$1
WORKSPACE=$2
DELIVERY=/program/Arkiv-Leveranser


#  Revisions:
#  0.1 Removed ECL from delivery, added DB instead!
#


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


####################################################
echo 'Remove tmp directory!'
####################################################

rm -fr $WORKSPACE/tmp/pgm
rm -fr $WORKSPACE/tmp/ecl
rm -fr $WORKSPACE/tmp/dps

####################################################
echo 'PGM!'
####################################################
    
    TMP_DEST=$WORKSPACE/tmp/pgm/$TAG_NAME
    TMP_DEST_SO=$TMP_DEST/cobol/so
    TMP_DEST_LINAGE=$TMP_DEST/cobol/linage
    
    # Create the destination directory if not already there
    if [[ ! -d $TMP_DEST_SO ]]; then
        mkdir -p $TMP_DEST_SO 
        mkdir -p $TMP_DEST_LINAGE 
    fi
    
    # Copy shared object files
#    cp $WORKSPACE/fwk/us/cobol/so/*.so $TMP_DEST_SO  
#    cp $WORKSPACE/fwk/us/cobol/linage/*.linage $TMP_DEST_LINAGE

    cp $WORKSPACE/src/New_Configuration.bin/*.so $TMP_DEST_SO  
    cp $WORKSPACE/tmp/*.linage $TMP_DEST_LINAGE
    
    
    doIt $TAG_NAME PGM $TMP_DEST


####################################################
echo 'DPS!'
####################################################
    
    TMP_DEST=$WORKSPACE/tmp/dps/$TAG_NAME
    
    # Create the destination directory if not already there
    if [[ ! -d $TMP_DEST ]]; then
        mkdir -p $TMP_DEST 
    fi
    
    cp -r  $WORKSPACE/src/dps/* $TMP_DEST  
    # Temporary solution transar.txt will later be
    # be a part of dps package
    #cp  $WORKSPACE/pgm/behor/transar.txt $TMP_DEST      
    doIt $TAG_NAME DPS $TMP_DEST


####################################################
echo 'DB!'
####################################################
    
    TMP_DEST=$WORKSPACE/tmp/db/$TAG_NAME
    
    # Create the destination directory if not already there
    if [[ ! -d $TMP_DEST ]]; then
        mkdir -p $TMP_DEST 
    fi
    
    cp -r  $WORKSPACE/src/db/* $TMP_DEST  

    chmod ugo+x $(find . -name *.sh)

    doIt $TAG_NAME DB $TMP_DEST

    
####################################################
echo 'ECL!'
####################################################
    
    TMP_DEST=$WORKSPACE/tmp/ecl/$TAG_NAME
    
    # Create the destination directory if not already there
    if [[ ! -d $TMP_DEST ]]; then
        mkdir -p $TMP_DEST 
    fi
    
    cp -r  $WORKSPACE/src/ecl/* $TMP_DEST  
    # make all ECLs executable
    chmod -R ugo+x $TMP_DEST  

    doIt $TAG_NAME ECL $TMP_DEST

    

# Last but not least, copy the CHANGES.txt
    cp   $WORKSPACE/*.txt  ${DELIVERY}/${TAG_NAME}
    cp   $WORKSPACE/*.html  ${DELIVERY}/${TAG_NAME}
    sudo chown -R urfapp:framework ${DELIVERY}/${TAG_NAME}/*.txt
    sudo chown -R urfapp:framework ${DELIVERY}/${TAG_NAME}/*.html
    exit 0    




