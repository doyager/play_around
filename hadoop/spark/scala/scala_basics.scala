#sum list 
val l = List(1, 3, 5, 11, -1, -3, -5)
l.foldLeft(0)(_ + _) // same as l.foldLeft(0)((a,b) => a + b)


#list of list

scala> val lol = List(List(1,2), List(3,4))
lol: List[List[Int]] = List(List(1, 2), List(3, 4))

val result = lol.flatten
result: List[Int] = List(1, 2, 3, 4)



#List

/ List of Strings
val fruit: List[String] = List("apples", "oranges", "pears")

// List of Integers
val nums: List[Int] = List(1, 2, 3, 4)

// Empty List.
val empty: List[Nothing] = List()

// Two dimensional list
val dim: List[List[Int]] =
   List(
      List(1, 0, 0),
      List(0, 1, 0),
      List(0, 0, 1)
   )
   
   
