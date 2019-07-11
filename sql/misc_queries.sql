


--Where clause on timestamp

select  marks_id from MARKS where student_id = 102 AND (CREATED_TIMESTAMP  BETWEEN to_timestamp('2019-07-11 00:00:00', 'yyyy-mm-dd hh24:mi:ss')
 AND to_timestamp('2019-07-11 23:59:59', 'yyyy-mm-dd hh24:mi:ss')))


-- combination of LIKE and IN
-- regexp_like
select  emp_id from employee where  regexp_like(NAME,'mac-name1|mac-name2')             
                  
