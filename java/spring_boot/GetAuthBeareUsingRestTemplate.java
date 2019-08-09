
package com.company.agent.ci.repository;

import java.util.List;
import java.util.Map;

import org.apache.http.client.methods.HttpPost;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Repository;
import org.springframework.web.client.RestTemplate;

import java.io.IOException;
import java.net.MalformedURLException;
import org.json.JSONArray;


import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

@Repository
public class AuthRepository {


/*

********** Inside Success responseEntity.getBody {"token":"eyJhbGciOiJIUzUxMiJ9.eyJmaXJzdE5hbWUiOiJTcmluYX
I1MSwiaWF0IjoxNTY1Mzc1MzUxLCJlbWFpbCI6InNyaW5heWGVtLnJlYWQiLCJjb25jZXB0cy53cml0ZSIsImxpYnJhcnkud3JpdG
UiLCJyb2xlcy5yZWFkIiwidXNlcnMud3JpdGUiLCJ3b3JraXRlbS53cml0ZSIsImxpYnJhcnkucmVhZldWVwcm9jZXNzaW1wcm92Z
W1lbnQud3CJjYXRhbG9nLndyaXRlIiwicS5jYWxsSW5
LnJlYWQiLCJjYXRhbG9nLnJlYWQiLCJxLnJ4Y2xhaW1zLndyaXRlIiwicHJvZHVjdHMud3JpdGUiLCJxLmNjcXVldWVvdXRib3VuZGNhb","success":true}
*/
@Autowired
	private RestTemplate restTemplate;

	public String getAuthToken() {

		String requestUrl = "http:///company-server.company.com:8080/portal-api/login";

		// curl -X POST "http://company-server.company.com:8080/portal-api/login"
		// -H "accept: */*" -H "Content-Type: application/json" -d "{ \"password\":
		// \"password123\", \"username\": \"username\"}"

		// URL serverUrl;
		String returnAuth = null;
		try {

			//String username = "username";
			//String password = "password123";
			HttpPost httpRequest = new HttpPost(requestUrl);
			httpRequest.setHeader("Content-Type", "application/json");
			httpRequest.setHeader("accept", "*/*");

			// setting up the request headers
			HttpHeaders requestHeaders = new HttpHeaders();
			requestHeaders.setContentType(MediaType.APPLICATION_JSON);

			String body = "{\"password\": \"" + password + "\", \"username\": \"" + username + "\"}";

			HttpEntity<String> payloadRequest = new HttpEntity<>(body, requestHeaders);
			ResponseEntity<String> responseEntity = restTemplate.exchange(requestUrl, HttpMethod.POST, payloadRequest,
					String.class);

			//System.out.println("********** responseEntity.getBody " + responseEntity.getBody());
			if (responseEntity.getStatusCode().is2xxSuccessful()) {

				logger.info("submitRequest: get Auth Token returned response sucess");
				System.out.println("********** Inside Success responseEntity.getBody " + responseEntity.getBody());
				String returnAuth = responseEntity.getBody();		
				
				//Json parsing
			      JSONObject obj = new JSONObject(returnAuth);
			      String token =  obj.getString("token"); 

			      System.out.println("**********  Token : " +token);
				
				 Map<String, String> map = objectMapper.readValue(returnAuth, new TypeReference<Map<String, String>>(){});
      
     				 System.out.println("**********  Map Token : " + map.get("token"));
			} else if (responseEntity.getStatusCode().isError()) {

				logger.info("submitRequest:  get Auth Token returned response error...returning empty result set");
			}

			return returnAuth;

		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		return returnAuth;
	}
