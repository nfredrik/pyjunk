
# http://stackoverflow.com/questions/4165135/how-to-use-while-read-bash-to-read-the-last-line-in-a-file-if-there-s-no-new

set -x

function to_posix 
{ 

	if [[ $@ =~ ^([0-9]{2})([0-9]{2})([0-9]{2})([0-9]{2})([0-9]{2})([0-9]{2})(.*)$ ]] ; then
		year=${BASH_REMATCH[1]} 
		mon=${BASH_REMATCH[2]} 
		day=${BASH_REMATCH[3]} 
		hours=${BASH_REMATCH[4]} 
		min=${BASH_REMATCH[5]} 
		secs=${BASH_REMATCH[6]} 
		msg=${BASH_REMATCH[7]}
        echo "20$year-$mon-$dayT$hours:$min:$secs$msg"
    fi

}



while IFS= read -r LINE || [[ -n "$LINE" ]]; do
    to_posix $LINE
done

exit 1
