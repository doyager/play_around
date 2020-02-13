#!/usr/bin/env python

from pyspark.sql import SparkSession

from pyspark.sql import HiveContext


from sys import argv

from pyspark.sql.functions import lit

import os.path

import uuid



########################################################################################################################

# # Authors      : 

# # Date Created : 8/19/18

# # Project      : Team1

# # Version      : 1.0

# # Description  : This program perform the count and assign to varialbe and compare 

########################################################################################################################



# Initializing spark session & Hive Context

spark = SparkSession.builder.appName("Compare variable").enableHiveSupport().getOrCreate()

hvContext = HiveContext(spark)

#given count query will return one row with one column
df_counts = spark.sql("select count(emp_no) from employee").collect().[0][0]

print(df_counts)
