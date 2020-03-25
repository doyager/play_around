

public class Test {

  public static void main(String[] args) {
    // TODO Auto-generated method stub


    String obj = "TRUE";  //  if obj="true" o/p : true. , if obj="" then o/p is false
    //null test

    Boolean xmlFlag = Optional.ofNullable(obj).map(o -> Boolean.valueOf(obj)).orElse(false);

    if(xmlFlag)
    {
      System.out.println("true");
    }else{
      System.out.println("false");
    }
    }}
