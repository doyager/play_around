from pyspark.sql import SparkSession
from pyspark.sql  import HiveContext
import uuid
from pyspark.sql.functions import udf


def insert_into_bi():
spark = SparkSession.builder.appNam("sample_uuid_add")
.config("spark.hadoop.avro.mapred.ignore.inputs.without.extension","false")
.enableHiveSupport().getOrCreate()


df = spark.sql("select * from inbound_db.bi_raw_tbl")

df_input = spark.sql("select * from " + input_db +"."+input_tbl)

#udf definition
uuidUDF = udf( lambda : str(uuid.uuid4()), StringType())

df.withColumn("uuid_key",uuidUDF())
df.registerTempleTable("df_final")
hvContext.cacheTable("df_final")

insert_query = "INSERT OVERWRITE TABLE  warehouse_db.bi_table select * from df_final"
spark.sql(insert_query)
hvContext.uncacheTable("df_final")
spark.stop()
exit(0)


if __name__ == "__main__":

   if len(argv) == 3:
          input_db = argv[1]
          input_tbl = argv[2]
