

url=https://parallelsort.azurewebsites.net/api/Sort?code=RHx7FBFDYF2NlZFebAtKDlBXtwOt9aSLkYstlzK6Up3lcune9HtZ4g==

echo URL is:${url}


outfile="sort_out.txt"
rm -f ${outfile}

echo "Result\tTimeType\tTime" >> ${outfile}

#for i in 1000000000 10000000000
for i in 100000000
do
        #echo "`./runAndTimeSort.sh "${i}" ${url} 2>&1 | sort | head -3 | tail -2 | tr "\n" "\t" `" >> $outfile &
	echo "`./runAndTimeSort.sh "${i}" ${url} 2>&1 `" >> $outfile &
done

echo "done"

