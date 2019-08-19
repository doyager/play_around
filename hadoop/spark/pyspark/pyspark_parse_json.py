#!/usr/bin/env python

from pyspark.sql import SparkSession

from pyspark.sql import HiveContext

from sys import argv

from pyspark.sql.functions import lit

import os.path

import uuid



########################################################################################################################

# # Authors      : Mac

# # Date Created : 11/20/18

# # Project      : Home

# # Version      : 1.0

# # Description  : This program flattens the input json file to extract required fields

########################################################################################################################


if __name__ == "__main__":

    print ">>>>Spark: Initializing the program.."

    print ">>>>Spark: Loading the arguments"
    # Initializing the arguments
    if len(argv) == 7:
        old_llks = argv[1]
        new_llks = argv[2]
        agadia_rawz_database = argv[3]
        agadia_rawz_table = argv[4]
        agadia_appz_database = argv[5]
        agadia_appz_table = argv[6]
        print ">>>>Spark: received arguments /"
        print ">>>>" + old_llks + " " + new_llks + " " + rawz_database + " " + agadia_rawz_table + " " + \
              agadia_appz_database + " " + appz_table
    else:
        print ">>>>Spark: Usage: <Old llks> <New llks> <Agadia Rawz database> <Agadia Rawz table> <Agadia Appz database>" \
              " <Agadia Appz table>"
        for i in argv:
            print i
            print "\n"
        exit(1)
        
# Initializing spark session & Hive Context

spark = SparkSession.builder.appName("IPS_FLATTEN_JSON").enableHiveSupport().getOrCreate()

#Run the Select query


print ">>>>Spark: Reading input json file"
df = spark.read.json("/Users/mac/Downloads/person-sample.json")
df.show()
df.printSchema()
print ">>>>Spark: Running select query statement"
df1 = df.select("person.personid","person.lastupdatedtimestamp","person.createdtimestamp",explode("person.relationships.relationship").alias("relations")).selectExpr("personid","lastupdatedtimestamp","createdtimestamp",'relations.type as relation_type','relations.id as relation_id','relations.createdtimestamp as relation_createdtimestamp','relations.lastupdatedtimestamp as relation_lastupdatedtimestamp').where(col('relation_type').like("%MEMBER_KEY%")).drop(col('relation_type')) # working
df1.show()
print ">>>>Spark: Writing output pipe-delimited file"
df1.write.mode('overwrite').option("sep","|").option("header","true").csv("/Users/mac/output1")
    #output = run_query(insert_query)

print ">>>>Spark: select query completed"


print">>>>Spark: End of program"

spark.stop()

exit(0)
