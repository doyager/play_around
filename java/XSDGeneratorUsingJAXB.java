

//1.
//Domain Model (Root)

Below is a simple Java model. Note how the bar property has required=true and the foo property does not.

import javax.xml.bind.annotation.*;

@XmlRootElement
@XmlAccessorType(XmlAccessType.FIELD)
public class Root {

    @XmlElement
    private String foo;

    @XmlElement(required=true)
    private String bar;

    @XmlElement(nillable=true)
    private String baz;

}

//2.
//Demo Code

//Below is some code that demonstrates how to generate an XML schema using the JAXBContext.

import java.io.IOException;
import javax.xml.bind.*;
import javax.xml.transform.Result;
import javax.xml.transform.stream.StreamResult;

public class GenerateSchema {

    public static void main(String[] args) throws Exception {
        JAXBContext jc = JAXBContext.newInstance(Root.class);

        jc.generateSchema(new SchemaOutputResolver() {
            @Override
            public Result createOutput(String namespaceUri,
                    String suggestedFileName) throws IOException {
                StreamResult result = new StreamResult(System.out);
                result.setSystemId(suggestedFileName);
                return result;
            }
        });
    }

}

//3.
//Generated XML Schema
//Below is the resulting XML schema note how the XML element corresponding to the foo field has minOccurs="0" while the XML element corresponding to the bar field (which was annotated with @XmlElement(required=true) does not. This is because the default minOccurs is 1 meaning it's required.

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<xs:schema version="1.0" xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="root" type="root"/>
  <xs:complexType name="root">
    <xs:sequence>
      <xs:element name="foo" type="xs:string" minOccurs="0"/>
      <xs:element name="bar" type="xs:string"/>
      <xs:element name="baz" type="xs:string" nillable="true" minOccurs="0"/>
    </xs:sequence>
  </xs:complexType>
</xs:schema>
