

###NATURAL JOIN operation
A NATURAL JOIN is a JOIN operation that creates an implicit join clause for you based on the common columns in the two tables being joined. Common columns are columns that have the same name in both tables.

A NATURAL JOIN can be an INNER join, a LEFT OUTER join, or a RIGHT OUTER join. The default is INNER join.

If the SELECT statement in which the NATURAL JOIN operation appears has an asterisk (*) in the select list, the asterisk will be expanded to the following list of columns (in this order):

All the common columns
Every column in the first (left) table that is not a common column
Every column in the second (right) table that is not a common column
An asterisk qualified by a table name (for example, COUNTRIES.*) will be expanded to every column of that table that is not a common column.

If a common column is referenced without being qualified by a table name, the column reference points to the column in the first (left) table if the join is an INNER JOIN or a LEFT OUTER JOIN. If it is a RIGHT OUTER JOIN, unqualified references to a common column point to the column in the second (right) table.

Syntax
TableExpression NATURAL [ { LEFT | RIGHT } [ OUTER ] | INNER ] JOIN { TableViewOrFunctionExpression | ( TableExpression ) }
Examples
If the tables COUNTRIES and CITIES have two common columns named COUNTRY and COUNTRY_ISO_CODE, the following two SELECT statements are equivalent:

1.  SELECT * FROM COUNTRIES NATURAL JOIN CITIES

2.   SELECT * FROM COUNTRIES JOIN CITIES
    USING (COUNTRY, COUNTRY_ISO_CODE)

Both 1 and 2 are equivalent



-- greater than time stamp

select * from emp where CREATED_TIMESTAMP > to_timestamp('2019-08-29 01:12:40','yyyy-mm-dd hh24.mi.ss') 

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

                  
