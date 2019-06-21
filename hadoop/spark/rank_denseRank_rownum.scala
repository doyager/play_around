
ROW_NUMBER()

… assigns unique numbers to each row within the PARTITION given the ORDER BY clause. So you’d get:

SELECT v, ROW_NUMBER() OVER()
FROM t

| V | ROW_NUMBER |
|---|------------|
| a |          1 |
| a |          2 |
| a |          3 |
| b |          4 |
| c |          5 |
| c |          6 |
| d |          7 |
| e |          8 |


RANK()

… behaves like ROW_NUMBER(), except that “equal” rows are ranked the same. If we substitute RANK() into our previous query:

SELECT v, RANK() OVER(ORDER BY v)
FROM t

| V | RANK |
|---|------|
| a |    1 |
| a |    1 |
| a |    1 |
| b |    4 |
| c |    5 |
| c |    5 |
| d |    7 |
| e |    8 |


DENSE_RANK()

Trivially, DENSE_RANK() is a rank with no gaps, i.e. it is “dense”. We can write:

SELECT v, DENSE_RANK() OVER(ORDER BY v)
FROM t
… to obtain

| V | DENSE_RANK |
|---|------------|
| a |          1 |
| a |          1 |
| a |          1 |
| b |          2 |
| c |          3 |
| c |          3 |
| d |          4 |
| e |          5 |



import org.apache.spark.sql.expressions.Window
import org.apache.spark.sql.functions._

val df = Seq(("a", 10), ("a", 10), ("a", 20)).toDF("col1", "col2")

val windowSpec = Window.partitionBy("col1").orderBy("col2")

df
  .withColumn("rank", rank().over(windowSpec))
  .withColumn("dense_rank", dense_rank().over(windowSpec))
  .withColumn("row_number", row_number().over(windowSpec)).show

+----+----+----+----------+----------+
|col1|col2|rank|dense_rank|row_number|
+----+----+----+----------+----------+
|   a|  10|   1|         1|         1|
|   a|  10|   1|         1|         2|
|   a|  20|   3|         2|         3|
+----+----+----+----------+----------+

##############################################

Assume input table,

CREATE TABLE t(v) AS
SELECT * FROM (
  VALUES('a'),('a'),('a'),('b'),
        ('c'),('c'),('d'),('e')
) t(v)


SELECT
  v, 
  ROW_NUMBER() OVER(ORDER BY v),
  RANK()       OVER(ORDER BY v),
  DENSE_RANK() OVER(ORDER BY v)
FROM t
ORDER BY 1, 2
… or this one (using the SQL standard WINDOW clause, to reuse window specifications):


SELECT
  v, 
  ROW_NUMBER() OVER(w),
  RANK()       OVER(w),
  DENSE_RANK() OVER(w)
FROM t
WINDOW w AS (ORDER BY v)
… to obtain:

| V | ROW_NUMBER | RANK | DENSE_RANK |
|---|------------|------|------------|
| a |          1 |    1 |          1 |
| a |          2 |    1 |          1 |
| a |          3 |    1 |          1 |
| b |          4 |    4 |          2 |
| c |          5 |    5 |          3 |
| c |          6 |    5 |          3 |
| d |          7 |    7 |          4 |
| e |          8 |    8 |          5 |
