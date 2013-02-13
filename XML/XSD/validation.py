
from  lxml import etree
try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

f = StringIO('''\
 <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
 <xsd:element name="a" type="AType"/>
 <xsd:complexType name="AType">
   <xsd:sequence>
     <xsd:element name="b" type="xsd:string" />
   </xsd:sequence>
 </xsd:complexType>
 </xsd:schema>
 ''')

xmlschema_doc = etree.parse(f)
xmlschema = etree.XMLSchema(xmlschema_doc)

valid = StringIO('<a><b></b></a>')
doc = etree.parse(valid)
print 'validating a correct doc'
if xmlschema.validate(doc):
    print 'It went okey'
else:
    print 'It went wrong'

xmlschema.assertValid(doc)

print 'validating a incorrect doc'
invalid = StringIO('<a><c></c></a>')
doc2 = etree.parse(invalid)
if xmlschema.validate(doc2):
    print 'It went okey'
else:
    print 'It went wrong'

xmlschema.assertValid(doc2)
