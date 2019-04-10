

# new data
ndc,metric_dec_qty,cnt,rank,total_cnt
4778,0.143,200,2,3200
4778,0.140,3000,1,3200
0037,0.286,4566,1,4998
4777,0.143,3353,1,4299
0038,0.286,11382,1,12191

# historic data
ndc,metric_dec_qty,cnt,rank,total_cnt
4778,0.143,2226,1,2802
4778,0.140,576,2,2802
0037,0.286,4566,1,4998
4777,0.143,3353,1,4299
0037,0.286,4122,1,4542


#output : with updated rcords and updated ranks as per new count values
+-----------+--------------+-----+---------+----+                               
|        ndc|metric_dec_qty|  cnt|total_cnt|rank|
+-----------+--------------+-----+---------+----+
|4778|          0.14| 3576|     6002|   1|
|4778|         0.143| 2426|     6002|   2|
|  0037|         0.286| 9132|     9996|   1|
|4777|         0.143| 6706|     8598|   1|
|  0038|         0.286|11382|    12191|   1|
|  0037|         0.286| 4122|     4542|   1|
+-----------+--------------+-----+---------+----+


------------------------
pyspark - shell



 pyspark --queue pbm_yarn --master yarn --packages com.databricks:spark-csv_2.10:1.3.0


df = sqlContext.sql("select * from  "+input_db+"."+input_table)

rank_new = sqlContext.load(source="com.databricks.spark.csv", path = 'file:///home/srcrx1survbthdv/test_area/outlier_detection/metric_qty_lvl/test_data/rank_store_new.csv', header = True,inferSchema = True)

rank_history = sqlContext.load(source="com.databricks.spark.csv", path = 'file:///home/srcrx1survbthdv/test_area/outlier_detection/metric_qty_lvl/test_data/rank_store_history.csv', header = True,inferSchema = True)

rank_new.registerTempTable("new_data")

rank_history.registerTempTable("historic_data")

updated_records = " select * from historic_data a left  join ( select ndc as ndc_new, metric_dec_qty as metric_dec_qty_new,cnt as cnt_new,rank as rank_new,total_cnt as total_cnt_new from new_data) b on (a.ndc = b.ndc_new and a.metric_dec_qty = b.metric_dec_qty_new)"
df_updated = sqlContext.sql(updated_records)
df_updated.show()


df_unchanged = df_updated.where(col("ndc_new").isNull()).select("ndc", "metric_dec_qty", "cnt", "total_cnt")
df_unchanged.show()

# filtering unchanged and adding up cnts to update the fields
df_updated_new = df_updated.where(col("ndc_new").isNotNull()).selectExpr('ndc',' metric_dec_qty','cnt + cnt_new as cnt','total_cnt + total_cnt_new as total_cnt')

new_records = " select * from historic_data a right  join ( select ndc as ndc_new, metric_dec_qty as metric_dec_qty_new,cnt as cnt_new,rank as rank_new,total_cnt as total_cnt_new from new_data) b on (a.ndc = b.ndc_new and a.metric_dec_qty = b.metric_dec_qty_new)"
df_new = sqlContext.sql(new_records)
df_new = df_new.where(col("ndc").isNull()).selectExpr("ndc_new as ndc", "metric_dec_qty_new as metric_dec_qty", "cnt_new as cnt", "total_cnt_new as total_cnt")
df_new.show()


rank_new.show()
df_updated_new.show()
df_unchanged.show()
df_new.show()


#df_final = df_updated_new.union(df_unchanged).union(df_new)
df_final = df_updated_new.unionAll(df_unchanged).unionAll(df_new) # spark 1.6
df_final.show()

df_final.registerTempTable("final_tbl")

#ranking on cnt
df_final_new = sqlContext.sql( "select * , rank() over (partition by ndc  order by cnt desc)as rank from final_tbl")
df_final_new.show()
