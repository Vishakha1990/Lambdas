
output_dir=./min_results

#opfile=${output_dir}/op_local.txt 
#rm -f ${opfile}

#echo "opfile" $opfile
#echo -e "Num\tInputGeneration\tProcessing" > opfile
#for i in 100 1000 10000 100000 1000000 10000000 100000000
#do
#    echo local size $i
#    time python minApp.py local $i >> ${opfile}
#done


#for numDivs in 5 10 20 40 100
#do
#    opfile=${output_dir}/op_${numDivs}_lambda.txt
#    rm -f opfile
#    echo -e "NumDivs\tNum\tInputGeneration\tLambda\tMerge" > ${opfile}
#done


#for i in 100 1000 10000 100000 1000000 10000000 100000000
#do
#    for numDivs in 1 5 10 20 40 100
#    do
#        opfile=${output_dir}/op_${numDivs}_lambda.txt
#        echo lambda numDivs $numDivs size $i
#        time python minApp.py lam $i $numDivs >> ${opfile}
#    done
#done

for i in 10000000 100000000
do
    for numDivs in 1000
    do
        opfile=${output_dir}/op_${numDivs}_lambda.txt
        echo lambda numDivs $numDivs size $i
        time python minApp.py lam $i $numDivs >> ${opfile}
    done
done

