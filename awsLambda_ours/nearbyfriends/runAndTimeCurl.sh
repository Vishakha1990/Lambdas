#./util/start-cluster.py
#./util/setup.py --appdir pychat --appfile lambda_func.py

#url=`head -2 applications/pychat/static/config.json | tail -1 | awk -F '":' '{print $2}' | xargs`
#echo URL is:${url}

#curl -H "Content-Type: application/json" -X POST -d '{"name":"VIshakha"}' https://nehatesting.azurewebsites.net/api/HttpTriggerCSharp1?code=d1vcyncMHpLajNlaxOYiPJZVsTLTp3ruQ/gXiRgdilEB6SlgP4hbqQ==



usr="user:0"
mylat="40.335"
mylong="2.335"

if [ -n "$3" ]
then
	usr=$1
	mylat=$2
	mylong=$3
	
#else
	#echo "Param 1 - No msg passed, using default ${usr} ${mylat} ${mylong}"
fi

if [ -n "$4" ]
then
	url=$4
else
	url=https://jkf02xx1kl.execute-api.us-east-2.amazonaws.com/prod/api/findnearbyfriends
fi

time curl -H "Content-Type: application/json" -X POST -s -w "\n" ${url} -d '{"userid": "'"${usr}"'","latitude": "'"${mylat}"'","longitude": "'"${mylong}"'"}'
