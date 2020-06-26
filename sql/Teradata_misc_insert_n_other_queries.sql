
--insert statemnt
-- insert using select , to_timestamp and current_timestamp
INSERT INTO TABLE1 VALUES ( 10,( select USER_ID from SCHEMA1.TABLE_USER where LOGN_USER_ID='EMP1001'), 'Measues',1001, TO_TIMESTAMP('2020-06-08 10:13:39.000400', 'YYYY-MM-DD HH24:MI:SS.FF6'), 'ACCUNT1',1,1,'NA','DEV_ENV',current_timestamp,1,current_timestamp,1 );
