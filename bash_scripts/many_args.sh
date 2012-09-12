

#echo "$*" $*

#echo "$@" $@

#echo "$@" $@

ALL=$(echo "$@")

NISSE=1



#for i in  $ALL
#do
#    echo $i
# 
#done


for item in "${@:2}"
do
    echo "$item"
done
