
https://docs.scala-lang.org/overviews/core/futures.html#promises

Promises
So far we have only considered Future objects created by asynchronous computations started using the future method. However, futures can also be created using promises.

While futures are defined as a type of read-only placeholder object created for a result which doesn’t yet exist, a promise can be thought of as a writable, single-assignment container, which completes a future. That is, a promise can be used to successfully complete a future with a value (by “completing” the promise) using the success method. Conversely, a promise can also be used to complete a future with an exception, by failing the promise, using the failure method.

A promise p completes the future returned by p.future. This future is specific to the promise p. Depending on the implementation, it may be the case that p.future eq p.

Consider the following producer-consumer example, in which one computation produces a value and hands it off to another computation which consumes that value. This passing of the value is done using a promise.

import scala.concurrent.{ Future, Promise }
import scala.concurrent.ExecutionContext.Implicits.global

val p = Promise[T]()
val f = p.future

val producer = Future {
  val r = produceSomething()
  p success r
  continueDoingSomethingUnrelated()
}

val consumer = Future {
  startDoingSomething()
  f foreach { r =>
    doSomethingWithResult()
  }
}
Here, we create a promise and use its future method to obtain the Future that it completes. Then, we begin two asynchronous computations. The first does some computation, resulting in a value r, which is then used to complete the future f, by fulfilling the promise p. The second does some computation, and then reads the result r of the completed future f. Note that the consumer can obtain the result before the producer task is finished executing the continueDoingSomethingUnrelated() method.

As mentioned before, promises have single-assignment semantics. As such, they can be completed only once. Calling success on a promise that has already been completed (or failed) will throw an IllegalStateException.

The following example shows how to fail a promise.

val p = Promise[T]()
val f = p.future

val producer = Future {
  val r = someComputation
  if (isInvalid(r))
    p failure (new IllegalStateException)
  else {
    val q = doSomeMoreComputation(r)
    p success q
  }
}
Here, the producer computes an intermediate result r, and checks whether it’s valid. In the case that it’s invalid, it fails the promise by completing the promise p with an exception. In this case, the associated future f is failed. Otherwise, the producer continues its computation, and finally completes the future f with a valid result, by completing promise p.

Promises can also be completed with a complete method which takes a potential value Try[T]– either a failed result of type Failure[Throwable] or a successful result of type Success[T].

Analogous to success, calling failure and complete on a promise that has already been completed will throw an IllegalStateException.

One nice property of programs written using promises with operations described so far and futures which are composed through monadic operations without side-effects is that these programs are deterministic. Deterministic here means that, given that no exception is thrown in the program, the result of the program (values observed in the futures) will always be the same, regardless of the execution schedule of the parallel program.

In some cases the client may want to complete the promise only if it has not been completed yet (e.g., there are several HTTP requests being executed from several different futures and the client is interested only in the first HTTP response - corresponding to the first future to complete the promise). For these reasons methods tryComplete, trySuccess and tryFailure exist on future. The client should be aware that using these methods results in programs which are not deterministic, but depend on the execution schedule.

The method completeWith completes the promise with another future. After the future is completed, the promise gets completed with the result of that future as well. The following program prints 1:

val f = Future { 1 }
val p = Promise[Int]()

p completeWith f

p.future foreach { x =>
  println(x)
}
When failing a promise with an exception, three subtypes of Throwables are handled specially. If the Throwable used to break the promise is a scala.runtime.NonLocalReturnControl, then the promise is completed with the corresponding value. If the Throwable used to break the promise is an instance of Error, InterruptedException, or scala.util.control.ControlThrowable, the Throwable is wrapped as the cause of a new ExecutionException which, in turn, is failing the promise.

Using promises, the onComplete method of the futures and the future construct you can implement any of the functional composition combinators described earlier. Let’s assume you want to implement a new combinator first which takes two futures f and g and produces a third future which is completed by either f or g (whichever comes first), but only given that it is successful.

Here is an example of how to do it:

def first[T](f: Future[T], g: Future[T]): Future[T] = {
  val p = promise[T]

  f foreach { x =>
    p.trySuccess(x)
  }

  g foreach { x =>
    p.trySuccess(x)
  }

  p.future
}
Note that in this implementation, if neither f nor g succeeds, then first(f, g) never completes (either with a value or with an exception).
