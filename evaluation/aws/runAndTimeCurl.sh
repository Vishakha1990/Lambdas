#./util/start-cluster.py
#./util/setup.py --appdir pychat --appfile lambda_func.py

#url=`head -2 applications/pychat/static/config.json | tail -1 | awk -F '":' '{print $2}' | xargs`
#echo URL is:${url}

#curl -H "Content-Type: application/json" -X POST -d '{"name":"VIshakha"}' https://nehatesting.azurewebsites.net/api/HttpTriggerCSharp1?code=d1vcyncMHpLajNlaxOYiPJZVsTLTp3ruQ/gXiRgdilEB6SlgP4hbqQ==



msg="hello"

if [ -n "$1" ]
then
	msg=$1
else
	echo "Param 1 - No msg passed, using default ${msg}"
fi

if [ -n "$2" ]
then
	url=$2
else
	url=https://8e4m1dc1dd.execute-api.us-west-2.amazonaws.com/prod/hello
fi

time curl -H "Content-Type: application/json" -X POST -s -w "\n" ${url} -d '{"msg": "'"${msg}"'"}'
