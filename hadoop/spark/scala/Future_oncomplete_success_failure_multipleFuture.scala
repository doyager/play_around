- Future sequence
- Future traverse
- Future - on complete
- Fututre - Success and failure
- Multiple Futures



Future sequence

http://allaboutscala.com/tutorials/chapter-9-beginner-tutorial-using-scala-futures/#future-sequence

In this section, we will show how to fire a bunch of future operations and
wait for their results by using the Future.sequence() function. As noted in the Scala API documentation, 
the sequence function is useful when you have to reduce a number of futures into a single future.
Moreover, these futures will be non-blocking and run in parallel which also imply that the order of the 
futures is not guaranteed as they can be interleaved.

Future traverse

The Future.traverse() function is fairly similar to the Future.sequence() function. As per the Scala API documentation, the traverse function also allows you to fire a bunch of future operations in parallel and wait for their results.
The traverse function, though, has the added benefit of allowing you to apply a function over the future operations.



######future - on complete 
# https://alvinalexander.com/scala/concurrency-with-scala-futures-tutorials-examples
import scala.concurrent.{Future}
import scala.concurrent.ExecutionContext.Implicits.global
import scala.util.{Failure, Success}
import scala.util.Random

object Example1 extends App {
    println("starting calculation ...")
    val f = Future {
        sleep(Random.nextInt(500))
        42
    }
    println("before onComplete")
    f.onComplete {
        case Success(value) => println(s"Got the callback, meaning = $value")
        case Failure(e) => e.printStackTrace
    }
    // do the rest of your work
    println("A ..."); sleep(100)
    println("B ..."); sleep(100)
    println("C ..."); sleep(100)
    println("D ..."); sleep(100)
    println("E ..."); sleep(100)
    println("F ..."); sleep(100)
    sleep(2000)
}

o/p:

starting calculation ...
before onComplete
A ...
B ...
C ...
D ...
E ...
Got the callback, meaning = 42
F ...

/*
This example is similar to the previous example, though it just returns the number 42 after a random delay. 
The important part of this example is the f.onComplete method call and the code that follows it. Here’s how that code works:

The f.onComplete method call sets up the callback. Whenever the Future completes,
it makes a callback to onComplete, at which time that code will be executed.
The Future will either return the desired result (42), or an exception.
The println statements with the slight delays represent other work your code can do while the Future is off and running.
Because the Future is off running concurrently somewhere, and you don’t know exactly when the result will be computed, the output from this code is nondeterministic, but it can look like this:

starting calculation ...
before onComplete
A ...
B ...
C ...
D ...
E ...
Got the callback, meaning = 42
F ...
Because the Future returns eventually, at some nondeterministic time, the “Got the callback” message may appear anywhere in that output.
*/



######### Fututre - Success and failure

/*
https://alvinalexander.com/scala/concurrency-with-scala-futures-tutorials-examples

This code is similar to the previous example, but this Future is wired to throw an exception about half the time, and the onSuccess and onFailure blocks are defined as partial functions; 
they only need to handle their expected conditions.
*/

import scala.concurrent.{Future}
import scala.concurrent.ExecutionContext.Implicits.global
import scala.util.{Failure, Success}
import scala.util.Random

object OnSuccessAndFailure extends App {
    val f = Future {
        sleep(Random.nextInt(500))
        if (Random.nextInt(500) > 250) throw new Exception("Yikes!") else 42
    }
    f onSuccess {
        case result => println(s"Success: $result")
    }
    f onFailure {
        case t => println(s"Exception: ${t.getMessage}")
    }

    // do the rest of your work
    println("A ..."); sleep(100)
    println("B ..."); sleep(100)
    println("C ..."); sleep(100)
    println("D ..."); sleep(100)
    println("E ..."); sleep(100)
    println("F ..."); sleep(100)
    sleep(2000)
}




########## multiple Futures

/*

https://alvinalexander.com/scala/concurrency-with-scala-futures-tutorials-examples

How to use multiple Futures in a for loop
The examples so far have shown how to run one computation in parallel, to keep things simple. You may occasionally do something like this, such as writing data to a database without blocking the web server, but many times you’ll want to run several operations concurrently, wait for them all to complete, and then do something with their combined results.

For example, in a stock market application I wrote, I run all of my web service queries in parallel, wait for their results, and then display a web page. This is faster than running them sequentially.

The following example is a little simpler than that, but it shows how to call an algorithm that may be running in the cloud. It makes three calls to Cloud.runAlgorithm, which is defined elsewhere to return a Future[Int]. For the moment, this algorithm isn’t important, other than to know that it prints its result right before returning it.

The code starts those three futures running, then joins them back together in the for-comprehension:


Here’s a brief description of how this code works:

The three calls to Cloud.runAlgorithm create the result1, result2, and result3 variables, which are of type Future[Int].
When those lines are executed, those futures begin running, just like the web service calls in my stock market application.
The for-comprehension is used as a way to join the results back together. When all three futures return, their Int values are assigned to the variables r1, r2, and r3, and the sum of those three values is returned from the yield expression, and assigned to the result variable.
Notice that result can’t just be printed after the for-comprehension. That’s because the for-comprehension returns a new Future, so result has the type Future[Int]. (This makes sense in more complicated examples.) Therefore, the correct way to print the example is with the onSuccess method call, as shown.
When this code is run, the output is nondeterministic, but looks something like this:

*/


import scala.concurrent.{Future, future}
import scala.concurrent.ExecutionContext.Implicits.global
import scala.util.{Failure, Success}
import scala.util.Random

object RunningMultipleCalcs extends App {
    println("starting futures")
    val result1 = Cloud.runAlgorithm(10)
    val result2 = Cloud.runAlgorithm(20)
    val result3 = Cloud.runAlgorithm(30)

    println("before for-comprehension")
    val result = for {
        r1 <- result1
        r2 <- result2
        r3 <- result3
    } yield (r1 + r2 + r3)

    println("before onSuccess")
    result onSuccess {
        case result => println(s"total = $result")
    }

    println("before sleep at the end")
    sleep(2000)  // important: keep the jvm alive
}


object Cloud {
    def runAlgorithm(i: Int): Future[Int] = future {
        sleep(Random.nextInt(500))
        val result = i + 10
        println(s"returning result from cloud: $result")
        result
    }
}

o/p:

starting futures
before for-comprehension
before onSuccess
before sleep at end
returning result from cloud: 30
returning result from cloud: 20
returning result from cloud: 40
total = 90


#########################



