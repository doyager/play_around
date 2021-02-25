

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("jsonFlatten").getOrCreate()
from pyspark.sql.functions import *
df = spark.read.json("/Users/AF03812/Downloads/person-sample.json")
df.show()
df.printSchema()
from pyspark.sql import Row
df1 = df.select("person.personid","person.lastupdatedtimestamp","person.createdtimestamp",explode("person.relationships.relationship").alias("relations")).selectExpr("personid","lastupdatedtimestamp","createdtimestamp",'relations.type as relation_type','relations.id as relation_id','relations.createdtimestamp as relation_createdtimestamp','relations.lastupdatedtimestamp as relation_lastupdatedtimestamp').where(col('relation_type').like("%MEMBER_KEY%")).drop(col('relation_type')) # working
df1.show()
df1.write.mode('overwrite').option("sep","|").option("header","true").csv("/Users/AF03812/output1")


# working

df_subscriber = df.select("person.personid","person.lastupdatedtimestamp","person.createdtimestamp",explode("person.relationships.relationship").alias("relations")).where(col('relations.type').like("%MEMBER_KEY%")).drop(col('relation_type')).select("personid","lastupdatedtimestamp","createdtimestamp","relations",explode("relations.identifiers.identifier").alias("identifier")).where(col('identifier.type').like("%SUBSCRIBER%")).selectExpr("personid","lastupdatedtimestamp as lastupdatedtimestamp_sub","createdtimestamp as createdtimestamp_sub",'relations.type as relation_type','relations.id as relation_id_sub','relations.createdtimestamp as relation_createdtimestamp_sub','relations.lastupdatedtimestamp as relation_lastupdatedtimestamp_sub','identifier.id as sub_id','identifier.lastupdatedtimestamp as sub_lastTS','identifier.createdtimestamp as sub_createTS')

df_mbr_ehuid = df.select("person.personid","person.lastupdatedtimestamp","person.createdtimestamp",explode("person.relationships.relationship").alias("relations")).where(col('relations.type').like("%MEMBER_KEY%")).drop(col('relation_type')).select("personid","lastupdatedtimestamp","createdtimestamp","relations",explode("relations.identifiers.identifier").alias("identifier")).where(col('identifier.type').like("%MBR_EHUBID%")).selectExpr("personid","lastupdatedtimestamp","createdtimestamp",'relations.type as relation_type','relations.id as relation_id','relations.createdtimestamp as relation_createdtimestamp','relations.lastupdatedtimestamp as relation_lastupdatedtimestamp','identifier.id as mbr_ehuid_id','identifier.lastupdatedtimestamp as mbr_ehuid_lastTS','identifier.createdtimestamp as mbr_ehuid_createTS')

df_final = df_subscriber.join(df_mbr_ehuid,"personid").selectExpr("personid","lastupdatedtimestamp","createdtimestamp",'relation_id','relation_createdtimestamp','relation_lastupdatedtimestamp','sub_id','sub_lastTS','sub_createTS','mbr_ehuid_id','mbr_ehuid_lastTS','mbr_ehuid_createTS')
df_final.show()
#working
df1 = df.select("person.personid","person.lastupdatedtimestamp","person.createdtimestamp",explode("person.relationships.relationship").alias("relations")).where(col('relations.type').like("%MEMBER_KEY%")).drop(col('relation_type')).select("personid","lastupdatedtimestamp","createdtimestamp","relations",explode("relations.identifiers.identifier").alias("identifier")).where(col('identifier.type').rlike("^(SUBSCRIBER|MBR_EHUBID)(.*)+$"))

--------------------
import avro.schema
df_av = spark.read.avro("/Users/userMac/Downloads/1000person.avro")
df_av.show(1)

df_av = spark.read.format("com.databricks.spark.avro").load("/Users/userMac/Downloads/1000person.avro")
df_av.show(1)


%%python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("avroFlatten").getOrCreate()
from pyspark.sql.functions import *
df_av = spark.read.format("com.databricks.spark.avro").load("/Users/userMac/Downloads/1000person.avro")
df_av.show(1)




# Creates a DataFrame from a specified directory
df = spark.read.format("com.databricks.spark.avro").load("/tmp/episodes.avro")

#  Saves the subset of the Avro records read in
subset = df.where("doctor > 5")
subset.write.format("com.databricks.spark.avro").save("/tmp/output")


# Creates a DataFrame from a specified directory
df = spark.read.format("com.databricks.spark.avro").load("src/test/resources/episodes.avro")

#  Saves the subset of the Avro records read in
subset = df.where("doctor > 5")
subset.write.format("com.databricks.spark.avro").save("/tmp/output")

---------------------
df = spark.read.json("/Users/userMac/Downloads/person-sample.json")
df.show()
df.printSchema()

df.createOrReplaceTempView("person")

all_cols = spark.sql("select * from person")
all_cols.show()
all_cols.show(10,False)


mbr_cols = spark.sql("select * from person where ")
all_cols.show()
all_cols.show(10,False)

first_three = spark.sql("")



df = spark.read.json("/Users/userMac/Downloads/person-sample.json")
df.show()
df1 = df.select("person.personid")
df1 = df.select("person.personid","person.lastupdatedtimestamp","person.createdtimestamp","person.relationships.relationship.type") #MEMBER_KEY
df1.show()
import pyspark.sql.functions as psf
df.select('column').where("column like '%s%'").show()
df2 = df.select("person.personid","person.relationships.relationship.type").where("person.relationships.relationship.type like '%MEMBER_KEY%'") #MEMBER_KEY
df2.show()



#3rd approch


df = spark.read.json("/Users/userMac/Downloads/person-sample.json")
df.show()
df.printSchema()
import org.apache.spark.sql.functions.explode

val child = df.select(explode(data("parent.children"))).toDF("children")

child.select(explode(child("children.child_prop1"))).toDF("child_prop1").show()




################

pyspark.sql.functions.explode(col)[source]
Returns a new row for each element in the given array or map.

>>> from pyspark.sql import Row
>>> eDF = spark.createDataFrame([Row(a=1, intlist=[1,2,3], mapfield={"a": "b"})])
>>> eDF.select(explode(eDF.intlist).alias("anInt")).collect()
[Row(anInt=1), Row(anInt=2), Row(anInt=3)]
>>> eDF.select(explode(eDF.mapfield).alias("key", "value")).show()
+---+-----+
|key|value|
+---+-----+
|  a|    b|
+---+-----+

df = spark.read.json("/Users/userMac/Downloads/person-sample.json")
df.show()
from pyspark.sql import Row
#df1 = df.select("person.personid","person.lastupdatedtimestamp","person.createdtimestamp",explode("person.relationships").alias("relations")).select(explode("relations.relationship").alias("relation")) #MEMBER_KEY
df1 = df.select("person.personid","person.lastupdatedtimestamp","person.createdtimestamp",explode("person.relationships.relationship").alias("relations")).select('relations.*') #MEMBER_KEY- working
df1 = df.select("person.personid","person.lastupdatedtimestamp","person.createdtimestamp",explode("person.relationships.relationship").alias("relations")).select("personid","lastupdatedtimestamp","createdtimestamp",'relations.* ') #MEMBER_KEY- working
df1 = df.select("person.personid","person.lastupdatedtimestamp","person.createdtimestamp",explode("person.relationships.relationship").alias("relations")).select("personid","lastupdatedtimestamp","createdtimestamp",'relations.*').where(col('type').like("%MEMBER%")) # working
# not working - df1 = df.selectExpr("person.personid","person.lastupdatedtimestamp as person_lastupdatedtimestamp","person.createdtimestamp as person_createdtimestamp",explode("person.relationships.relationship").alias("relations")).select("personid","person_lastupdatedtimestamp","person_createdtimestamp",'relations.*').where(col('type').like("%MEMBER%"))#MEMBER_KEY- working
df1 = df.select("person.personid","person.lastupdatedtimestamp","person.createdtimestamp",explode("person.relationships.relationship").alias("relations")).selectExpr("personid","lastupdatedtimestamp","createdtimestamp",'relations.type as relation_type','relations.id as relation_id','relations.createdtimestamp as relation_createdtimestamp','relations.lastupdatedtimestamp as relation_lastupdatedtimestamp').where(col('relation_type').like("%MEMBER_KEY%")).drop(col('relation_type')) # working
df1.show()
from pyspark.sql import Row


#########################
pyspark.sql.functions.array_contains(col, value)[source]
Collection function: returns True if the array contains the given value. The collection elements and value must be of the same type.

Parameters:
col – name of column containing array
value – value to check for in array
>>> df = spark.createDataFrame([(["a", "b", "c"],), ([],)], ['data'])
>>> df.select(array_contains(df.data, "a")).collect()
[Row(array_contains(data, a)=True), Row(array_contains(data, a)=False)]


###############
  from pyspark.sql.types import *

from pyspark.sql.functions import *
df1 = df.select("person.personid","person.lastupdatedtimestamp","person.createdtimestamp",explode("person.relationships"),"person.relationships.relationship.type") #MEMBER_KEY

from pyspark.sql import SparkSession
>>> spark = SparkSession.builder.appName("jsonFlatten").getOrCreate()
 #.config("spark.some.config.option", "some-value") \
 .getOrCreate()


from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("jsonFlatten").getOrCreate()
df = spark.read.json("/Users/userMac/Downloads/person-sample.json")
from pyspark.sql.functions import *
#df1 = df.select("person.personid","person.lastupdatedtimestamp","person.createdtimestamp",explode("person.relationships"),"person.relationships.relationship.type") #MEMBER_KEY
df1 = df.select("person.personid","person.lastupdatedtimestamp","person.createdtimestamp","person.relationships.relationship.type") #MEMBER_KEY
df1.show()
json_schema = df.schema.json()
import json
new_schema = StructType.fromJson(json.loads(json_schema))


# new_df = sql_context.read.json(df.rdd.map(lambda r: r.json)) --try


sc = spark.sparkContext

path = "examples/src/main/resources/people.json"
peopleDF = spark.read.json(path)
peopleDF.printSchema()
