
#url=https://nehatesting.azurewebsites.net/api/HttpTriggerCSharp1?code=d1vcyncMHpLajNlaxOYiPJZVsTLTp3ruQ/gXiRgdilEB6SlgP4hbqQ==


#./util/start-cluster.py
#./util/setup.py --appdir pychat --appfile lambda_func.py

url=`head -2 applications/pychat/static/config.json | tail -1 | awk -F '":' '{print $2}' | xargs`
#xargs trims space and quotes

echo URL is:${url}


outfile="output_loop.txt"
rm -f ${outfile}

echo "Result\t\tTimeType\tTime" >> ${outfile}

for i in {1..1000};
do
	echo "`./runAndTimeCurl.sh "msg_${i}" ${url} 2>&1 | sort | head -3 | tail -2 | tr "\n" "\t" `" >> $outfile &
done

echo "done"

