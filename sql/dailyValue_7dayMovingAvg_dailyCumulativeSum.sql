




SELECT 
symptom_date,
sum(confirmedcases) OVER(ORDER BY symptom_date ASC rows UNBOUNDED PRECEDING)               AS DailyCummulativeConfirmedcases,  -- caculates cumulative sum till date
AVG(confirmedcases)over (order by symptom_date ASC ROWS 6 PRECEDING ) as curr7DayAvgconfirmedcases,  -- calculates last 7 day avg till date 
 confirmedcases as dailyNewConfirmed. --- current day value 
FROM
(SELECT     cast(symptom_date AS date) AS symptom_date,
                                                 symp_type_nm,
                                                 count(DISTINCT mcid) AS confirmedcases
                                                 
                                      FROM       fact_mbr_symptom symptom
                                      INNER JOIN dim_st ste
                                      ON         symp.st_cd=ste.st_cd
                                      WHERE      symptom_type_name = 'FEVER'
                                      AND        idfctn_src_name = 'LAB'
                                      AND        frst_idfctn_ind='Y'     
                                      GROUP BY   symptom_date,
                                                 symptom_type_name)fQuery
                                                 
-- output datea 
Row. symptom_date.          DailyCUMULATIVECONFIRMEDCASES    CURR7DAYAVGCONFIRMEDCASES.  dailyNewConfirmed
1.  2020-01-04                         1                 1.000                           1
2.  2020-01-05                         2                 1.000                           1
3.  2020-01-06                         12                4.000                          10
4.  2020-01-07                         16                4.000                            4
5.  2020-01-08                         17                3.400                            1
6.  2020-01-09                         24                4.000                            7
7.  2020-01-10                         36                5.142                            12



                                                 
                                                 
                
