


#########################################
## Case class

Recipe for this is given below

1. Start the spark shell and give it some additional memory:

 $ spark-shell --driver-memory 1G
2. Import for the implicit conversations:

 scala> import sqlContext. implicits._
3. Create a person case class:

 scala> case class Person (first_name:String,last_name: String,age:Int)
4. In another shell, create some sample data to be put in HDFS:

$ mkdir person
$ echo "Barack,Obama,53" >>person/person.txt
$ echo "George,Bush,68" >>person/person.txt
$ echo "Bill,Clinton,68" >>person/person.txt
$ hdfs dfs -put person person
5. Load the person directly as on RDD:

 scala> val p = sc.textFile ("hdfs://localhost:9000/user/hduser/person")
6. Split each line into an array of string, based on a comma, as a delimiter:

 val pmap = p.map ( line => line.split (","))
7. Convert the RDD of Array[string] into the RDD of person case objects:

 scala> val personRDD = pmap.map ( p => Person (p(0), p(1), p(2). toInt))
8. Convert the personRDD into the personDF DataFrame:

 scala> val personDF = personRDD. toDF
9. Register the personDF as a table:

 scala> personDF.registerTempTable ("person")
10. Run a SQL query against it:

 scala> val people = SQL ("select * from person")
11. Get the output values from persons:

 scala> people.collect.foreach (printIn)
 
 #########################################
