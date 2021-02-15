
# current date feb 1
# last 30 day - jan 30 to jan 1
#30beforelast 30 day - dec31 to dec 2

we have calculate diff of sum of member ids between last 30 days and 30before last 30 day 

-- Final query 
               
select 
numOfCasesThirtyDayCumSum,numOfCasesSixtyDayCumSum, numOfCasesLastThirtyDayCumSum,
CASE numOfCasesLastThirtyDayCumSum WHEN 0 THEN 0 ELSE CAST((((numOfCasesThirtyDayCumSum -numOfCasesLastThirtyDayCumSum )/numOfCasesLastThirtyDayCumSum)*100) as DECIMAL(18,6) ) END as pastThirtyPercentChnge
from 
(select 
       count( distinct (case when IDFCTN_DTM between dateadd(day,-30,current_timestamp()) and current_date() and SYMPTOM.SYMPTOM_TYPE_NM = 'FEVER' and SYMPTOM.FRST_IDFCTN_INDICATOR='Y' then MEMBER_ID end) ) as numOfCasesThirtyDayCumSum,
  count( distinct (case when IDFCTN_DTM between dateadd(day,-60,current_timestamp()) and current_date() and SYMPTOM.SYMPTOM_TYPE_NM = 'FEVER' and SYMPTOM.FRST_IDFCTN_INDICATOR='Y' then MEMBER_ID end) ) as numOfCasesSixtyDayCumSum,
 count( distinct (case when IDFCTN_DTM between dateadd(day,-60,current_timestamp()) and dateadd(day,-30,current_timestamp()) and SYMPTOM.SYMPTOM_TYPE_NM = 'FEVER' and SYMPTOM.FRST_IDFCTN_INDICATOR='Y' then MEMBER_ID end) ) as numOfCasesLastThirtyDayCumSum
                 from ALLDATA_SCHEMA.FACT_SYMPTOM SYMP
                 inner join  ALLDATA_SCHEMA.DIMENTION_STATE STE)
                 
                 

-- last 30 day i.e. jan 30 to jan 1 , current date feb 1
SELECT
    count(MEMBER_ID)
FROM
    fact_mbr_symp SYMP
INNER JOIN dim_st STE ON
    SYMP.ST_CD = STE.ST_CD
WHERE
    IDFCTN_DTM BETWEEN dateadd(DAY,-30, current_timestamp()) AND current_date()
    AND SYMPTOM.SYMPTOM_TYPE_NAME = 'FEVER'
    AND SYMPTOM.FIRST_IDFCTN_IND = 'Y' 
   --239211

-- 
-- 30 before last 30 days ie.. dec 31 to de 2, current date feb 1
SELECT
    count(MEMBER_ID)
FROM
    fact_mbr_symp SYMP
INNER JOIN dim_st STE ON
    SYMP.ST_CD = STE.ST_CD
WHERE
    IDFCTN_DTM BETWEEN dateadd(DAY,-60, current_timestamp()) AND dateadd(day,-30,current_timestamp())
     AND SYMPTOM.SYMPTOM_TYPE_NAME = 'FEVER'
    AND SYMPTOM.FIRST_IDFCTN_IND = 'Y' 
--  477908


