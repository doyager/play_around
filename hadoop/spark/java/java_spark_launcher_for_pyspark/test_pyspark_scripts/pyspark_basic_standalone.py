#!/usr/bin/env python
from pyspark import SparkConf, SQLContext
from pyspark.sql import SparkSession

"""
 spark submit command :   spark2-submit ./pyspark_basic_standalone.py
"""

# Initializing spark session & Hive Context
print (">>>>Spark: Initializing SparkSession ..")
spark = SparkSession.builder.appName("basic_standalone_app").getOrCreate()
df = spark.createDataFrame([("danny",1),("jon",2),("sam",3)], ['name','id'])
df.show()



"""
output :
+-----+---+
| name| id|
+-----+---+
|danny|  1|
|  jon|  2|
|  sam|  3|
+-----+---+
"""
