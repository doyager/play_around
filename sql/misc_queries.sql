
--like 
Select *  From tbl Where name like 'saho%'

-- like in :

Select *  From tbl Where regexp_like(name,'^sasho$|^rags$|^shashi*');

-- listagg : 
--concate column after group by 
      select deptno, listagg(ename, ';' ) within group (order by ename) from scott.emp group by deptno order by deptno;

          DEPTNO .  LISTAGG(ENAME,';')WITHINGROUP(ORDERBYENAME)
              10   CLARK;KING;MILLER


--Where clause on timestamp

select  marks_id from MARKS where student_id = 102 AND (CREATED_TIMESTAMP  BETWEEN to_timestamp('2019-07-11 00:00:00', 'yyyy-mm-dd hh24:mi:ss')
 AND to_timestamp('2019-07-11 23:59:59', 'yyyy-mm-dd hh24:mi:ss')))


-- combination of LIKE and IN
-- regexp_like
select  emp_id from employee where  regexp_like(NAME,'mac-name1|mac-name2')    
                  
                  
-- json data - group by and concate (select columns)
-- group by on json column data = "DATA" , where one col is id and other col is cNbr                 
                  
        SELECT  JSON_VALUE(DATA,'$.id'),JSON_VALUE(DATA,'$.cNbr'),listagg(JSON_VALUE(DATA,'$.actn_cd'),'|') within group  (order by JSON_VALUE(DATA,'$.cNbr'))from REFERENCE_DATA A where  W_ID in (
       select  W_ID from VA302.W_ITEM where W_QUEUE_ID in (select  W_QUEUE_ID from W_QUEUE where  regexp_like(NAME,'address issue|card issue')) AND (CREATED_TIMESTAMP  BETWEEN to_timestamp('2019-07-11 00:00:00', 'yyyy-mm-dd hh24:mi:ss')
        AND to_timestamp('2019-07-11 23:59:59', 'yyyy-mm-dd hh24:mi:ss'))) AND QUALIFIER is NULL  Group by  (JSON_VALUE(DATA,'$.id'),JSON_VALUE(DATA,'$.cNbr')) ;

        id	     cNbr	       actn_cd
       23104316	19168BD4857	R01030
       25931316	19166BN3139	R01030
       31929282	19168BJ6247	RG2400|RG2400
       36477702	19165MD7791	R01030

                  
