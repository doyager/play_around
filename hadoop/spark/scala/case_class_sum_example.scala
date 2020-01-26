

Case classes are like regular classes with a few key differences which we will go over. 
Case classes are good for modeling immutable data. In the next step of the tour, 
we’ll see how they are useful in pattern matching.

####Defining a case class
A minimal case class requires the keywords case class, an identifier, and a parameter list (which may be empty):

case class Book(isbn: String)

val frankenstein = Book("978-0486282114")
Notice how the keyword new was not used to instantiate the Book case class. 
This is because case classes have an apply method by default which takes care of object construction.

When you create a case class with parameters, the parameters are public vals.

case class Message(sender: String, recipient: String, body: String)
val message1 = Message("guillaume@quebec.ca", "jorge@catalonia.es", "Ça va ?")

println(message1.sender)  // prints guillaume@quebec.ca
message1.sender = "travis@washington.us"  // this line does not compile
You can’t reassign message1.sender because it is a val (i.e. immutable). 
It is possible to use vars in case classes but this is discouraged.

####Comparison
Case classes are compared by structure and not by reference:

case class Message(sender: String, recipient: String, body: String)

val message2 = Message("jorge@catalonia.es", "guillaume@quebec.ca", "Com va?")
val message3 = Message("jorge@catalonia.es", "guillaume@quebec.ca", "Com va?")
val messagesAreTheSame = message2 == message3  // true
Even though message2 and message3 refer to different objects, the value of each object is equal.

#####Copying
You can create a (shallow) copy of an instance of a case class simply by using the copy method. 
You can optionally change the constructor arguments.

case class Message(sender: String, recipient: String, body: String)
val message4 = Message("julien@bretagne.fr", "travis@washington.us", "Me zo o komz gant ma amezeg")
val message5 = message4.copy(sender = message4.recipient, recipient = "claire@bourgogne.fr")
message5.sender  // travis@washington.us
message5.recipient // claire@bourgogne.fr
message5.body  // "Me zo o komz gant ma amezeg"
The recipient of message4 is used as the sender of message5 but the body of message4 was copied directly.











#######
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
