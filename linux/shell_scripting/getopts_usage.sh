





#!/bin/bash


usage()
{
        echo "######################################################################################"
        echo -e "########################### Test Job Usage ###########################"
        echo "######################################################################################"
        echo -e "\n Full Run : \n bash ./main.sh -r <run-type> \n E.g. bash ./main.sh -r fullRun \n\n Specific Run : \n bash ./main.sh -r <run-type> -i<analytic-ids> \n E.g. bash ./main.sh -r specificRun -i 81,82"
        echo "######################################################################################"
}


while getopts ":r:d:p:" opt; do
  case $opt in
    r) RUNTYPE="$OPTARG";;

    i) SPECIFIC_RUN_IDS="$OPTARG";;

    ?) echo "Invalid option -$OPTARG"
        usage
        exit 1 #as we wish to exit in case of wrong options
    ;;
  esac
done

if [ $OPTIND -eq 1 ]; then
        echo -e "No options were passed!!!"
        usage
        exit 1 #exit in case of no options passed
fi

echo "runtype : $RUNTYPE"
echo "specific-run-ids : $SPECIFIC_RUN_IDS"

#count non options passed
shift $((OPTIND-1))
echo "$# non-option arguments"

#end of script 
