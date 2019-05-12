#!/bin/bash
###################################################################################################################################
# # Author       : mac
# # Date Created : 05/08/19
# # Project      : proj
# # Version      : 1.0
# # Description  : this calls some libraries using curl command and send acknowledge in case of success/failure
#
###################################################################################################################################

HOME="."
PROPERTIES_FILE=${HOME}/"project_proj2_platform.properties"
PROP_ANALYTIC_ID_LIST="project_proj2_ANALYTIC_IDS"
PROP_STATUSEMAIL_RECEPIENTS="project_proj2_STATUSEMAIL_RECEPIENTS"
PROP_AI_HOST="project_proj2_HOSTNAME"
PROP_AI_HOST_PORT="project_proj2_HOST_PORT"
CURL_URL_BASE="http://$proj2_host:$proj2_host_port/AnalyticLibrary/v1/analytics/"
ACK_EMAIL_SUBJECT_PREFIX="project proj2 Platform Job :"
FULL_RUN_VAL=Full-Run
SPECIFIC_RUN_VAL=Specific-Run

#set timestamp to be used for log
time_stamp=$(date +"%Y-%m-%d_%H%M%S%3N")
TODAY=$(date)

#creating log path
LOGS_PATH=${HOME}/logs

#Log Files
log_file_name=`echo project_proj2_platform_${time_stamp}.log`
log_file="${LOGS_PATH}/${log_file_name}"

if [[ ! -e $LOGS_PATH ]]; then
    mkdir -p $LOGS_PATH
    echo "Log directory created !!" >> ${log_file} 2>&1
fi


usage()
{
        echo -e "\n######################################################################################"
        echo -e "########################### proj1 - proj2 Platform Job Usage ###########################"
        echo -e "######################################################################################"
        echo -e "\n Full Run : \n bash ./main.sh -r <run-type> \n E.g. bash ./main.sh -r Full-Run \n\n Special Run : \n bash ./main.sh -r <run-type> -i<ids> \n E.g. bash ./main.sh -r Special-Run -i 4001,4002"
        echo -e "###################################################################################### \n"
}


while getopts ":r:i:" opt; do
  case $opt in
    r) RUN_TYPE="$OPTARG";;

    i) SPECIFIC_RUN_IDS="$OPTARG";;

    ?) echo "Invalid option -$OPTARG" >> ${log_file} 2>&1
        usage >> ${log_file} 2>&1
        exit 1
    ;;
  esac
done

if [ $OPTIND -eq 1 ]; then
        echo "No options were passed!!!" >> ${log_file} 2>&1
        usage >> ${log_file} 2>&1
        exit 1
fi



executeAckPush(){

echo -e "\nInside  executeAckPush method" >> ${log_file} 2>&1
read -r -d '' email_body << EOM
#####################################################################################
\n########################### proj1 -  proj2 Platform Job Report ##########################
\n#####################################################################################
\n\nTotal no of jobs : $2 \nTotal no of success jobs : $3 \nTotal no of failure jobs : $4

\n\nLog path : ${log_file}
\n$5
\n\n#####################################################################################
EOM
echo -e "INFO Email body :" >> ${log_file} 2>&1
echo -e $email_body >> ${log_file} 2>&1
echo -e $email_body | mailx -s "$ACK_EMAIL_SUBJECT_PREFIX::: $TODAY :: $RUN_TYPE" $1
}

read_properties(){
	if [ -f $PROPERTIES_FILE ]
	then
		#reading prop using pro name
		val=$(grep "${1}" ${PROPERTIES_FILE}|cut -d'=' -f2)
		echo $val
	else
		echo "$PROPERTIES_FILE not found!!" >> ${log_file} 2>&1
		exit 1
	fi
}

#reading properties
analytic_id_list=$(read_properties $PROP_ANALYTIC_ID_LIST)
recepient_list=$(read_properties $PROP_STATUSEMAIL_RECEPIENTS)
proj2_host=$(read_properties $PROP_AI_HOST)
proj2_host_port=$(read_properties $PROP_AI_HOST_PORT)
CURL_URL_BASE="http://$ai_host:$ai_host_port/AnalyticLibrary/v1/analytics/"

process(){
	echo "############################################################################################################" >> ${log_file} 2>&1
	echo "INFO: proj1 proj2 Platform Job is Started at - $TODAY : $RUN_TYPE" >> ${log_file} 2>&1
	echo "############################################################################################################" >> ${log_file} 2>&1

	ids_list=$1
	count=0
	success_count=0
	failure_count=0
	for analytic_id in $(echo $ids_list | sed "s/,/ /g")
	do
		curlUrl=${CURL_URL_BASE}$analytic_id
		echo ${curlUrl} >> ${log_file} 2>&1
		#curl -X -s -v "${curlUrl}" -H "accept:application/json"
		curlStatus=$?
		if [[ curlStatus -ne 0 ]]; then
        		echo -e "ERROR: CURL COMMAND FAILURE :  \n Command :$curlUrl \n ReturnStatus: $curlStatus"   >> ${log_file} 2>&1
        		echo "ERROR: CURL COMMAND FAILURE : $curlStatus"
        		failure_count=$((failure_count+1))
		fi
		success_count=$((success_count+1))
		count=$((count+1))
	done

	#calling Ack push method , Arg-5 placeholder for custom message
	executeAckPush $recepient_list $count $success_count $failure_count ""

	echo "############################################################################################################" >> ${log_file} 2>&1
	echo "INFO: proj1 proj2 Platform Job - $RUNTYPE  Completed" >> ${log_file} 2>&1
	echo "############################################################################################################" >> ${log_file} 2>&1
}

specific_run(){
	process $SPECIFIC_RUN_IDS
}
full_run(){
	process $analytic_id_list
}

main(){

	if [ "$RUN_TYPE" == "$FULL_RUN_VAL" ]
        then
                full_run
        elif [ "$RUN_TYPE" == "$SPECIFIC_RUN_VAL" ]
	then
        	specific_run
	else
		echo "ERROR : Wrong args value passed !! --> $RUN_TYPE " >> ${log_file} 2>&1
		executeAckPush $recepient_list "failed-job" "xxx" "xxx" "ERROR : Wrong args value passed !! --> $RUN_TYPE"
	fi
}

#calling main method
main
