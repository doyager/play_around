#!/usr/bin/env python
# encoding=utf8
from pyspark import SparkConf, SQLContext
from pyspark.sql import SparkSession
from pyspark.sql import HiveContext
from pyspark.sql import Row
from pyspark.sql.functions import *


"""
 spark submit command :   spark2-submit ./pyspark_basic_standalone.py
spark2-submit --conf "spark.dynamicAllocation.enabled=true" --deploy-mode client --supervise --executor-cores 3 --executor-memory 10G --driver-memory 5G --queue root.dev_yarn ./pyspark_read_hive_table.py
"""

input_db = "test_db_name"
input_table = "test_tbl"
# Initializing spark session & Hive Context
print (">>>>Spark: Initializing SparkContext ..")
spark = SparkSession.builder.appName("basic_read_hive_table_app").enableHiveSupport().getOrCreate()
hvContext = HiveContext(spark)
df = spark.sql("select * from  "+input_db+"."+input_table)
df.show()
spark.stop()
