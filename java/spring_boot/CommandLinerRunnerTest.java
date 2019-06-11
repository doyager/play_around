
package com.anthem.integrityengine.agent.config;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

import org.springframework.boot.CommandLineRunner;

import org.springframework.stereotype.Component;

/*

To quickly test some functionality part of spring boot application use commandlinerunner ,

-Put this class under com.anthem.integrityengine.agent.config
-mvn clean , install
-then start agent application [Which had "@SpringBootApplication"], command liner runner will be called
and main method in that will be executed.

o/p:

*************************Commnad line runner called...
 Shell Process Command : /Users/mac/test_area/dummy_script.sh portal dry-test
Tue Jun 11 10:18:58 EDT 2019
Hello World !!
Hello World after sleep !!
Tue Jun 11 10:19:19 EDT 2019
 Shell Process Command :SUCCESS !!
 Shell Process Command :Completed !!

*/


@Component
public class CommandLinerRunnerTest implements CommandLineRunner {

  @Override
  public void run(String... args) throws Exception {
    System.out.println("*************************Commnad line runner called...");

    String returnStr = "dummy-str";
    List<String> returnList = new ArrayList<String>();

    String projectDir = "/Users/mac/test_area";
    String mainScript = "dummy_script.sh";
    String shellType = "sh";
    String arg1 = "portal";
    String arg2 = "dry-test";
    String all_args = arg1 + " " + arg2;

    String script = projectDir + "/" + mainScript;
    String cmd = script + " " + all_args;

    try {
      System.out.println(" Shell Process Command : " + cmd);
      Process p;

      List<String> cmdList = new ArrayList<String>();
      // adding command and args to the list
      cmdList.add(shellType);
      cmdList.add(script);
      cmdList.add(arg1);
      cmdList.add(arg2);
      ProcessBuilder pb = new ProcessBuilder(cmdList);
      p = pb.start();

      p.waitFor();
      BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
      String line;
      while ((line = reader.readLine()) != null) {
        System.out.println(line);
      }

      if ((p.exitValue()) == 0) {

    	  System.out.println(" Shell Process Command :SUCCESS !! ");
        returnStr = "SUCCESS";

      } else {
    	  System.out.println(" Shell Process Command :FAILURE !! ");
        returnStr = "FAILURE";

        throw new Exception("ERROR :  Shell Process Failed ");
      }
      System.out.println(" Shell Process Command :Completed !! ");
    } catch (IOException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    } catch (InterruptedException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }
  }
}
