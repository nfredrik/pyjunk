#trap "echo Booh!" SIGINT SIGTERM
#echo "pid is $$"

do_check()
{
    if [  $1 -ne 0 ]; then echo ECL did exit with $1 on line $2; fi
}
set -x



./divzero; do_check $? $LINENO

./bad; do_check $? $LINENO
