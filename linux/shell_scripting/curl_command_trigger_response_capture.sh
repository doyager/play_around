ui_host="machine.compnay.com"
CURL_BASE_BASE="https://$ui_host/analytics/v1/analytics/"
auth_token="aadkfadlkndfpmfldm.,dkfjdfjfl"
ACK_EMAIL_SUBJECT_PREFIX="TEAM Platform Job :"
HOME="."
PROPERTIES_FILE=${HOME}/"project_sit_platform.properties"
PROP_ANALYTIC_HINT_LIST="PROJECT_ANALYTICS_HINTS"
PROP_STATUSEMAIL_RECEPIENTS="PROJECT_STATUSEMAIL_RECEPIENTS"
PROP_UI_HOST="PROJECT_HOSTNAME"
PROP_UI_HOST_PORT="PROJECT_HOST_PORT"
PROP_UI_USER_NAME="PROJECT_USER_NAME"
PROP_UI_USER_PW="PROJECT_USER_PW"

#block comments
: <<'END'
#property file name : project_sit_platform.properties
#property file format:
PROJECT_ANALYTIC_IDS=107,105,102,103,104,481
PROJECT_ANALYTICS_HINTS=cc_duplicate,cc_notcovered
PROJECT_STATUSEMAIL_RECEPIENTS=mac@company.com
PROJECT_HOSTNAME=dnshostname.compnay.com
#PROJECT_HOST_PORT=19443
PROJECT_USER_NAME=SERVICEIDDEFV
PROJECT_USER_PW=dev123#

END
#end of block comments


#set timestamp to be used for log
time_stamp=$(date +"%Y-%m-%d_%H%M%S%3N")
TODAY=$(date)

#creating log path
LOGS_PATH=${HOME}/logs

#Log Files
log_file_name=`echo project_logfile_${time_stamp}.log`
log_file="${LOGS_PATH}/${log_file_name}"

if [[ ! -e $LOGS_PATH ]]; then
    mkdir -p $LOGS_PATH
    echo "Log directory created !!" >> ${log_file} 2>&1
fi



executeAckPush(){

echo -e "\nInside  executeAckPush method" >> ${log_file} 2>&1
read -r -d '' email_body << EOM
#####################################################################################
\n###################### Platform Job Trigger Report ########################
\n#####################################################################################
\n\nTotal no of jobs : $2 \nTotal no of success jobs : $3 \nTotal no of failure jobs : $4

\n\nLog path : ${log_file}
\n$5
\n\n#####################################################################################
EOM
echo -e "INFO Email body : [" >> ${log_file} 2>&1
echo -e $email_body >> ${log_file} 2>&1
echo -e "]" >> ${log_file} 2>&1
echo -e $email_body | mailx -s "$ACK_EMAIL_SUBJECT_PREFIX::: $TODAY :: $RUN_TYPE" $1
}


analytic_id_list=$(read_properties $PROP_ANALYTIC_ID_LIST)
analytic_hint_list=$(read_properties $PROP_ANALYTIC_HINT_LIST)
recepient_list=$(read_properties $PROP_STATUSEMAIL_RECEPIENTS)
ui_host=$(read_properties $PROP_UI_HOST)
ui_host_port=$(read_properties $PROP_UI_HOST_PORT)

  ids_list=$1
	count=0
	success_count=0
	failure_count=0
	for analytic_id in $(echo $ids_list | sed "s/,/ /g")
	do
		#curlUrl=${CURL_URL_BASE}$analytic_id
		echo "************************Execution No : $count **************************" >> ${log_file} 2>&1
		echo "analytic_id : ${analytic_id}" >> ${log_file} 2>&1
		echo "curl_url : ${CURL_URL_BASE}" >> ${log_file} 2>&1

		echo "Fetching Auth bearer" >> ${log_file} 2>&1
	    auth_token=$( get_auth_bearer $CURL_AUTH_BEARER_BASE $USER_NAME $PASS_WORD)

	    echo -e "\n auth_token : $auth_token \n" >> ${log_file} 2>&1
	    echo "auth_token : $auth_token"

responseStatus=$(curl -s -o /dev/null -w "%{http_code}" -k -X POST "${CURL_URL_BASE}" -H "Authorization: Bearer $auth_token" -H "accept: application/json"  -H "Content-Type: application/json" -d "{ \"hints\": [ \"$analytic_id\" ] }") >> ${log_file} 3>&1
		echo -e "\n Analytic : $analytic_id , responseStatus : $responseStatus \n" >> ${log_file} 2>&1
		echo -e "\n Analytic : $analytic_id , responseStatus : $responseStatus \n"
		if [ $responseStatus -ne 200 ]; then
        		echo -e "ERROR: CURL COMMAND FAILURE :  \n analytic_id :$analytic_id \n curl_url_base :$CURL_URL_BASE \n return_status: $curlStatus" >> ${log_file} 2>&1
        		echo "ERROR: CURL COMMAND FAILURE : $curlStatus"
        		failure_count=$((failure_count+1))
        else
		echo "Analytic : $analytic_id triggered succesfully !!!" >> ${log_file} 2>&1
		echo "Analytic : $analytic_id triggered succesfully !!!"
		success_count=$((success_count+1))
		fi
    
    success_count=$((success_count+1))
		fi
		count=$((count+1))
		echo "Sleeping for $SLEEP_INTERVAL ..." >> ${log_file} 2>&1
		echo "sleep_start: $(date)" >> ${log_file} 2>&1
		sleep $SLEEP_INTERVAL #sleep between each execution
		echo -e "sleep_end: $(date) \n\n" >> ${log_file} 2>&1
		echo -e "*******************************************************************\n" >> ${log_file} 2>&1
	done

	#calling Ack push method , Arg-5 placeholder for custom message
	executeAckPush $recepient_list $count $success_count $failure_count ""

	echo "############################################################################################################" >> ${log_file} 2>&1
	echo "INFO:  Platform Job - $RUNTYPE  Completed" >> ${log_file} 2>&1
	echo "############################################################################################################" >> ${log_file} 2>&1
}
