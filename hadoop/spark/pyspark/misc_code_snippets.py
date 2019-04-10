
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

