
#create df



#method 1:


      from pyspark.sql import Row
      l = [('Ankit',25),('Jalfaizy',22),('saurabh',20),('Bala',26)]
      rdd = sc.parallelize(l)
      people = rdd.map(lambda x: Row(name=x[0], age=int(x[1])))
      schemaPeople = sqlContext.createDataFrame(people)





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



#stats mean, quantile and window function 

spark.version
# u'2.1.1'

sampleData = [("bob","Developer",125000),("mark","Developer",108000),("carl","Tester",70000),("peter","Developer",185000),("jon","Tester",65000),("roman","Tester",82000),("simon","Developer",98000),("eric","Developer",144000),("carlos","Tester",75000),("henry","Developer",110000)]

df = spark.createDataFrame(sampleData, schema=["Name","Role","Salary"])
df.show()
# +------+---------+------+ 
# |  Name|     Role|Salary|
# +------+---------+------+
# |   bob|Developer|125000| 
# |  mark|Developer|108000|
# |  carl|   Tester| 70000|
# | peter|Developer|185000|
# |   jon|   Tester| 65000|
# | roman|   Tester| 82000|
# | simon|Developer| 98000|
# |  eric|Developer|144000|
# |carlos|   Tester| 75000|
# | henry|Developer|110000|
# +------+---------+------+

med = df.approxQuantile("Salary", [0.5], 0.25) # no need to import DataFrameStatFunctions
med
# [98000.0]


import pyspark.sql.functions as func
from pyspark.sql import Window

windowSpec = Window.partitionBy(df['Role'])
df2 = df.withColumn('mean_salary', func.mean(df['Salary']).over(windowSpec))
df2.show()
# +------+---------+------+------------------+
# |  Name|     Role|Salary|       mean_salary| 
# +------+---------+------+------------------+
# |  carl|   Tester| 70000|           73000.0| 
# |   jon|   Tester| 65000|           73000.0|
# | roman|   Tester| 82000|           73000.0|
# |carlos|   Tester| 75000|           73000.0|
# |   bob|Developer|125000|128333.33333333333|
# |  mark|Developer|108000|128333.33333333333| 
# | peter|Developer|185000|128333.33333333333| 
# | simon|Developer| 98000|128333.33333333333| 
# |  eric|Developer|144000|128333.33333333333|
# | henry|Developer|110000|128333.33333333333| 
# +------+---------+------+------------------+


#cast str to decimal

dframe.withColumn("c_number", dframe.col("c_a").cast("decimal(38,0)"))




### Remove duplicates 

schema = 'id int, name string'
sampleDF = spark.createDataFrame(
[[1,'Scott'], 
[2,'Tiger'], 
[3,'Jane'], 
[4,'Jenny'], 
[5,'Judy'],
[3,'Jane'],
[2,'Tiger']], schema=schema)

# method - 1 : remove duplicates using distinct

>>> newDF = sampleDF.distinct()
>>> newDF.sort('id').show()
+---+-----+
| id| name|
+---+-----+
|  1|Scott|
|  2|Tiger|
|  3| Jane|
|  4|Jenny|
|  5| Judy|
+---+-----+

# method - 2 : remove duplicates using dropDuplicates

>>> newDF2 = sampleDF.dropDuplicates()
>>> newDF2.sort('id').show()
+---+-----+
| id| name|
+---+-----+
|  1|Scott|
|  2|Tiger|
|  3| Jane|
|  4|Jenny|
|  5| Judy|
+---+-----+

# method -3 : remove duplicates using  group by 

The GROUP BY clause is used to group the rows based on a set of specified grouping columns and
compute aggregations on the group of rows based on one or more specified aggregate function. 
You can use groupBy to group duplicate rows using the count aggregate function.

Consider following pyspark example remove duplicate from DataFrame using groupBy function.

Pyspark:

>>> newDF3 = sampleDF.groupBy("id", "name").count().select("id", "name").sort("id")
>>> newDF3.show()
+---+-----+
| id| name|
+---+-----+
|  1|Scott|
|  2|Tiger|
|  3| Jane|
|  4|Jenny|
|  5| Judy|
+---+-----+

# method - 4 : remove duplicates using row_number function

Spark Window functions are used to calculate results such as the rank, row number etc over a range of input rows.
The row_number() window function 
returns a sequential number starting from 1 within a window partition.
All duplicates values will have row number other then 1.

>>> from pyspark.sql.window import Window
>>> from pyspark.sql.functions import row_number

>>> newDF4 = sampleDF.withColumn("row_number", row_number().over(Window.partitionBy("id", "name").orderBy("id"))).where("row_number = 1").sort("id").select("id", "name")
>>> newDF4.show()
+---+-----+
| id| name|
+---+-----+
|  1|Scott|
|  2|Tiger|
|  3| Jane|
|  4|Jenny|
|  5| Judy|
+---+-----+

