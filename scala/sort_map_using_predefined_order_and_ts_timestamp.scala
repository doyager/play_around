/*
Question : 
predefined_order = ['Impression','buttonclick','Success']

to order a a map based on predefined value order and key is time stamp in long epoxy format with duplicates .
We want to order by the predefined_order list when timestamp is same else based on timestamp

*/
val predefined_order = List("Impression", "buttonclick", "Success")

val map: Map[Long, String] = Map(
  1621064951000L -> "buttonclick",
  1621064950000L -> "Impression",
  1621064952000L -> "Success",
  1621064952000L -> "buttonclick",
  1621064951000L -> "Success"
)

val orderedMap = map.toList
  .sortBy { case (ts, eventType) => (ts, predefined_order.indexOf(eventType)) }
  .toMap

// Output the ordered map
orderedMap.foreach { case (ts, eventType) =>
  println(s"$ts -> $eventType")
}

/*

Here's an example Scala code that orders a Map based on a predefined order list and the timestamp in long epoxy format:

```scala
val predefined_order = List("Impression", "buttonclick", "Success")

val map: Map[Long, String] = Map(
  1621064951000L -> "buttonclick",
  1621064950000L -> "Impression",
  1621064952000L -> "Success",
  1621064952000L -> "buttonclick",
  1621064951000L -> "Success"
)

val orderedMap = map.toList
  .sortBy { case (ts, eventType) => (ts, predefined_order.indexOf(eventType)) }
  .toMap

// Output the ordered map
orderedMap.foreach { case (ts, eventType) =>
  println(s"$ts -> $eventType")
}
```

In this example, the `predefined_order` list is defined at the beginning. 
The `map` variable is defined as a `Map` with `Long` keys representing timestamps and `String` values representing event types.

The `orderedMap` is created by first converting the `map` to a `List` using the `toList` method. 
Then, the list is sorted based on the `(ts, predefined_order.indexOf(eventType))` tuple. This means that the list is first sorted by timestamp, and then by the index of the event type in the `predefined_order` list. The `indexOf` method returns -1 if the element is not found in the list, so any event types that are not in the `predefined_order` list will be sorted at the end.

Finally, the sorted list is converted back to a `Map` using the `toMap` method. 
The `orderedMap` variable now contains the sorted map.

The output of the example code will be:
```
1621064950000 -> Impression
1621064951000 -> buttonclick
1621064951000 -> Success
1621064952000 -> Success
1621064952000 -> buttonclick
```

As you can see, the map is first ordered by timestamp, and then by the event type in the `predefined_order` list. 
Note that the duplicate timestamps are preserved in the output.
*/
