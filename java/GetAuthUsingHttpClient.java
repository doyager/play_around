package com.company.agent.ci.repository;

import java.io.IOException;
import java.io.UnsupportedEncodingException;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.ParseException;
import org.apache.http.client.CookieStore;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.BasicCookieStore;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;

public class GetAuthUsingHttpClient {

/*

method to get auth token by making an calling to the rest service using username and password 

output :
************************* returnAuth : {"token":"eyJhbGciOiJIUzUxMuYXlhbiIsImxhc3ROYW1lIjoiTWFjaGF
ybGEgU3JpIiwic3ViIjoiQUcwMzgxMiIsInBob25lIjoiKiIsImV4cCI6MTU2NTM3Mjk5MSwiaWF0IjoxNTY1
lcnMud3JpdGUiLCJ3b3JraXRlbS53cml0ZSIsImxpYnJhcnkucmVhZCIsInByb2R1Y3RzLnJlYWQiLCJxLmNjQmx1ZVBsYW4ud3J
JyYXJ5LmV4ZWN1dGUiLCJxLmNjcXVldWVwcm9jZXNzaW1wcm92ZW1lbnQud3JpdGUiLCJjbGFpbS53cml0ZSIsImxpYnJh
cnkuY29uZmlnIiwicS5zZW50aW1lbnQud3JpdGUiLCJxLmNsYWltcy53cml0ZSIsInVzZXJzLnJlYWQiLCJ
50ZXJ2ZW50aW9uLnF1ZXVlLjIud3J","success":true}


*/
  public static void main(String[] args) {
    // TODO Auto-generated method stub

    try {
      // Create HTTPClient - Used to make Request to API
      HttpClient httpClient = null;
      CookieStore httpCookieStore = new BasicCookieStore();
      HttpClientBuilder builder = HttpClientBuilder.create().setDefaultCookieStore(httpCookieStore);
      httpClient = builder.build();

      String requestUrl = "http://comapny-server.companyname.com:8080/portal-api/login";
      String username = "employeeId";
      String password = "password";
      String returnAuth = null;

      HttpPost httpRequest = new HttpPost(requestUrl);
      httpRequest.setHeader("Content-Type", "application/json");
      httpRequest.setHeader("accept", "*/*");
      StringEntity body;

      body =
          new StringEntity(
              "{\"password\": \"" + password + "\",\"username\": \"" + username + "\"}");

      httpRequest.setEntity(body);

      HttpResponse response = httpClient.execute(httpRequest);

      HttpEntity entity = response.getEntity();
      returnAuth = EntityUtils.toString(entity);
      System.out.println("********** returnAuth : " + returnAuth);
    } catch (UnsupportedEncodingException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    } catch (ParseException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    } catch (IOException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }
  }
}




/*
output 
************************* returnAuth : {"token":"eyJhbGciOiJIUzUxMuYXlhbiIsImxhc3ROYW1lIjoiTWFjaGF
ybGEgU3JpIiwic3ViIjoiQUcwMzgxMiIsInBob25lIjoiKiIsImV4cCI6MTU2NTM3Mjk5MSwiaWF0IjoxNTY1
lcnMud3JpdGUiLCJ3b3JraXRlbS53cml0ZSIsImxpYnJhcnkucmVhZCIsInByb2R1Y3RzLnJlYWQiLCJxLmNjQmx1ZVBsYW4ud3J
JyYXJ5LmV4ZWN1dGUiLCJxLmNjcXVldWVwcm9jZXNzaW1wcm92ZW1lbnQud3JpdGUiLCJjbGFpbS53cml0ZSIsImxpYnJh
cnkuY29uZmlnIiwicS5zZW50aW1lbnQud3JpdGUiLCJxLmNsYWltcy53cml0ZSIsInVzZXJzLnJlYWQiLCJ
50ZXJ2ZW50aW9uLnF1ZXVlLjIud3J","success":true}

*/
