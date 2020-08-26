
-- gets sum of numOfcases in last 30 days from the current date
--Teradata
select
SUM( (case when rptg_dt between current_date() - INTERVAL ''30'' DAY and current_date() then numOfCases else 0 end) ) as numOfCasesThirtyDayCumSum
from table 
