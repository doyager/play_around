#create data frame :


#method 1:


        val someData = Seq(
          Row(8, "bat"),
          Row(64, "mouse"),
          Row(-27, "horse")
        )

        val someSchema = List(
          StructField("number", IntegerType, true),
          StructField("word", StringType, true)
        )

        val someDF = spark.createDataFrame(
          spark.sparkContext.parallelize(someData),
          StructType(someSchema)
        )

#method 2:


        //The toDF() method can be called on a sequence object to create a DataFrame.
      import spark.implicits._
      

      val someDF = Seq(
        (8, "bat"),
        (64, "mouse"),
        (-27, "horse")
      ).toDF("number", "word")


#method 3:

      createDF() is defined in spark-daria and allows for the following terse syntax.

      val someDF = spark.createDF(
        List(
          (8, "bat"),
          (64, "mouse"),
          (-27, "horse")
        ), List(
          ("number", IntegerType, true),
          ("word", StringType, true)
        )
      )



#udf - spark sql

val squared = (s: Long) => {
  s * s
}
spark.udf.register("square", squared)
spark.range(1, 20).registerTempTable("test")
%sql select id, square(id) as id_squared from test

#udf - data frame

import org.apache.spark.sql.functions.{col, udf}
val squared = udf((s: Long) => s * s)
display(spark.range(1, 20).select(squared(col("id")) as "id_squared"))
