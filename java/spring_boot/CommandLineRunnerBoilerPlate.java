package com.company.agent.cc.config;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

import org.springframework.boot.CommandLineRunner;

import org.springframework.stereotype.Component;




@Component
public class CommandLineRunnerTest implements CommandLineRunner {

  @Override
  public void run(String... args) throws Exception {
    System.out.println("*************************Commnad line runner called...");

   

    try {
     
      System.out.println(" *Commnad line runner :Completed !! ");
    } catch (Exception e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }   }
}
