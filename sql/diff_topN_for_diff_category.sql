-- we want to show different top N values for each group , given top N for each category is adhoc we are creating a temp 
-- table using dual table concept 
with cat_topN as (SELECT *
FROM (
SELECT 'C1' Category, 3 topN FROM dual
UNION ALL
SELECT 'C2' Category, 2 TopN FROM dual)),
data as (
select Category,val,
row_number() over (partition by Category order by val desc) as rnk
from
(SELECT 'C1' Category, 5 val FROM dual
UNION ALL
SELECT 'C1' Category, 10 val FROM dual
UNION ALL
SELECT 'C1' Category, 15 val FROM dual
UNION ALL
SELECT 'C1' Category, 20 val FROM dual
UNION ALL
SELECT 'C1' Category, 25 val FROM dual
UNION ALL
SELECT 'C2' Category, 10 val FROM dual
UNION ALL
SELECT 'C2' Category, 20 val FROM dual
UNION ALL
SELECT 'C2' Category, 30 val FROM dual
UNION ALL
SELECT 'C2' Category, 40 val FROM dual
UNION ALL
SELECT 'C2' Category, 50 val FROM dual
))
select d.Category, d.val , d.rnk from data d join cat_topN c
on d.Category = c.Category
where rnk <= c.topN


o/p:
CATEGORY,VAL,RNK
C1	25	1
C1	20	2
C1	15	3
C2	50	1
C2	40	2
