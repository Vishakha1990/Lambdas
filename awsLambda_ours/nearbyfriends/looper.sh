
for numDivs in 30 40 50 60 70 80 90 100
do
	for trial in 1 2
	do
		echo -e "$numDivs\t$trial"
		python findnearbypeopleApp.py $numDivs > ${numDivs}_${trial}.txt
	done
done
