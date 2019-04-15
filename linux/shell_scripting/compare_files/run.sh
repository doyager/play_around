#!/usr/local/bin/bash

#control run script for the process

project_dir="."
main_script=$project_dir"/main.sh"
temp_dir=$project_dir"/tmp_data"
log_dir=$project_dir"/logs"
log_file=$log_dir"/run_op.txt"

#clean up
rm -rf $tmp_dir
rm $log_file

#file 1 run
$main_script ./sysctl_host1.txt hstmc1 ./sysctl_host2.txt hstmc2

#file 2 run
$main_script ./ora.init_hst1 hstmc1 ./ora.init_hst2 hstmc2

#file 3 run
$main_script ./sys_par_hst1.txt hstmc1 ./sys_par_hst2.txt hstmc2
