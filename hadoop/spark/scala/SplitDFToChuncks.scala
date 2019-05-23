package com.test;

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.{ lit, col, current_timestamp,row_number }
import org.apache.spark.sql.expressions.Window
import org.apache.spark.sql.DataFrame

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


object SplitDFToChuncks {


/*
command for run:
spark2-submit --packages com.databricks:spark-avro_2.11:4.0.0  --conf "spark.ui.port=53902"  --conf "spark.dynamicAllocation.enabled=true"
--deploy-mode client --supervise --queue dev_yarn --master yarn --executor-cores 4 --num-executors 10 --executor-memory 10G --driver-memory 5G
--class com.test.SplitDFToChuncks Test-Project-SNAPSHOT.jar

*/

 val logger = LoggerFactory.getLogger(SplitDFToChuncks.getClass)

def main(args: Array[String]) {

if (args.length != 2 ) {
      System.err.println(" Args Error : Incorrect no of args passed !!!  Required 2 args and " + args.length + " are passed !")
      System.err.println("Usages :\n\n <db_name> <table_name>)
       throw new RuntimeException(" Args Error : Incorrect no of args passed !!!  Required 2 args")
      }
      else{
val spark1 = SparkSession
.builder()
.appName("Df split test ")
.config("spark.sql.warehouse.dir", "spark-warehouse")
.enableHiveSupport()
.getOrCreate()

val table_name = "test_tbl" //args(1)
val db_name = "temp_db" //args(0)
//val spark1 = SparkSessionUtil.sparkSession

val df = spark1.sql("select *  from  " + db_name + "." + table_name+" limit 6000")
//creating a column wit constant value as we want rank to be incrementing on single group
val newDF = df.withColumn("grouped", lit("grouped"))
//we can order by any column
val windowSpec = Window.partitionBy("grouped").orderBy(col("date_created").desc)
// apply window specification for row_number generation
var latestDF = newDF.withColumn("row", row_number() over windowSpec)   

val k=1000  // chunck size
val totalCount = latestDF.count()  // our DF total count
var lowLimit = 0
var highLimit = lowLimit + k

while (lowLimit < totalCount) {
val inter_df = latestDF.where(s"row <= ${highLimit} and row > ${lowLimit}") //.show(false)
inter_df.show()
println("Inside while")
// TODO : post to kafka
lowLimit = lowLimit + k
highLimit = highLimit + k
println("lowLimit : "+lowLimit)
println("lowLimit : "+highLimit)

}

}
}

}
