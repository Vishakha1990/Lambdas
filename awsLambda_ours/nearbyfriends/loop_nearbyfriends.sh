

opDir=./burst_scaling
numReqs=10
url=https://jkf02xx1kl.execute-api.us-east-2.amazonaws.com/prod/api/findnearbyfriends


if [ -z "$1" ]
then
        echo "Param 1 - NumRequests not specified - using Default 10"
else
        numReqs=$1
fi

outfile=$opDir"/burst_${numReqs}.txt"
rm -f ${outfile}

echo outfile is:${outfile}

echo "Result\tTimeType\tTime" >> ${outfile}

for i in `seq 1 ${numReqs}`;
do
        #echo "`./runAndTimeCurl.sh 2>&1 | sort | head -3 | tail -2 | tr "\n" "\t" `" >> $outfile &
	echo "`./runAndTimeCurl.sh 2>&1 | sort | tail -4 | tr "\n" "\t" `" >> $outfile &
done

echo "done"

