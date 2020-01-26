

EXTRACTOR OBJECTS
-- https://docs.scala-lang.org/tour/extractor-objects.html
An extractor object is an object with an unapply method. Whereas the apply method is like a constructor 
which takes arguments and creates an object, the unapply takes an object and tries to give back the arguments.
This is most often used in pattern matching and partial functions.

import scala.util.Random

object CustomerID {

  def apply(name: String) = s"$name--${Random.nextLong}"

  def unapply(customerID: String): Option[String] = {
    val stringArray: Array[String] = customerID.split("--")
    if (stringArray.tail.nonEmpty) Some(stringArray.head) else None
  }
}

val customer1ID = CustomerID("Sukyoung")  // Sukyoung--23098234908
customer1ID match {
  case CustomerID(name) => println(name)  // prints Sukyoung
  case _ => println("Could not extract a CustomerID")
}
The apply method creates a CustomerID string from a name. The unapply does the inverse to get the name back. 
When we call CustomerID("Sukyoung"), this is shorthand syntax for calling CustomerID.apply("Sukyoung"). 
When we call case CustomerID(name) => println(name), we’re calling the unapply method with CustomerID.unapply(customer1ID).

Since a value definition can use a pattern to introduce a new variable, an extractor can be used to initialize 
the variable, where the unapply method supplies the value.

val customer2ID = CustomerID("Nico")
val CustomerID(name) = customer2ID
println(name)  // prints Nico
This is equivalent to val name = CustomerID.unapply(customer2ID).get.

val CustomerID(name2) = "--asdfasdfasdf"
If there is no match, a scala.MatchError is thrown:

val CustomerID(name3) = "-asdfasdfasdf"
The return type of an unapply should be chosen as follows:

If it is just a test, return a Boolean. For instance case even().
If it returns a single sub-value of type T, return an Option[T].
If you want to return several sub-values T1,...,Tn, group them in an optional tuple Option[(T1,...,Tn)].
Sometimes, the number of values to extract isn’t fixed and we would like to return an arbitrary number of values, 
depending on the input. For this use case, you can define extractors with an unapplySeq method 
which returns an Option[Seq[T]]. Common examples of these patterns include deconstructing a 
List using case List(x, y, z) => and decomposing a String using a regular expression Regex,
such as case r(name, remainingFields @ _*) =>.





#######################

Tutorial point :



An extractor in Scala is an object that has a method called unapply as one of its members. The purpose of that unapply method is to match a value and take it apart. Often, the extractor object also defines a dual method apply for building values, but this is not required.

Example
Let us take an example of object defines both apply and unapply methods. The apply method has the same meaning as always:
it turns Test into an object that can be applied to arguments in parentheses in the same way a method is applied. 
So you can write Test ("Zara", "gmail.com") to construct the string "Zara@gmail.com".

The unapply method is what turns Test class into an extractor and it reverses the construction process of apply. 
Where apply takes two strings and forms an email address string out of them, unapply takes an email address and 
returns potentially two strings: the user and the domain of the address.

The unapply must also handle the case where the given string is not an email address. That's why unapply returns
an Option-type over pairs of strings. Its result is either Some (user, domain) if the string str is an email 
address with the given user and domain parts, or None, if str is not an email address. Here are some examples as follows.

Syntax
unapply("Zara@gmail.com") equals Some("Zara", "gmail.com")
unapply("Zara Ali") equals None
Following example program shows an extractor object for email addresses.

Example
object Demo {
   def main(args: Array[String]) {
      println ("Apply method : " + apply("Zara", "gmail.com"));
      println ("Unapply method : " + unapply("Zara@gmail.com"));
      println ("Unapply method : " + unapply("Zara Ali"));
   }
   
   // The injection method (optional)
   def apply(user: String, domain: String) = {
      user +"@"+ domain
   }

   // The extraction method (mandatory)
   def unapply(str: String): Option[(String, String)] = {
      val parts = str split "@"
      
      if (parts.length == 2){
         Some(parts(0), parts(1)) 
      } else {
         None
      }
   }
}
Save the above program in Demo.scala. The following commands are used to compile and execute this program.

Command
\>scalac Demo.scala
\>scala Demo
Output
Apply method : Zara@gmail.com
Unapply method : Some((Zara,gmail.com))
Unapply method : None
Pattern Matching with Extractors
When an instance of a class is followed by parentheses with a list of zero or more parameters, the compiler
invokes the apply method on that instance. We can define apply both in objects and in classes.

As mentioned above, the purpose of the unapply method is to extract a specific value we are looking for. 
It does the opposite operation apply does. When comparing an extractor object using the match statement 
the unapply method will be automatically executed.

Try the following example program.

Example
object Demo {
   def main(args: Array[String]) {
      val x = Demo(5)
      println(x)

      x match {
         case Demo(num) => println(x+" is bigger two times than "+num)
         
         //unapply is invoked
         case _ => println("i cannot calculate")
      }
   }
   def apply(x: Int) = x*2
   def unapply(z: Int): Option[Int] = if (z%2==0) Some(z/2) else None
}
Save the above program in Demo.scala. The following commands are used to compile and execute this program.

Command
\>scalac Demo.scala
\>scala Demo
Output
10
10 is bigger two times than 5
