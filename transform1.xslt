<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" indent="yes"/>

  <xsl:template match="/">
    <html>
      <head>
        <title>XML to HTML table</title>
      </head>
      <body>
        <table border="1">
          <tr bgcolor="#9acd32">
            <th>Category</th>
            <th>Quantity</th>
            <th>Price</th>
          </tr>
          <xsl:apply-templates select="Root/Data"/>
        </table>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="Data">
    <xsl:variable name="subtotal" select="Quantity * Price"/>
    <tr>
      <td><xsl:value-of select="Category"/></td>
      <td><xsl:value-of select="Quantity"/></td>
      <td><xsl:value-of select="format-number(Price, '###,##0.00')"/></td>
    </tr>
  </xsl:template>

</xsl:stylesheet>
