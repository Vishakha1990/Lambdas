
#url=https://nehatesting.azurewebsites.net/api/HttpTriggerCSharp1?code=d1vcyncMHpLajNlaxOYiPJZVsTLTp3ruQ/gXiRgdilEB6SlgP4hbqQ==


#./util/start-cluster.py
#./util/setup.py --appdir pychat --appfile lambda_func.py

numReqs=10
url=`head -2 ~/gitRepository/Lambdas/applications/pychat/static/config.json | tail -1 | awk -F '":' '{print $2}' | xargs`
#xargs trims space and quotes
ext=""

if [ -z "$1" ]
then
	echo "Param 1 - NumRequests not specified - using Default : 10"
else
	numReqs=$1
fi

if [ $2 == "-v" ]
then
	echo "-v param passed : verbose.. output not trimmed"
	ext="_v"
fi

outfile="output_loop_${numReqs}${ext}.txt"
rm -f ${outfile}

echo URL is:${url}
echo NumReqs is:${numReqs}
echo outfile is:${outfile}

echo "Result\t\tTimeType\tTime" >> ${outfile}

if [ $2 == "-v" ]
then
	for i in `seq 1 ${numReqs}`;
	do
	        #echo $i
	        echo "`./runAndTimeCurl.sh "msg_${i}" ${url} 2>&1 `" >> $outfile & 
	done
	exit
fi

for i in `seq 1 ${numReqs}`;
do
	#echo $i
	echo "`./runAndTimeCurl.sh "msg_${i}" ${url} 2>&1 | sort | head -3 | tail -2 | tr "\n" "\t" `" >> $outfile &
done

echo "done"

