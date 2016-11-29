

numReqs=10
url=https://mud0dqdiye.execute-api.us-west-2.amazonaws.com/prod/api/helloapi


if [ -z "$1" ]
then
        echo "Param 1 - NumRequests not specified - using Default : 10"
else
        numReqs=$1
fi

outfile="output_loop_${numReqs}.txt"
rm -f ${outfile}

echo URL is:${url}
echo NumReqs is:${numReqs}
echo outfile is:${outfile}

echo "Result\tTimeType\tTime" >> ${outfile}

for i in `seq 1 ${numReqs}`;
do
        echo "`./runAndTimeCurl.sh "msg_${i}" ${url} 2>&1 | sort | head -3 | tail -2 | tr "\n" "\t" `" >> $outfile &
done

echo "done"

