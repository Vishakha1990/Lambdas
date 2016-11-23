


url=https://nehatesting.azurewebsites.net/api/HttpTriggerCSharp1?code=d1vcyncMHpLajNlaxOYiPJZVsTLTp3ruQ/gXiRgdilEB6SlgP4hbqQ==

echo URL is:${url}


outfile="output.txt"
rm -f ${outfile}

echo "Result\tTimeType\tTime" >> ${outfile}

for i in {1..1000};
do
        echo "`./runAndTimeCurl.sh "msg_${i}" ${url} 2>&1 | sort | head -3 | tail -2 | tr "\n" "\t" `" >> $outfile &
done

echo "done"

