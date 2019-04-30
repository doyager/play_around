#in shell
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
