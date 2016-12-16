
for burst in 20 30 40 60 70 80 90
do
	echo "$burst"
	./loop_nearbyfriends.sh ${burst}
	sleep 30
done
