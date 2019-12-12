What is a pure function?

A pure function is side-effect free, plus the result does not depend on anything other than its inputs.

For a given input, the only effect of a pure function is the output it produces—there are no other effects.

Think of a pure function as a pipe, with input flowing in and output flowing out, with no leaks in between.

Here’s a function in Scala that takes values and returns their sum.

scala> def add(a:Int,b:Int) = a + b
add: (a: Int, b: Int)Int
The add function caused no side-effects. It did not alter the input values provided, it used another pure function, the + operator, and returned the sum of the values as the result of the call. The add function is a pure function.


When we work with pure functions, there’s no explicit demand on the order in which the functions should be called.

For example, let’s say we have two pure functions: add and multiply, where each of these functions takes in two values and return the sum and the product of the values, respectively. Since these functions are pure, the following two sequence of calls will result in the same outcome:

scala> def add(a:Int,b:Int) = a + b
add: (a: Int, b: Int)Int

scala> def multiply(a:Int,b:Int) = a * b
multiply: (a: Int, b: Int)Int

scala> add(5,8) + multiply(5,8)
res0: Int = 53

scala> multiply(5,8) + add(5,8)
res1: Int = 53
On the other hand, if our computation involves a call to an impure function, we can’t reorder function calls like that. Expressions that use pure functions can be easily rearranged and yield themselves for better optimizations that produce the same result.

Why pure functions??

One of the main principles of Functional Programming is to write our applications so that the core is made of pure functions, while side effects are in a thin external layer.

Benefits of pure functions are:

They’re easier to reason about 
This is because a pure function has no side effects or hidden I/O, you can get an idea of what it does just by looking at its signature.

They’re easier to combine 
 A pure function takes an input, does some computations with it, and returns a result. It does not change the world around it, because of which “output depends only on input,” which makes pure functions easy to combine together into simple solutions.

They’re easier to test 
Pure functions are a lot easier to test than impure functions.  

For example :

scala> def pureFunction(name : String) = s"My name is $name"

pureFunction: (name: String)String

scala> def impureFunction(name : String) = println(s"My name is $name")

impureFunction: (name: String)Unit
In order to test our function pureFunction, 1 line of code is enough: assert(pureFunction(“Shivangi”) == “My name is Shivangi”). On the other side, testing the function impureFunction is a lot more complicated as we need to redirect the standard output and do assertions on it.

They’re easier to debug
Pure functions are easier to debug than their impure functions because the output of a pure function depends only on the function’s input parameters and your algorithm, you don’t need to look outside the function’s scope to debug it.

They’re easier to parallelize
It is easier to write parallel/concurrent applications with Function Programming.

It can be stated that :

“If there is no data dependency between two pure expressions, then their order can be reversed, or they can be performed in parallel and they cannot interfere with one another (in other terms, the evaluation of any pure expression is thread-safe).”

What else Pure Functions are : 

Referentially transparent
Referential transparency says that an expression or a function may safely be replaced by its value. A function f is pure if the expression f(x) is referentially transparent for all referentially transparent values x.

Now let us discuss what Referential transparency is.

It is a property of functions that are independent of temporal context and have no side effects. For a particular input, an invocation of a referentially transparent function can be replaced by its result without changing the program semantics.

For example : input + 3*2 can be replaced by input + 6, since the sub-expression 3 * 2 is referentially transparent.

Why would we care about referential transparency ???

Referential transparency plays a significant role in program optimization. The ability to replace a function or an expression with its value, at compile time, can save quite a few cycles during runtime.

“Referentially transparent” means that the value of the expression can depend only on the values of its parts, and not on any other facts about them.

Idempotent
The word Idempotent has many meanings, but we will focus on what it means in programming.  A function or operation is idempotent if the result or effect of executing it multiple times for a given input is the same as executing it only once for the same input. The function add is pure and it can be executed any number of times. For a given value of a and b, it would produce the same result no matter how many times we call it.

Pure Functions appear to be idempotent and they are. If we call a pure-function once it yields a particular result based on the input. If we call it many more times, with the same input, it would return the same result as the first time.

The benefit of idempotent is that pure functions may be safely retried any number of times or their execution may safely be skipped entirely if we know we don’t need the result after all.

Referential transparency says it’s safe to replace a pure function with its value. Idempotency says it is safe to recompute the function any number of times. These two features combined says that pure functions are easy and safe to play with—they offer the most flexibility for program optimization.

Memoizable
Memoization is an optimization technique. The main goal is to reduce the computational time at the expense of space, that is, by storing or caching the results of computations based on the values of the operands or arguments.

Memoization makes sense only if the result of the function will be the same for a given set of arguments or input. Since pure functions have this property, they’re readily memoizable.

can be lazy
Lazy evaluation is where a program may postpone evaluating an expression until just-in-time when its value is needed. If the value is never needed during the execution of the program, the evaluation of the expression may be totally skipped. In Scala, we can mark some variable bindings as lazy.

The benefit of this is that sometimes we don’t get efficient by running things faster but sometimes we get efficient by eliminating things we otherwise don’t have to execute, so in a way we eliminate computations and by doing so we get really efficient doing it.

Conclusion:

Pure functions are one of the fundamentals of Functional Programming. If a function is pure, you may evaluate it now or safely compute it later. Furthermore, you can save the value of evaluation(by making it lazy) and reuse it since it will have the same result no matter how many times we evaluate it. Also, if a function has no side-effect, the only way anyone will know if the function was evaluated or not is by looking at the result. So, the execution can be safely postponed as desired. They also help in performance optimization due to referential transparency and memoization features.

References :

http://blog.agiledeveloper.com/
http://alvinalexander.com/scala/fp-book/benefits-of-pure-functions
