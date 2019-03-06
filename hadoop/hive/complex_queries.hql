
Hive :   It is an OLAP , and doest support OLTP 


hive vs rdbms


) AVRO:-

It is row major format.
Its primary design goal was schema evolution.
In the avro format, we store schema separately from data. Generally avro schema file (.avsc) is maintained.


2) ORC

Column oriented storage format.
Originally it is Hive's Row Columnar file. Now improved as Optimized RC (ORC)
Schema is with the data, but as a part of footer.
Data is stored as row groups and stripes.
Each stripe maintains indexes and stats about data it stores.

3) Parquet

Similar to ORC. Based on google dremel
Schema stored in footer
Column oriented storage format
Has integrated compression and indexes

Space or compression wise I found them pretty close to each other

Around 10 GB of CSV data compressed to 1.1 GB of ORC with ZLIB compression and same data to 1.2 GB of Parquet GZIP. Both file formats with SNAPPY compression, used around 1.6 GB of space.

Conversion speed wise ORC was little better it took 9 min where as parquet took 10 plus min.


Hive default delimiter

ctrl a character:
The default delimiter  '\u001'

sort by vs order by vs distribute by vs cluster by :

SORT BY : Hive uses to sort the rows before feeding the rows to a reducer
		Hive uses the columns in SORT BY to sort the rows before feeding the rows to a reducer. 
		The sort order will be dependent on the column types. If the column is of numeric type, 
		then the sort order is also in numeric order. If the column is of string type, then the sort
		order will be lexicographical order.  [lexicographical order.]

		Numeric - number oder 
		string - lexicographical order


		Ordering : It orders data at each of ‘N’ reducers , but each reducer can have overlapping ranges of data.

		Outcome : N or more sorted files with overlapping ranges.


		Let’s understand with an example of below query:-

		MySQL

		hive> SELECT emp_id, emp_salary FROM employees SORT BY emp_salary DESC;
		


ORDER BY . :  ORDER BY guarantees total ordering of data, but for that it has to be passed on to a single reducer, 

		This is similar to ORDER BY in SQL Language.

		In Hive, ORDER BY guarantees total ordering of data, but for that it has to be passed on to a single reducer, 
		which is normally performance intensive and therefore in strict mode, hive makes it compulsory to use LIMIT 
		with ORDER BY so that reducer doesn’t get overburdened.

		Ordering : Total Ordered data.

		Outcome : Single output i.e. fully ordered.

		For example :

		MySQL

		hive> SELECT emp_id, emp_salary FROM employees ORDER BY emp_salary DESC;
		1
		hive> SELECT emp_id, emp_salary FROM employees ORDER BY emp_salary DESC;

DISTRIBUTE BY : N reducers gets non-overlapping ranges of column, but doesn’t sort 

		It ensures each of N reducers gets non-overlapping ranges of column, but doesn’t sort the output of each reducer. 
		You end up with N or more unsorted files with non-overlapping ranges.

		Example ( taken directly from Hive wiki ):-

		We are Distributing By x on the following 5 rows to 2 reducer:


			x1
			x2
			x4
			x3
			x1

			Reducer 1
			x1
			x2
			x1
			Reducer 2
			x4
			x3


Cluster By : is a short-cut for both Distribute By and Sort By.

		CLUSTER BY x ensures each of N reducers gets non-overlapping ranges, then sorts by those ranges at the reducers.

		Ordering : Global ordering between multiple reducers.

		Outcome : N or more sorted files with non-overlapping ranges.

		For the same example as above , if we use Cluster By x, the two reducers will further sort rows on x:

		Reducer 1 :
		x1
		x1
		x2


		Reducer 2 :
		x3
		x4
		
		

# find max date employee rrecord:


       1. simple 
	m
	select t1.* from test t1
	join (
	  select id, max(modifed) maxModified from test
	  group by id
	) s
	on t1.id = s.id and t1.modifed = s.maxModified
	
	2. window - row function
	
			SELECT t.id
		    ,t.name
		    ,t.age
		    ,t.modified
		FROM (
		    SELECT id
			,name
			,age
			,modified
			,ROW_NUMBER() OVER (
			    PARTITION BY id ORDER BY unix_timestamp(modified,'yyyy-MM-dd hh:mm:ss') DESC
			    ) AS ROW_NUMBER   
		    FROM test
		    ) t
		WHERE t.ROW_NUMBER <= 1;




#Index

#window functions
# common table expression


# window functions

# moving avg over 4 rows 
# moving average over 4 rows including current one [i.e. last 3 records and current one]
# so for first 3 rows in the result data set , for row 1 - it is avg of only first col , for row 2 - avg of row1 & row 2
# for row 3 - avg of row 1,2,3 and from row 4 - it will have the avg for four rows - row 1,2,3,4 
# for row 5 - avg of row 2,3,4 and row 5

from groceries
select id, revenue, day,
avg(revenue) over (
order by id
rows between 3 preceding and current row
)
as running_avgerage;

# moving average over all the top records including current one, ie,.for row 3 moving_avg woudl be, avg includes  row1,2 and row3
eg 2: for row 10 moving_avg would be, avg includes  row1,2,3,4,5...9 and row10

from groceries
select id, revenue, day,
avg(revenue) over (
order by id
rows between unbounded preceding and current row
)
as running_avgerage;

# sums up the revenue over entire partition
# running sum over a day with out order by id -> sums up the count over entire partition  , 
from groceries
select id, revenue, day,
sum(revenue) over (
partition by day
)
as running_sum;



# running total per day , here we order by id within the partition

from groceries
select id, revenue, day,
sum(id) over (
partition by day
order by id)
as running_total;

# running count over a day , i.e. group by each day and count per day group  wihtin group, here we order by id within the partition
from groceries
select id, revenue, day,
count(id) over (
partition by day
order by id)
as running_count;

Note : if we dont use order by id with in the over function , then the total_count for all the rows will be same 
as the count will not be all" unbounded preceding including current one" i.e for row 3 it is rows 1, 2 and row 3 but it will be "unbounded preceding and 
unbounded following " ie.. for ever row it includes all the rows above it and all rows below it hence the total
coutn will be same for all the rows with in the day partition

# running count over a day with out order by id -> sums up the count over entire partition  , 

from groceries
select id, revenue, day,
count(id) over (
partition by day
)
as running_count;

# row_number(), this will give a row number within every partition 
#row number alwasy assigns unique value within partiiton even if the values are same
# here row_number will reset for ever date ie.. day , as day is our partition
# every record has unique row_number within a partition

from groceries
select id,product,day,
row_number() over (partition by day order by id)
as row_number;

o/p:

id | product | day | row_number
01 banan . 2017-01-01 1
02 banan . 2017-01-02 1
03 banan . 2017-01-02 2
03 apple . 2017-01-02 3
04 banan . 2017-01-03 1
05 banan . 2017-01-04 1
06 banan . 2017-01-04 2
07 banan . 2017-01-04 3
08 banan . 2017-01-04 4


# rank() , rank function
# ranks are NOT unique over a window
# rank window funciton works exactly likerow_number() except that two rows with the same order id will have the same rank
# observe the result for day 2
from groceries
select id,product,day,
rank() over (partition by day order by id)
as rank;

o/P:

id | product | day | rank
01 banan . 2017-01-01 1
02 banan . 2017-01-02 1
03 banan . 2017-01-02 2
03 apple . 2017-01-02 2
04 banan . 2017-01-03 1
05 banan . 2017-01-04 1
06 banan . 2017-01-04 2
07 banan . 2017-01-04 3
08 banan . 2017-01-04 4

Note: with same order id 3 , this two records have same rank

# rank and limit the rank
select * from (
	select user_id, value, desc, 
	rank() over ( partition by user_id order by value desc) as rank 
	from test4 ) t where rank < 3;
The output looks like this:

OK
1	2	hallo	1
1	1	hallo	2
2	11	hallo4	1
2	10	hallo3	2


# cummulative sum :

select
name,
amount,
 SUM(amount)
over
 (
 order by name
 rows between unbounded preceding and current row
 ) cumulative_Sum
from test;
Output:

name	amount	cumulative sum
abc	100	100
abc	200	300
bcd	100	400
bcd	100	500
bcd	100	600
cde	400	1000
cde	400	1400
efg	600	2000
efg	600	2600


# common table expression :

A Common Table Expression (CTE) is a temporary result set derived from a simple query specified in a WITH clause, 
which immediately precedes a SELECT or INSERT keyword.  The CTE is defined only within the execution scope of a 
single statement.  One or more CTEs can be used in a Hive SELECT, INSERT, CREATE TABLE AS SELECT, or 
CREATE VIEW AS SELECT statement.

CTE in Select Statements
with q1 as ( select key from src where key = '5')
select *
from q1;
 
-- from style
with q1 as (select * from src where key= '5')
from q1
select *;
  
-- chaining CTEs
with q1 as ( select key from q2 where key = '5'),
q2 as ( select key from src where key = '5')
select * from (select key from q1) a;
  
-- union example
with q1 as (select * from src where key= '5'),
q2 as (select * from src s2 where key = '4')
select * from q1 union all select * from q2;

# CTE With rank 


# CTE with rank() function : common tbt expression with windowing function rank 
with q1 as (select ndc, metric_qty, count(*) as cnt from dv_db.clm_test group by ndc, metric_qty)
 select * , rank() over (partition by ndc order by cnt desc)as rank from q1;

 +------------+---------------------+---------+-------+--+
|   q1.ndc   |  q1.metric_qty  | q1.cnt  | rank  |
+------------+---------------------+---------+-------+--+
| 37826  | 0.5                 | 5       | 1     |
| 37826  | 0.6000000238418579  | 3       | 2     |
| 37826  | 1.0                 | 1       | 3     |
| 37826  | 0.800000011920929   | 1       | 3     |
+------------+---------------------+---------+-------+--+

# CTE with rank and filter rank 

set mapred.job.queue.name = root.team1;
with
q1 as (select ndc, metric_dec_qty, count(*) as cnt from dv_db.clm_test group by ndc, metric_dec_qty)
,q2 as (select * , rank() over (partition by ndc  order by cnt desc)as rank from q1)
select * from q2 where rank < 2;


INFO  : Stage-Stage-1: Map: 1  Reduce: 1   Cumulative CPU: 16.14 sec   HDFS Read: 8018 HDFS Write: 204 SUCCESS
INFO  : Stage-Stage-2: Map: 1  Reduce: 1   Cumulative CPU: 13.75 sec   HDFS Read: 8020 HDFS Write: 18 SUCCESS
INFO  : Total MapReduce CPU Time Spent: 29 seconds 890 msec
INFO  : Completed executing command(queryId=hive_20190201150707_4378a030-c67f-4c87-9c9e-00675587b5ab); Time taken: 88.005 seconds
INFO  : OK
DEBUG : Shutting down query with
q1 as (select ndc, metric_dec_qty, count(*) as cnt from dv_db.clm_test group by ndc, metric_qty)
,q2 as (select * , rank() over (partition by ndc  order by cnt desc)as rank from q1)
select * from q2 where rank < 2
+------------+--------------------+---------+----------+--+
|   q2.ndc   | q2.metric_qty  | q2.cnt  | q2.rank  |
+------------+--------------------+---------+----------+--+
| 378262 | 0.5                | 5       | 1        |
+------------+--------------------+---------+----------+--+


# CTE with rank and filter rank and sum per each group 
#to find the most frequent value per group and even the total sum of all values consider per group and printing the
# top rank in each group

with q1 as (select ndc, metric_dec_qty, count(*) as cnt from "+input_db+"."+input_table+" group by ndc, metric_dec_qty) 
,q2 as (select * , rank() over (partition by ndc  order by cnt desc)as rank from q1)
, q3 as (select *, sum(cnt) over (partition by ndc order by ndc) as total_cnt from q2)
select * from q3 where rank < 2


# multiple CTE

A single scan.

Note:
- a single stage
- a single TableScan
- predicate: (((i = 1) and (j = 2)) and (k = 3)) (type: boolean)

create table t (i int,j int,k int);

explain 
with    t1 as (select i,j,k from t  where i=1)
       ,t2 as (select i,j,k from t1 where j=2)
       ,t3 as (select i,j,k from t2 where k=3) 

select * from t3
;
Explain
STAGE DEPENDENCIES:
  Stage-0 is a root stage

STAGE PLANS:
  Stage: Stage-0
    Fetch Operator
      limit: -1
      Processor Tree:
        TableScan
          alias: t
          Statistics: Num rows: 1 Data size: 0 Basic stats: PARTIAL Column stats: NONE
          Filter Operator
            predicate: (((i = 1) and (j = 2)) and (k = 3)) (type: boolean)
            Statistics: Num rows: 1 Data size: 0 Basic stats: PARTIAL Column stats: NONE
            Select Operator
              expressions: 1 (type: int), 2 (type: int), 3 (type: int)
              outputColumnNames: _col0, _col1, _col2
              Statistics: Num rows: 1 Data size: 0 Basic stats: PARTIAL Column stats: NONE
              ListSink
	      
	      
	      
# OFFSET 

	# offset by 10 and select next 5 only

		SELECT Id, ProductName, UnitPrice, Package
		FROM Product
		ORDER BY UnitPrice DESC
		OFFSET 10 ROWS
		FETCH NEXT 5 ROWS ONLY
