



package com.company;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Test {

    public static void main(String[] args)
    {

        List<String> list = new ArrayList<String>();
//add some stuff
        list.add("android");
        list.add("apple");
        String[] stringArray = list.toArray(new String[0]);

        System.out.println("Arr : "+stringArray.toString());
        //Arr : [Ljava.lang.String;@484b61fc
        System.out.println(Arrays.toString(list.toArray()));
        //o/p:[android, apple]
        
        
        // Join 
          List<Integer> intList = Arrays.asList(1, 2, 3);
           System.out.println(StringUtils.join(intList, "|"));
           // o/p: 1|2|3
    }
    
    public static String buildCommaSeperatedNumStringFromIntList(List<Integer> intList) {

		StringBuilder strBuilder = new StringBuilder("");
		if (!CollectionUtils.isEmpty(intList)) {

			for (Integer i : intList) {
				strBuilder.append(i).append(",");
			}
		}
		return strBuilder.length() > 2 ? strBuilder.substring(0, strBuilder.length() - 1) : strBuilder.toString();

	}
	
	public static String buildCommaSeperatedStringWithQuotesFromList(List<String> stringList) {

		StringBuilder strBuilder = new StringBuilder("");
		if (!CollectionUtils.isEmpty(stringList)) {

			for (String str : stringList) {
				strBuilder.append("'" + str.replace(",", "','") + "'").append(",");
			}
		}
		return strBuilder.length() > 2 ? strBuilder.substring(0, strBuilder.length() - 1) : strBuilder.toString();

	}
}
