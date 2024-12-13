rm input_modified.txt
ex -c 'source day3.vim' input.txt

TOT=0
FILTERED_TOT=0
ENABLED=1

for i in $( cat input_modified.txt )
do
	if [[ $i == '+' ]]
	then
		ENABLED=1
		continue
	elif [[ $i == '-' ]]
	then
		ENABLED=0
		continue
	fi
	echo $i
	CURRENT=$(( $i ))
	TOT=$(( $TOT + $CURRENT ))
	if [[ $ENABLED == '1' ]]
	then
		FILTERED_TOT=$(( $FILTERED_TOT + $CURRENT ))
	fi
done

printf "Total mult without filtering: $TOT\n"
printf "Total mult with filtering: $FILTERED_TOT\n"
