
# syntax

%scala
import org.apache.spark.sql.types.StructType
import org.apache.spark.sql.catalyst.ScalaReflection

case class A(key: String, time: java.sql.Timestamp, date: java.sql.Date, decimal: java.math.BigDecimal, map: Map[String, Int], nested: Seq[Map[String, Seq[Int]]])
val schema = ScalaReflection.schemaFor[A].dataType.asInstanceOf[StructType]
schema.printTreeString


#########################################
## Case class
# Link : http://www.infoobjects.com/2016/06/21/spark-inferring-schema-using-case-classes/
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

#### case class 2  with triats addition
#link : https://blog.codecentric.de/en/2016/07/spark-2-0-datasets-case-classes/


val df: DataFrame = spark.read
                         .schema(schema)
                         .option("header", true)
                         .csv("/path/to/bodies.csv")

val id       = StructField("id",       DataTypes.IntegerType)
val width    = StructField("width",    DataTypes.DoubleType)
val height   = StructField("height",   DataTypes.DoubleType)
val depth    = StructField("depth",    DataTypes.DoubleType)
val material = StructField("material", DataTypes.StringType)
val color    = StructField("color",    DataTypes.StringType)
 
val fields = Array(id, width, height, depth, material, color)
val schema = StructType(fields)

#Spark 2.0 introduces Datasets to better address these points. The take away message is that instead of using type agnostic Rows,
#one can use Scala’s case classes or tuples to describe the contents of the rows. The (not so) magic gluing is done by using as on 
#a Dataframe. (Tupels would match by position and also lack the possibility to customize naming.)

final case class Body(id: Int, 
                      width: Double, 
                      height: Double, 
                      depth: Double, 
                      material: String, 
                      color: String)
 
val ds = df.as[Body]
#The matching between the DataFrames columns and the fields of the case class is done by name and the types should match. 
#In summary, this introduces a contract and narrows down possible sources of error. For example, one immediate benefit is 
#that we can access fields via the dot operator and get additional IDE support:

val colors = ds.map(_.color) // Compiles!
ds.map(_.colour)             // Typo - WON'T compile!
#Further, we can use this feature and the newly added type-safe aggregation functions to write queries with compile time safety:

import org.apache.spark.sql.expressions.scalalang.typed.{
  count => typedCount, 
  sum => typedSum}
 
ds.groupByKey(body => body.color)
  .agg(typedCount[Body](_.id).name("count(id)"),
       typedSum[Body](_.width).name("sum(width)"),
       typedSum[Body](_.height).name("sum(height)"),
       typedSum[Body](_.depth).name("sum(depth)"))
  .withColumnRenamed("value", "group")
  .alias("Summary by color level")
  .show()
#If we wanted to compute the volume of all bodies, this would be quite straightforward in the DataFrame API.
#Two solutions come to mind:

// 1. Solution: Using a user-defined function and appending the results as column
val volumeUDF = udf {
 (width: Double, height: Double, depth: Double) => width * height * depth
}
 
ds.withColumn("volume", volumeUDF($"width", $"height", $"depth"))
 
// 2. Solution: Using a SQL query
spark.sql(s"""
           |SELECT *, width * height * depth
           |AS volume
           |FROM bodies
           |""".stripMargin)



# udf 
// 1. Solution: Using a user-defined function and appending the results as column
val volumeUDF = udf {
 (width: Double, height: Double, depth: Double) => width * height * depth
}
 
ds.withColumn("volume", volumeUDF($"width", $"height", $"depth"))
 
// 2. Solution: Using a SQL query
spark.sql(s"""
           |SELECT *, width * height * depth
           |AS volume
           |FROM bodies
           |""".stripMargin)



ds.map { 
 body => 
  val volume = body.width * body.height * body.depth
  BodyWithVolume(body.id, body.width, body.height, body.depth, body.material, body.color, volume)
}


# traits 
trait IsIdentifiable {
 def id: Int
}
 
trait HasThreeDimensions {
 def width: Double
 def height: Double
 def depth: Double
}
 
trait ConsistsOfMaterial {
 def material: String
 def color: String
}
 
trait HasVolume extends HasThreeDimensions {
 def volume = width * height * depth
}
 
final case class Body(id: Int, 
                      width: Double, 
                      height: Double, 
                      depth: Double, 
                      material: String, 
                      color: String) extends 
                      IsIdentifiable with 
                      HasThreeDimensions with 
                      ConsistsOfMaterial
 
final case class BodyWithVolume(id: Int, 
                                width: Double, 
                                height: Double, 
                                depth: Double, 
                                material: String, 
                                color: String) extends 
                                IsIdentifiable with 
                                HasVolume with 
                                ConsistsOfMaterial


Traits:

A trait encapsulates method and field definitions, which can then be reused by mixing them into classes.

"""Unlike class inheritance, in which each class must inherit from just one superclass, 
a class can mix in any number of traits."""

Traits are used to define object types by specifying the signature of the supported methods. Scala also allows traits to be partially implemented but traits may not have constructor parameters.

"""A trait definition looks just like a class definition except that it uses the keyword trait.
The following is the basic example syntax of trait."""

trait Equal {
   def isEqual(x: Any): Boolean
   def isNotEqual(x: Any): Boolean = !isEqual(x)
}



#When to Use Traits?
There is no firm rule, but here are few guidelines to consider −

If the behavior will not be reused, then make it a concrete class. It is not reusable behavior after all.

If it might be reused in multiple, unrelated classes, make it a trait. Only traits can be mixed into different parts of the class hierarchy.

If you want to inherit from it in Java code, use an abstract class.

If you plan to distribute it in compiled form, and you expect outside groups to write classes inheriting from it, you might lean towards using an abstract class.

If efficiency is very important, lean towards using a class.



#################################################
#################################################
"""Complete example"""

#Syntax
trait Equal {
   def isEqual(x: Any): Boolean
   def isNotEqual(x: Any): Boolean = !isEqual(x)
}
This trait consists of two methods isEqual and isNotEqual. 
Here, we have not given any implementation for isEqual where as another method has its implementation. 
Child classes extending a trait can give implementation for the un-implemented methods. 

"""So a trait is very similar to what we have abstract classes in Java."""

Let us assume an example of trait Equal contain two methods isEqual() and isNotEqual(). 
The trait Equal contain one implemented method that is isEqual() 
so when user defined class Point extends the trait Equal, implementation to isEqual()
method in Point class should be provided.

Here it is required to know two important method of Scala, which are used in the following example.

obj.isInstanceOf [Point] To check Type of obj and Point are same are not.

obj.asInstanceOf [Point] means exact casting by taking the object obj type and returns the same obj as Point type.

Try the following example program to implement traits.

######################
####Example
trait Equal {
   def isEqual(x: Any): Boolean
   def isNotEqual(x: Any): Boolean = !isEqual(x)
}

class Point(xc: Int, yc: Int) extends Equal {
   var x: Int = xc
   var y: Int = yc
   
   def isEqual(obj: Any) = obj.isInstanceOf[Point] && obj.asInstanceOf[Point].x == y
}

object Demo {
   def main(args: Array[String]) {
      val p1 = new Point(2, 3)
      val p2 = new Point(2, 4)
      val p3 = new Point(3, 3)

      println(p1.isNotEqual(p2))
      println(p1.isNotEqual(p3))
      println(p1.isNotEqual(2))
   }
}
Save the above program in Demo.scala. The following commands are used to compile and execute this program.
######################
###Command
\>scalac Demo.scala
\>scala Demo
####Output
true
false
true
#################################################
#################################################



"""
Abstract class
In Scala, an abstract class is constructed using the abstract keyword.
It contains both abstract and non-abstract methods and cannot support multiple inheritances.

Traits
Like a class, Traits can have methods(both abstract and non-abstract), and fields as its members. Traits are just like interfaces in Java. 
But they are more powerful than the interface in Java because in the traits we are allowed to implement the members.

                                      Traits vs Abstract class
#1 Traits support multiple inheritance.	                 #1 Abstract class does not support multiple inheritance.
#2We are allowed to add a trait to an object instance.	  #2 abstract class - We are not allowed to add an abstract class to an object instance.
#3Traits does not contain constructor parameters.	       #3 Abstract class contain constructor parameters.
#4Traits are completely interoperable only when they     #4 Abstract class are completely interoperable with Java code.
do not contain any implementation code.	
#5Traits are stackable.                                  #5 Abstract class is not stackable. So, super calls are statically bound.
So, super calls are dynamically bound.	

"""

#################
Abstract class:

// Scala program to illustrate how to  
// create an abstract class 
  
// Abstract class 
abstract class Abstclass 
{ 
      
    // Abstract and non-abstract method 
    def portal 
    def tutorial() 
    {  
        println("Scala tutorial") 
    } 
  
} 
  
// GFG class extends abstract class 
class GFG extends Abstclass 
{ 
    def portal() 
    { 
        println("Welcome!! GeeksforGeeks") 
    } 
} 
  
object Main  
{ 
      
    // Main method 
    def main(args: Array[String])  
    { 
        // object of GFG class 
        var obj = new GFG (); 
        obj.tutorial() 
        obj.portal() 
    } 
} 
Output:

Scala tutorial
Welcome!! GeeksforGeeks
###################

#Trait:

// Scala program to illustrate how to  
// create traits 
  
// traits 
trait mytrait 
{ 
      
    // Abstract and non-abstract method 
    def portal 
    def tutorial() 
    {  
        println("Scala tutorial") 
    } 
  
} 
  
// GFG class extends trait 
class GFG extends mytrait 
{ 
    def portal() 
    { 
        println("Welcome!! GeeksforGeeks") 
    } 
} 
  
object Main  
{ 
      
    // Main method 
    def main(args: Array[String])  
    { 
          
        // object of GFG class 
        var obj = new GFG (); 
        obj.tutorial() 
        obj.portal() 
    } 
} 
Output:

Scala tutorial
Welcome!! GeeksforGeeks

