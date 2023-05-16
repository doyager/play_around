import scala.collection.mutable.{HashMap, Set, MultiMap}

val myMap = new HashMap[String, Set[String]] with MultiMap[String, String]

myMap.addBinding("1", "bar")
myMap.addBinding("2", "foo")
myMap.addBinding("2", "bar")
myMap.addBinding("3", "baz")
myMap.addBinding("1", "foo")
myMap.addBinding("1", "baz")

println(myMap)

val predefined_order = List("foo", "bar", "baz")

val sortedValues: List[List[String]] = myMap.toList
  .sortBy(_._1)
  .map { case (_, values) =>
    values.toList.sorted(Ordering.by(predefined_order.indexOf))
  }
  .toList

print(sortedValues.flatten)

/*
o/p:
HashMap(1 -> HashSet(bar, foo, baz), 2 -> HashSet(bar, foo), 3 -> HashSet(baz))
List(foo, bar, baz, foo, bar, baz)
*/
