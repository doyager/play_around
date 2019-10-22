
case class UserLogin( timestamp:String , type String , userID: String, classInfo : String , LogActivity1 :String, LogActivity2 :String)

val df = spark.read.option("delimiter"," ").csv("/usr/user1/logs/log_10_22_2019.txt");

val log_df = df.as[UserLogin]

log_df.registerTemTable("logs_tbl");

val login_cnts = spark.sql("select userID,count(*) as logins from logs_tbl where LogActivity2='IN' groupBy userID ");

[1001]

1001 , 1
1002, 0

//tcolkp_users
val userDetails ; //table already loaded as datagrame

val join_df = login_cnts.join(userDetails,userDetails("id") == login_cnts("userID",left)

val result = join_df.select(`name, logins`)
result.show()
