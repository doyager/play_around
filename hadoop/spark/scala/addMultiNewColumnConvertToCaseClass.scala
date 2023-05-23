// add multiple new columns using withColumn , then convert to a case class


import spark.implicits._

//final schema column list , here SCD is the case class name
val scdColumns = spark.emptyDataset[SCDSchema].columns.map(col)

//adding this three new columns will add all required columns to newDF to make it SCD schema 
val newDfAsSCD = newDf.toDF
                  .withColumn("col10",lit("test1"))
                  .withColumn("col11",lit(false))
                  .withColumn("ds",col(dsCol))
                  .select(scdColumns:_*)
                  .as[SCD]
