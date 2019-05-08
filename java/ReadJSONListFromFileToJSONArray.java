import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;


/* 

pom :

<dependency>
    <groupId>com.googlecode.json-simple</groupId>
    <artifactId>json-simple</artifactId>
    <version>1.1</version>
</dependency>

input:
// input json list : json-list-file.json

[
	{
		"objid": "124",
		"qualifier": "SUPPRESS",
		"objData": "{\"emp_num\":\"124\",\"age\":\"40\"}",
		"properties": null
	},
  {
		"objid": "125",
		"qualifier": "NON-SUPPRESS",
			"objData": "{\"emp_num\":\"125\",\"age\":\"30\"}",
		"properties": null
	}]





*/
public class ReadJSONList {

	// https://howtodoinjava.com/json/json-simple-read-write-json-examples/
	
	@SuppressWarnings("unchecked")
	public static void main(String[] args) {
		// JSON parser object to parse read file
		JSONParser jsonParser = new JSONParser();

		try // (FileReader reader = new FileReader("employees.json"))
		{

			String file_path = "/user/mac/json-list-file.json";
			//reads json file with list of json
			FileReader reader = new FileReader(file_path);
			// Read JSON file
			Object obj = jsonParser.parse(reader);

			JSONArray employeeList = (JSONArray) obj;
			System.out.println(employeeList);

			//iterating through each json obj in json arr
			for(Object o : employeeList) {
			
				JSONObject employeeObject = (JSONObject) o;
				
				//accewssing each element by name from each json obj
				String qualifier = (String) employeeObject.get("qualifier");
				System.out.println(qualifier);
				
			}
			// Iterate over employee array
			//employeeList.forEach(emp -> parseEmployeeObject((JSONObject) emp));

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (ParseException e) {
			e.printStackTrace();
		}
	}
  }
