#./util/start-cluster.py
#./util/setup.py --appdir pychat --appfile lambda_func.py

url=`head -2 applications/pychat/static/config.json | tail -1 | awk -F '":' '{print $2}' | xargs`
#echo URL is:${url}

msg="hello"

if [ -n "$1" ]
then
	msg=$1
fi

if [ -n "$2" ]
then
	url=$2
else
	url=`head -2 applications/pychat/static/config.json | tail -1 | awk -F '":' '{print $2}' | xargs`
fi

time curl -s -w "\n" ${url} -d '{"op": "msg", "msg": "'"${msg}"'"}'
