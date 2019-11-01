#!/bin/sh
###################################################################################################################################
# # Author       : Mac
# # Date Created : 10/30/19
# # Project      : Project
# # Version      : 1.0
# # Description  : This script reboots the Platform Java agent process for project
###################################################################################################################################

HOME="."
AGENT_NAME=project-proces
AGENT_PORT='Dserver.port=35000'
AGENT_START_SCRIPT=/home/mac/project/dev/start_agent.sh

#set timestamp to be used for log
time_stamp=$(date +"%Y-%m-%d_%H%M%S%3N")
TODAY=$(date)

#creating log path
LOGS_PATH=${HOME}/logs

#Log Files
log_file_name=`echo project_platform_agent_reboot_${time_stamp}.log`
log_file="${LOGS_PATH}/${log_file_name}"

if [[ ! -e $LOGS_PATH ]]; then
    mkdir -p $LOGS_PATH
    echo "Log directory created !!" >> ${log_file} 2>&1
fi


get_processid()
{
        pid=$(ps aux | grep java | grep $AGENT_NAME | grep $AGENT_PORT | cut -d " " -f2)
        echo $pid
}

kill_process()
{
        pid=$1
        `kill -9 $pid`
        echo $?
}

start_agent()
{
        `sh $AGENT_START_SCRIPT`
        echo $?
}

process()
{

        echo "############################################################################################################" >> ${log_file} 2>&1
        echo "INFO: Project Platform Agent Reboot Process Started @ $TODAY " >> ${log_file} 2>&1
        echo "############################################################################################################" >> ${log_file} 2>&1

        p_id=$(get_processid)

        if [ ! -z $p_id ]; then
                echo -e "$AGENT_NAME : Current Process ID = $p_id"  >> ${log_file} 2>&1
                ret_val=$(kill_process $p_id)
                echo "$AGENT_NAME : KILL_PROCESS() return code = $ret_val"  >> ${log_file} 2>&1
                if [ "$ret_val" -ne "0" ]; then
                        echo "$AGENT_NAME : KILL_PROCESS() Process command failure!!"  >> ${log_file} 2>&1
                        exit $ret_val
                fi
                echo -e "$AGENT_NAME : KILL_PROCESS() Process command successful!!"  >> ${log_file} 2>&1
                str_ret_val=$(start_agent)
                echo "$AGENT_NAME : START_AGENT() Process return code = $str_ret_val"  >> ${log_file} 2>&1
                if [ $str_ret_val -ne 0 ]; then
                        echo "$AGENT_NAME : START_AGENT() Process command failure!!"  >> ${log_file} 2>&1
                        exit $str_ret_val
                fi
                echo -e "$AGENT_NAME : START_AGENT() Process command successful!!"  >> ${log_file} 2>&1
                new_pid=$(get_processid)
                echo -e "$AGENT_NAME : New Process ID = $new_pid"  >> ${log_file} 2>&1
        else
                echo -e "$AGENT_NAME : NO Current Process for $AGENT_NAME"  >> ${log_file} 2>&1
                str_ret_val=$(start_agent)
                echo "$AGENT_NAME : START_AGENT() return code = $str_ret_val"  >> ${log_file} 2>&1
                if [ $str_ret_val -ne 0 ]; then
                        echo "$AGENT_NAME : START_AGENT() Process command failure!!"  >> ${log_file} 2>&1
                        exit $str_ret_val
                fi
                echo -e "$AGENT_NAME : START_AGENT() Process command successful!!"  >> ${log_file} 2>&1
                new_pid=$(get_processid)
                echo -e "$AGENT_NAME : New Process ID = $new_pid"  >> ${log_file} 2>&1
        fi
        echo "############################################################################################################" >> ${log_file} 2>&1
        echo "INFO: Project Platform Agent Reboot Process Completed !!" >> ${log_file} 2>&1
        echo "############################################################################################################" >> ${log_file} 2>&1
}


#start process
process
