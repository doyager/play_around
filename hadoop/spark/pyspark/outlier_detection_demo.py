#!/usr/bin/env python
#from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import HiveContext
from sys import argv
from pyspark.sql.functions import *
from pyspark.sql import Row
import os.path

"""
process :
- finds the most frequent metric_qty value per each "ndc " group and assigng rank to it and filtering rank < 2 to retrive only the most frequent values and creating  temp table df_mode_Score to use it futher 
- using the above created temp table and joining with main data set to find out outlier records based on metric qty 

"""

def getOutliers() :

        try:
                # Initializing spark context & Hive Context
                print (">>>>Spark: Initializing SparkContext ..")
                spark = SparkSession.builder.appName("outlier_analysis").enableHiveSupport().getOrCreate()
                hvContext = HiveContext(spark)
                #df_mode_score = spark.sql("select * from  dv_pbminrxph_gbd_r000_sg.clm_cvs_vap_prcsr_hdr_test")
                #df_mode_score.show()
                df_mode_score = spark.sql("with q1 as (select ndc, metric_dec_qty, count(*) as cnt from db.tb1 group by ndc, metric_dec_qty) ,q2 as (select * , rank() over (partition by ndc  order by cnt desc)as rank from q1) select * from q2 where rank < 2")
                df_mode_score.show()
                #exit(1)
                df_mode_score.registerTempTable("df_mode_score")
                hvContext.cacheTable('df_mode_score')
                threshold="1.5"  #50% for test
                df_outliers = spark.sql(" select a.ndc, a.metric_dec_qty, a.col1, b.metric_dec_qty as most_freq_qty from db.tb1 a join df_mode_score b ON (a.ndc = b.ndc) where a.metric_dec_qty > "+ threshold +" * b.metric_dec_qty ")
                df_outliers.show()
                df_outliers.registerTempTable("df_outliers")
                hvContext.cacheTable('df_outliers')
                #insert_query= "INSERT OVERWRITE TABLE " + output_db+"."+output_table+" select col1, coln from df_outliers"
                #spark.sql(insert_query)
                hvContext.uncacheTable('df_mode_score')
                hvContext.uncacheTable('df_outliers')
                spark.stop()
                print (">>>>Spark: Insert into outliers table completed !!!")
                print (">>>>Spark: End of program")
        except Exception as e:
                            print "[ERROR] getOutliers failed "
                            print e
                            exit(1)


if __name__ == "__main__":
    print (">>>>Spark: Initializing the program..")
    print (">>>>Spark: Loading the arguments")
    getOutliers()
    exit(0)
    if len(argv) == 5:
      input_db = argv[1]
      input_table = argv[2]
      output_db = argv[3]
      output_table = argv[4]
      getOutliers()
    else:
      print (">>>>Spark: Argument length error")
