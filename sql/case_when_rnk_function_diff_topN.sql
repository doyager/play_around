-- usage of case when , with rank funciton


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
select d.Category, d.val , d.rnk,
CASE d.rnk 
                WHEN 1  THEN 'First-Rank'  
                WHEN 2  THEN 'Second-Rank' 
                WHEN 3 THEN 'Third-Rank' 
                WHEN 0 THEN 'No-Rank' 
                ELSE 'No-Rank'
            END AS Rank_Name

from data d join cat_topN c
on d.Category = c.Category
where rnk <= c.topN

o/p:
CATEGORY,VAL,RNK,RANK_NAME
C1	25	1	First-Rank
C1	20	2	Second-Rank
C1	15	3	Third-Rank
C2	50	1	First-Rank
C2	40	2	Second-Rank
