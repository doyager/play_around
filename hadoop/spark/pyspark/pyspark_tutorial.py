
# ways of creating Data frame
l = [('Alice', 1)]
>>> spark.createDataFrame(l).collect()
[Row(_1='Alice', _2=1)]
>>> spark.createDataFrame(l, ['name', 'age']).collect()
[Row(name='Alice', age=1)]
>>> d = [{'name': 'Alice', 'age': 1}]
>>> spark.createDataFrame(d).collect()
[Row(age=1, name='Alice')]
>>> rdd = sc.parallelize(l)
>>> spark.createDataFrame(rdd).collect()
[Row(_1='Alice', _2=1)]
>>> df = spark.createDataFrame(rdd, ['name', 'age'])
>>> df.collect()
[Row(name='Alice', age=1)]
>>> from pyspark.sql import Row
>>> Person = Row('name', 'age')
>>> person = rdd.map(lambda r: Person(*r))
>>> df2 = spark.createDataFrame(person)
>>> df2.collect()
[Row(name='Alice', age=1)]
>>> from pyspark.sql.types import *
>>> schema = StructType([
...    StructField("name", StringType(), True),
...    StructField("age", IntegerType(), True)])
>>> df3 = spark.createDataFrame(rdd, schema)
>>> df3.collect()
[Row(name='Alice', age=1)]
>>> spark.createDataFrame(df.toPandas()).collect()  
[Row(name='Alice', age=1)]
>>> spark.createDataFrame(pandas.DataFrame([[1, 2]])).collect()  
[Row(0=1, 1=2)]
>>> spark.createDataFrame(rdd, "a: string, b: int").collect()
[Row(a='Alice', b=1)]
>>> rdd = rdd.map(lambda row: row[1])
>>> spark.createDataFrame(rdd, "int").collect()
[Row(value=1)]
>>> spark.createDataFrame(rdd, "boolean").collect() 

6.

df.createOrReplaceTempView("table1")
>>> df2 = spark.sql("SELECT field1 AS f1, field2 as f2 from table1")
>>> df2.collect()
[Row(f1=1, f2='row1'), Row(f1=2, f2='row2'), Row(f1=3, f2='row3')]

7. 

          range(start, end=None, step=1, numPartitions=None)[source]
          Create a DataFrame with single pyspark.sql.types.LongType column named id, containing elements in a range from start to end (exclusive) with step value step.

          Parameters
          start – the start value

          end – the end value (exclusive)

          step – the incremental step (default: 1)

          numPartitions – the number of partitions of the DataFrame

          Returns
          DataFrame

Range:

sqlContext.range(1, 7, 2).collect()
[Row(id=1), Row(id=3), Row(id=5)]
If only one argument is specified, it will be used as the end value.

>>> sqlContext.range(3).collect()
[Row(id=0), Row(id=1), Row(id=2)]
