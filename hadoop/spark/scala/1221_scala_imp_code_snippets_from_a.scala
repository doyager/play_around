

//dedupe using row number logic 

val df = dfRaw.withColumn("latestRow",
                              row_number().over(
                              Window
                              .partitionBy( $"idDept")
                              .orderBy($"tsLastUpdateAt".desc)
                           )
                          ).filter("latestRow == 1")
                         .drop("latestRow")
-----------------

// filter data frame to get just values equalt to cat 

val dfFilter_catOnly = df.filter($"animal_name" === "CAT")


// filter data frame to get  values OTHER THAN cat 

val dfFilter_notCat = df.filter($"animal_name" =!= "CAT")
# !== is deprecated , so we use =!= instead of !==
-----------------

//to add colum, filter based on conditions ( list of values for col , date time , hour , date ) value of 
 sparkSession.udf.register("ensureTimestampInRange", HelperTools.standardizeToEpochMilliseconds _)
.withColumn(
        "eventSuccessFlag",
        when($"eventType" isInCollection Const.EventMap("SUCCESS") and $"status" === "SUCCEEDED", 1)
          .otherwise(0)
      )
      .withColumn(
        "eventFailFlag",
        when($"eventType" isInCollection Const.EventMap("FAIL") and $"status" === "FAILED", 1)
          .otherwise(0)
      )
      .filter($"eventSuccessFlag" === 1 || $"eventFailFlag" === 1)
      .filter($"ds" === date_add(lit(endDate.toString), 1))
      .filter($"hr" <= hourPartition)
      .filter(from_unixtime(expr("ensureTimestampInRange(createdAt)/1000.0")) >= startDate.toString + " 00:00:00")
      .filter(from_unixtime(expr("ensureTimestampInRange(createdAt)/1000.0")) <= endDate.toString + " 23:59:59")
      .withColumn("createdAtTs", from_unixtime(expr("ensureTimestampInRange(createdAt)/1000.0")))


//add literal value
.withColumn("createdAtTs", from_unixtime(expr("ensureTimestampInRange(createdAt*1000)/1000.0")))
      .withColumn("hr", lit("all"))
