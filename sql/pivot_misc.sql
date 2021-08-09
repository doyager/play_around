

Ref 1: https://blogs.oracle.com/sql/how-to-convert-rows-to-columns-and-back-again-with-sql-aka-pivot-and-unpivot

Oracle Database 11g introduced the pivot operator. This makes switching rows to columns easy. To use this you need three things:

The column that has the values defining the new columns
What these defining values are
What to show in the new columns
The value in the new columns must be an aggregate. For example, count, sum, min, etc. Place a pivot clause containing these items after the table name, like so:

select * from table
pivot ( 3 for 1 in (2, 2, 2) );
So to create the final medal table from the raw data, you need to plug in:

You want the medals to become columns. So this is medal.
The values defining the columns are Gold, Silver and Bronze
You need how many rows there are for each colour. i.e. a count(*)
Stick it all together and you get:

select * from (
 select noc, medal from olympic_medal_winners
)
pivot ( 
 count(*) for medal in ( 'Gold' gold, 'Silver' silver, 'Bronze' bronze )
)
order  by 2 desc, 3 desc, 4 desc
fetch first 5 rows only;

NOC  GOLD  SILVER  BRONZE  
USA  47    40      40      
CHN  31    19      29      
GBR  30    26      19      
RUS  21    19      19      
GER  20    11      17



Reference 2 : https://www.oracletutorial.com/oracle-basics/oracle-pivot/

Oracle 11g introduced the new PIVOT clause that allows you to write cross-tabulation queries
which transpose rows into columns, aggregating data in the process of the transposing. As a result, the output of a pivot operation returns more columns and fewer rows than the starting data set.



SELECT 
    select_list
FROM 
    table_name
PIVOT [XML] ( 
    pivot_clause
    pivot_for_clause
    pivot_in_clause 
);
Code language: SQL (Structured Query Language) (sql)
In this syntax, following the PIVOT keyword are three clauses:

pivot_clause specifies the column(s) that you want to aggregate. The pivot_clause performs an implicitly GROUP BY based on all columns which are not specified in the clause, along with values provided by the pivot_in_clause.
pivot_for_clause specifies the column that you want to group or pivot.
pivot_in_clause defines a filter for column(s) in the pivot_for_clause. The aggregation for each value in the pivot_in_clause will be rotated into a separate column.


    SELECT * FROM order_stats PIVOT( COUNT(order_id) FOR category_name IN ( 'CPU', 'Video Card', 'Mother Board', 'Storage' ) ) ORDERBYstatus;

    





Exampel : My code
-- get MCID level coutns for each RQST_DESC group [We have 3 diff values for RQST_DESC]
WITH t1 as (select MCID,RQST_DESC From TABLE_A
where MCID= 1234567 -- added where to test at MCID level  )
Select * from t1
PIVOT ( count(*) for RQST_DESC in ('ACV_ACTUAL' ACV_ACTUAL_CNT , 'ACV_PCV' ACV_PCV_CNT , 'ACV_AI'  ACV_AI_CNT ) )

o/p:
MCID | ACV_ACTUAL_CNT | ACV_PCV_CNT | ACV_AI_CNT
1234567	    0	              3	            3
