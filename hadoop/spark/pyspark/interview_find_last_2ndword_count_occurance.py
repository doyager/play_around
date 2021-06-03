'''
Find the last second word in the file and count the occurances of that word in the file .



Approach:
in the below created data frame "KENBFBF" is the last second word in the file and we will use that word to filter and then count 

'''



df = spark.createDataFrame([
  ["sample text 1 AFTEDGH XX"],
  ["sample text 2 GDHDH ZZ"],
  ["sample text 3 JEYHEHH YY"],
  ["sample text 4 QPRYRT EB"],
  ["sample text 5 KENBFBF XX"]
]).toDF("line")

+--------+
|word    |
+--------+
|AFTEDGH |
|GDHDH   |
|JEYHEHH |
|QPRYRT  |
|KENBFBF |
+--------+


import pyspark.sql.functions as F

df2 = df.withColumn('word', F.element_at(F.split(F.col('line'), ' '), -2))

df2.show(truncate=False)
+------------------------+-------+
|line                    |word   |
+------------------------+-------+
|sample text 1 AFTEDGH XX|AFTEDGH|
|sample text 2 GDHDH ZZ  |GDHDH  |
|sample text 3 JEYHEHH YY|JEYHEHH|
|sample text 4 QPRYRT EB |QPRYRT |
|sample text 5 KENBFBF XX|KENBFBF|
+------------------------+-------+



When you pass a string to the filter function, the string is interpreted as SQL. 
Count is a SQL keyword and using count as a variable confuses the parser. This is a small bug. 
You can easily avoid this. Instead of using a String use a column expression, as shown below:

df.groupBy("x").count()

  .filter($"count" >= 2)// or .filter("`count` >= 2")

  .show()
