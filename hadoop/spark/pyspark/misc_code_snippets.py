


# udf with multile input columns
# add up all array of column values 

 from pyspark.sql.types import IntegerType
>>> from pyspark.sql.functions import udf, array
>>> sum_cols = udf(lambda arr: sum(arr), IntegerType())
>>> spark.createDataFrame([(101, 1, 16)], ['ID', 'A', 'B']) \
...     .withColumn('Result', sum_cols(array('A', 'B'))).show()
+---+---+---+------+
| ID|  A|  B|Result|
+---+---+---+------+
|101|  1| 16|    17|
+---+---+---+------+
