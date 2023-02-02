attempt_counter=0
max_attempts=30

$IP_APP=192.168.56.11
PORT_APP=5000

until $(curl --output /dev/null --silent --head --fail http://"$IP_APP":"$PORT_APP"); do
    if [ ${attempt_counter} -eq ${max_attempts} ];then
      echo "Max attempts reached"
      exit 1
    fi

    printf '.'
    attempt_counter=$(($attempt_counter+1))
    sleep 60
done
