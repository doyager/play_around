#!/bin/sh
if [ "$#" -ne 4 ]; then
  echo "Usage: 4 input params expected" >&2
  exit 1
fi

AGENT_NAME=$1
RUN_DATE=$2
SERVER_NAME=$3
SLEEP_DURATION=$4

HOME="/home/mac/test_area/script_agent_test/scripts"
#set timestamp to be used for log
time_stamp=$(date +"%Y-%m-%d_%H%M%S%3N")
TODAY=$(date)

#creating log path
LOGS_PATH=${HOME}/logs


#Log Files
log_file_name=`echo script_agent_platform_${time_stamp}.log`
log_file="${LOGS_PATH}/${log_file_name}"

if [[ ! -e $LOGS_PATH ]]; then
    mkdir -p $LOGS_PATH
    echo "Log directory created !!" >> ${log_file} 2>&1
fi

echo "Hello World !!" >> ${log_file} 2>&1
echo -e "Input Args : \nAGENT_NAME : $AGENT_NAME \nRUN_DATE : $RUN_DATE \nSERVER_NAME : $SERVER_NAME \nSLEEP_DURATION : $SLEEP_DURATION !!" >> ${log_file} 2>&1
echo "Sleeping for $SLEEP_DURATION ..." >> ${log_file} 2>&1
echo "sleep_start: $(date)" >> ${log_file} 2>&1
sleep $SLEEP_DURATION
echo -e "sleep_end: $(date) \n\n" >> ${log_file} 2>&1
echo "Hello World !!" >> ${log_file} 2>&1
echo "After sleep !!" >> ${log_file} 2>&1
exit 0
