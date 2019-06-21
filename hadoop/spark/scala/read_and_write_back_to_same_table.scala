
// checkpint() - will enable to do this


val sparkSession = SparkSession
			.builder()
			.appName("test-app")
			.config("spark.sql.warehouse.dir", "spark-warehouse")
			.enableHiveSupport()
			.getOrCreate()
      
      var df = spark.sql("select * , bround((quantity / days), 3) as qty_enriched from  " + schemaName + "." + Constants._INPUT_TBL.asInstanceOf[String]) 

 //val df_final = df_updated_new.union(df_unchanged).union(df_new)
    val df_final = df_updated_new.unionAll(df_unchanged).unionAll(df_new) // spark 1.6
    //df_final.show()

    df_final.createOrReplaceTempView("final_union_tbl")

    //ranking on cnt

    spark.sparkContext.setCheckpointDir("/tmp/checkPoint/rank_store");
    val df_final_ranks = spark.sql("select * , rank() over (partition by ndc  order by cnt desc)as rank from final_union_tbl").checkpoint()

    //df_final_ranks.show()

    df_final_ranks.write.mode("overwrite").saveAsTable(schemaName + "." + Constants.RANK_STORE_TBL.asInstanceOf[String])
    df_final_ranks.createOrReplaceTempView("final_tbl")
    df_final_ranks.cache()

    val insert_final_mode_score = "INSERT OVERWRITE TABLE " + schemaName + "." + Constants.RANK_STORE_TBL.asInstanceOf[String] + " select * from final_tbl"
    spark.sql(insert_final_mode_score)
