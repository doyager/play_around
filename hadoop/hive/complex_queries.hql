
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
	      
