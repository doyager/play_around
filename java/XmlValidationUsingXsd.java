
package com.company.tests;

import javax.xml.XMLConstants;
import javax.xml.transform.stream.StreamSource;
import javax.xml.validation.Schema;
import javax.xml.validation.SchemaFactory;
import javax.xml.validation.Validator;

import org.xml.sax.SAXException;

import java.io.File;
import java.io.IOException;

public class Test {

  public static void main(String[] args) throws  Exception {
    // TODO Auto-generated method stub

    Test test =new Test();
    test.xsdValidationTest();
   
  }

  public void xsdValidationTest() throws Exception{

    try {
      System.out.println("Validation started");

      String xsdPath="scripts/xml_process/IntegratedCrossChannel_schema.xsd"; //src/main/resources/ integrity-engine-command-center-agent/src/main/resources/
      String xmlPath="scripts/xml_process/IntegratedCrossChannel_012345_dummyVals.xml"; //src/main/resources/

      ClassLoader classLoader = ClassLoader.getSystemClassLoader(); //this.getClass().getClassLoader();
      // Getting resource(File) from class loader
      File xsdFile=new File(classLoader.getResource(xsdPath).getFile());
      File xmlFile = new File(classLoader.getResource(xmlPath).getFile());


      SchemaFactory factory =
              SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
      Schema schema = factory.newSchema(xsdFile);//new File(xsdPath));
      Validator validator = schema.newValidator();
      validator.validate(new StreamSource(xmlFile)); //new File(xmlPath)));
      System.out.println("Validation Successful");

      /*
      Srping boot
      File file = ResourceUtils.getFile("classpath:config/sample.txt")

      //File is found
      System.out.println("File Found : " + file.exists());

      //Read File Content
      String content = new String(Files.readAllBytes(file.toPath()));
      System.out.println(content);
      * */
    } catch (IOException | SAXException e) {
      System.out.println("Exception: "+e.getMessage());
      e.printStackTrace();
     // return false;
    }
    //return true;
  }
  }
