
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
