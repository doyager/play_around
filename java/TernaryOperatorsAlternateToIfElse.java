
//alternative to the Java if/then/else

result = testCondition ? trueValue : falseValue
As described in the Oracle documentation (and with a minor change from me), 
this statement can be read as “If testCondition is true, assign the value of trueValue to result;
otherwise, assign the value of falseValue to result.”

Interested in saying a lot while writing a little? In a single line of code,
the Java ternary operator let's you assign a value to a variable based on a boolean expression 
— either a boolean field, or a statement that evaluates to a boolean result.

At its most basic, the ternary operator, also known as the conditional operator,
can be used as an alternative to the Java if/then/else syntax, but it goes beyond that, 
and can even be used on the right hand side of Java statements.


Simple ternary operator examples
One use of the Java ternary operator is to assign the minimum (or maximum) value of two variables to a third variable, essentially replacing a Math.min(a,b) or Math.max(a,b) method call. Here’s an example that assigns the minimum of two variables, a and b, to a third variable named minVal:

minVal = (a < b) ? a : b;
In this code, if the variable a is less than b, minVal is assigned the value of a; otherwise, 
minVal is assigned the value of b. Note that the parentheses in this example are optional, so you can write that same statement like this:

minVal = a < b ? a : b;
I think the parentheses make the code a little easier to read, but again, they’re optional, 
so use whichever syntax you prefer.

You can take a similar approach to get the absolute value of a number, using code like this:

int absValue = (a < 0) ? -a : a;
General ternary operator syntax
Given those examples, you can probably see that the general syntax of the ternary operator looks like this:

result = testCondition ? trueValue : falseValue
As described in the Oracle documentation (and with a minor change from me), 
this statement can be read as “If testCondition is true, assign the value of trueValue to result;
otherwise, assign the value of falseValue to result.”

Here are two more examples that demonstrate this very clearly. To show that all things don’t have to be ints, here’s an example using a float value:

// result is assigned the value 1.0
float result = true ? 1.0f : 2.0f;

public class JavaTernaryOperatorExamples
{
  /**
   * Examples using the Java ternary operator
   * @author alvin alexander, devdaily.com
   */
  public static void main(String[] args)
  {
    // min value example
    int minVal, a=3, b=2;
    minVal = a < b ? a : b;
    System.out.println("min = " + minVal);
    
    // absolute value example
    a = -10;
    int absValue = (a < 0) ? -a : a;
    System.out.println("abs = " + absValue);

    // result is assigned the value 1.0
    float result = true ? 1.0f : 2.0f;
    System.out.println("float = " + result);
 
    // result is assigned the value "Sorry Dude, it's false"
    String s = false ? "Dude, that was true" : "Sorry Dude, it's false";
    System.out.println(s);
    
    // example using the ternary operator on the rhs, in a string
    int x = 5;
    String out = "There " + (x > 1 ? " are " + x + " cookies" : "is one cookie") + " in the jar.";
    System.out.println(out);

  }
}
