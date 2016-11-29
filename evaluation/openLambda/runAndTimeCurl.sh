#./util/start-cluster.py
#./util/setup.py --appdir pychat --appfile lambda_func.py


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
	url=`head -2 ~/gitRepository/Lambdas/applications/pychat/static/config.json | tail -1 | awk -F '":' '{print $2}' | xargs`
	echo "Param 2 - url not passed, using ${url}"
fi

time curl -s -w "\n" ${url} -d '{"op": "msg", "msg": "'"${msg}"'"}'
