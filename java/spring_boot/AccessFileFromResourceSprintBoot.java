
/*

This methods loads XSD file from resource/scripts/xml_process/schema_update_01115.xsd and xml file from file system and validates
the xml file as per schema in xsd file
*/

 @Autowired ResourceLoader resourceLoader;

// we get access file contents as input stream or URL , but not as java.io.File in sprintboot
Resource resource =
          resourceLoader.getResource(
              "classpath:scripts/xml_process/schema_updated_0115.xsd");
      System.out.println("resource " + resource.getFilename());    
      resource.getURL()
      File xmlFile = new File(xmlFilePathLocal);
      SchemaFactory factory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
      Schema schema = factory.newSchema(resource.getURL());
      System.out.println("schema" + schema);
      //Schema schema = factory.newSchema(xsdFile);
      Validator validator = schema.newValidator();
      validator.validate(new StreamSource(xmlFile));
