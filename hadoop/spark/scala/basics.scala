#shell start command :

spark2-shell --queue dv_que1 --executor-cores 4 --num-executors 10 --executor-memory 10G --driver-memory 5G --conf spark.dynamicAllocation.enabled=true --conf spark.dynamicAllocation.maxExecutors=10

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


#method 4:



                val values = List(List("1", "One","A") ,List("2", "Two","B") ,List("3", "Three","C"),List("4","Four","D")).map(x =>(x(0), x(1),x(2)))
                val newNames = Seq("x1", "x2", "x3")
                import spark.implicits._
                val df = values.toDF(newNames: _*)



#udf - spark sql

val squared = (s: Long) => {
  s * s
}
spark.udf.register("square", squared)
spark.range(1, 20).registerTempTable("test")
%sql select id, square(id) as id_squared from test


# spark df add difference columns , to matct the master column list 
# master col : x1 to x5 , and if df has x1 & x2 , now x3 ,x4,x5 should be added 




                #data
                val values = List(List("1", "One","A") ,List("2", "Two","B") ,List("3", "Three","C"),List("4","Four","D")).map(x =>(x(0), x(1),x(2)))
                val col_names = Seq("x1", "x4", "x5")
                import spark.implicits._

                #create df
                var df = values.toDF(col_names: _*)
                df.show

                #get col list
                val colNames = df.columns
                val selectColumns = df.columns.toSeq

                val master_cols = Seq("x1", "x2", "x3","x4","x5")
                #diff columns 

                #calculate diff cols
                val dif_cols = master_cols.filterNot(selectColumns.toSet)
                #dif_cols1: Seq[String] = List(x4, x5)

                #adding diff columns 
                for (name <- dif_cols) df = df.withColumn(name , lit("value"))
                df.show
                import org.apache.spark.sql.functions._
                #selecting cols in order 
                val df_final = df.select(master_cols.map(col): _*)
                df_final.show





#udf - data frame

import org.apache.spark.sql.functions.{col, udf}
val squared = udf((s: Long) => s * s)
display(spark.range(1, 20).select(squared(col("id")) as "id_squared"))
