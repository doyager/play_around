#map vs flat map
Quite a difference, right? Because of the way flatMap works, 
it flattens the resulting list of strings into a sequence of characters (Seq[Char]). 
I like to think of flatMap as a combination of map followed by flatten, so it first

Tip: I often refer to flatMap as mapFlat so I can remember how it works.

scala> val fruits = Seq("apple", "banana", "orange")
fruits: Seq[java.lang.String] = List(apple, banana, orange)

scala> fruits.map(_.toUpperCase)
res0: Seq[java.lang.String] = List(APPLE, BANANA, ORANGE)

scala> fruits.flatMap(_.toUpperCase)
res1: Seq[Char] = List(A, P, P, L, E, B, A, N, A, N, A, O, R, A, N, G, E)


(or)

scala> val mapResult = fruits.map(_.toUpperCase)
mapResult: Seq[String] = List(APPLE, BANANA, ORANGE)

scala> val flattenResult = mapResult.flatten
flattenResult: Seq[Char] = List(A, P, P, L, E, B, A, N, A, N, A, O, R, A, N, G, E)


# examnple flatMap and sum

scala> val strings = Seq("1", "2", "foo", "3", "bar")
strings: Seq[java.lang.String] = List(1, 2, foo, 3, bar)

scala> strings.map(toInt)
res0: Seq[Option[Int]] = List(Some(1), Some(2), None, Some(3), None)

scala> strings.flatMap(toInt)
res1: Seq[Int] = List(1, 2, 3)

scala> strings.flatMap(toInt).sum
res2: Int = 6


#sum list 
val l = List(1, 3, 5, 11, -1, -3, -5)
l.foldLeft(0)(_ + _) // same as l.foldLeft(0)((a,b) => a + b)


#list of list

scala> val lol = List(List(1,2), List(3,4))
lol: List[List[Int]] = List(List(1, 2), List(3, 4))

val result = lol.flatten
result: List[Int] = List(1, 2, 3, 4)

(or)
List(List(1,2), List(3,4)).flatten
> List(1,2,3,4)


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


# fold vs foldleft vs foldright

The primary difference is the order in which the fold operation iterates through the collection in question. 
foldLeft starts on the left side—the first item—and iterates to the right; foldRight starts on the right side—the last
item—and iterates to the left. fold goes in no particular order.

val numbers = List(5, 4, 8, 6, 2)
numbers.fold(0) { (z, i) =>
  a + i
}
// result = 25


val l = List(1, 3, 5, 11, -1, -3, -5)
l.foldLeft(0)(_ + _) // same as l.foldLeft(0)((a,b) => a + b)


In essence, fold takes data in one format and gives it back to you in another. All three methods—fold, foldLeft, and foldRight—do the same thing, but just a little differently. I will first explain the concept all three share and then explain their differences.

By the way, if you are coming from Ruby, like me, this is the same idea as inject. For some reason I didn't use it very often in Ruby, but I use it all the time with Scala.

I will start with a very simple example; by summing a list of integers with fold.

val numbers = List(5, 4, 8, 6, 2)
numbers.fold(0) { (z, i) =>
  a + i
}
// result = 25
The fold method for a List takes two arguments; the start value and a function. This function also takes two arguments; the accumulated value and the current item in the list. So here's what happens:

At the start of execution, the start value that you passed as the first argument is given to your function as its first argument. As the function's second argument it is given the first item on the list (in the case of fold this may or may not be the actual first item on your list as you will read about below).

The function is then applied to its two arguments, in this case a simple addition, and returns the result.
Fold then gives the function the previous return value as its first argument and the next item in the list as its second argument, and applies it, returning the result.
This process repeats for each item of the list and returns the return value of the function once all items in the list have been iterated over.
This is a trivial example though. Let's take a look at something that is more useful. I will use foldLeft in this next example and will explain how it is different from fold later. For now, think of it in the same way as fold.
Here is our class and companion object we will be working with.

class Foo(val name: String, val age: Int, val sex: Symbol)

object Foo {
  def apply(name: String, age: Int, sex: Symbol) = new Foo(name, age, sex)
}
Let's say we have a list of Foo instances.

val fooList = Foo("Hugh Jass", 25, 'male) ::
              Foo("Biggus Dickus", 43, 'male) ::
              Foo("Incontinentia Buttocks", 37, 'female) ::
              Nil
And we want to turn it into a list of strings in the format of [title] [name], [age]

--------------foldleft exampel
val stringList = fooList.foldLeft(List[String]()) { (z, f) =>
  val title = f.sex match {
    case 'male => "Mr."
    case 'female => "Ms."
  }
  z :+ s"$title ${f.name}, ${f.age}"
}

// stringList(0)
// Mr. Hugh Jass, 25

// stringList(2)
// Ms. Incontinentia Buttocks, 37

Like the first example, we have a beginning—this case and empty List of Strings—and the operation function. 
In this example we determine which title is appropriate for the current item, construct the string we want,
and append it to the end of the accumulator (which is a list).

Now, the difference between fold, foldLeft, and foldRight.
The primary difference is the order in which the fold operation iterates through the collection in question. 
foldLeft starts on the left side—the first item—and iterates to the right; foldRight starts on the right side—the 
last item—and iterates to the left. fold goes in no particular order.

Because fold does not go in any particular order, there are constraints on the start value and thus return 
value (in all three folds the type of the start value must be the same as the return value).

The first constraint is that the start value must be a supertype of the object you're folding. 
In our first example we were folding on a type List[Int] and had a start type of Int. Int is a supertype of List[Int].

The second constraint of fold is that the start value must be neutral, i.e. it must not change the result. 
For example, the neutral value for an addition operation would be 0, 1 for multiplication, Nil lists, etc.

Those are the basics!
   
   
