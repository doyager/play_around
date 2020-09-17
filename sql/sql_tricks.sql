
-- calculate total num of occurances of empid , no of 'Y' for each empid , no of 'N' for each empid

  select EMP_ID , COUNT(EMP_ID),
  case when FRCST_IND = 'N' then count(  EMP_ID) else 0 end as  numOfN
  ,case when FRCST_IND = 'Y' then count( EMP_ID) else 0 end as  numOfY
  from SCHEMA1.EMPLOYEE_DATA_TABL
  group by EMP_ID,FRCST_IND;
  
  

-- get sum of members per week at state level for symptom of 'FEVER' for company id = ABC123
-- weekly sum of members at state level using state_nm and state_cd

SELECT   min_symp_impct_dt_frequency, 
                       st_cd,
                       ST_NM,
                          sum(totConfCase)       AS totConfCase       
                 FROM     ( 
                                     SELECT     CASE  WHEN (       ( 
                                                                                            cast(idfctn_dtm AS date) - (000101 (date))) + 1) mod 7 = 6 THEN cast(idfctn_dtm AS date) + 6
                                                           ELSE cast(idfctn_dtm AS date) + (6 - ((( cast(idfctn_dtm AS date) - (000101 (date))) + 1) mod 7 + 1))
                                                END AS min_symp_impct_dt_frequency, 
                                                 ste.st_cd,
                                                 ST_NM,
                                                symp_type_nm,         
                                                count(DISTINCT mcid) AS totalconfirmedcases
                                     FROM       ETL_VIEWS_ACIISST_C19.fact_mbr_symp symp 
                                     INNER JOIN ETL_VIEWS_ACIISST_C19.dim_st ste 
                                     ON         symp.st_cd=ste.st_cd 
                                     WHERE      symp_type_nm = 'FEVER' 
                                     AND        Diag_ind='Y' AND COMPANY_ID='ABC123' and st_nm = 'GEORGIA' 
                                     GROUP BY   min_symp_impct_dt_frequency, 
                                                symp_type_nm,ste.st_cd,ST_NM
              ) comb 
                 GROUP BY comb.min_symp_impct_dt_frequency,st_cd,ST_NM



-- Instead of Where clause , checking in select clause 
SELECT  mtrc.ITEM_ID,ITEM_NM, ITEM_DESC
CASE when ITEM_DESC='CAR' then SUM(NMRTR_AMT) else 0 end   as SalesNumberCar,
CASE when ITEM_DESC='BIKE' then SUM(DNMRTR_AMT) else 0 end   as SalesNumberBike
from table

-- adding unique series name based on metric id
CONCAT('series',TRIM(DENSE_RANK () OVER (order by mtrc.MTRC_ID) )) AS MTRC_SERIES_KEY  
                     
                     
                     
-- 30 day cumulative sum from current data
count( distinct (case when Date_DTM between current_date() - INTERVAL '30' DAY and current_date() and EMPLOYEE_IND='Y' then employee end) ) as empCountsThirtyDayCumSum,
                     
  
                     
                     
  -- CAST and zero check for denominator
   CASE totalMem WHEN 0 THEN 0 ELSE  ((CAST(numOfCases as DECIMAL(18,6)) /CAST(totalMem as DECIMAL(18,6)))*1000 ) END as perThousand,

