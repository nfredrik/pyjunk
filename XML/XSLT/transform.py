from  lxml import etree

xslt_root = etree.XML('''\
 <xsl:stylesheet version="1.0"
     xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
     <xsl:template match="/">
         <foo><xsl:value-of select="/a/b/text()" /></foo>
     </xsl:template>
 </xsl:stylesheet>''')
transform = etree.XSLT(xslt_root)

source= '<a><b>Text</b></a>'
root = etree.XML(source)
result = transform(root)

print 'source:', source
print 'resulted in:', str(result) 
