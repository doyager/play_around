

-- Instead of Where clause , checking in select clause 
SELECT  mtrc.ITEM_ID,ITEM_NM, ITEM_DESC
CASE when ITEM_DESC='CAR' then SUM(NMRTR_AMT) else 0 end   as SalesNumberCar,
CASE when ITEM_DESC='BIKE' then SUM(DNMRTR_AMT) else 0 end   as SalesNumberBike
from table

-- adding unique series name based on metric id
CONCAT('series',TRIM(DENSE_RANK () OVER (order by mtrc.MTRC_ID) )) AS MTRC_SERIES_KEY  
                     
                     
                     
-- 30 day cumulative sum from current data
count( distinct (case when Date_DTM between current_date() - INTERVAL '30' DAY and current_date() and EMPLOYEE_IND='Y' then employee end) ) as empCountsThirtyDayCumSum,

