<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <head>
        <title>Catalog</title>
      </head>
      <body>
        <table>
          <tr>
            <th>Description</th>
            <th>Image</th>
            <th>Gender</th>
            <th>Item Number</th>
            <th>Price</th>
            <th>Sizes</th>
          </tr>
          <xsl:for-each select="//catalog_item">
            <xsl:variable name="product" select="../@description"/>
            <xsl:variable name="image" select="../@product_image"/>
            <xsl:variable name="gender" select="@gender"/>
            <xsl:variable name="item_number" select="item_number"/>
            <xsl:variable name="price" select="price"/>
            <tr>
              <td><xsl:value-of select="$product"/></td>
              <td><img src="{concat('../images/', $image)}"/></td>
              <td><xsl:value-of select="$gender"/></td>
              <td><xsl:value-of select="$item_number"/></td>
              <td><xsl:value-of select="$price"/></td>
              <td>
                <xsl:for-each select="size">
                  <xsl:value-of select="@description"/>:
                  <xsl:for-each select="color_swatch">
                    <xsl:value-of select="."/>
                    <xsl:if test="position() != last()">, </xsl:if>
                  </xsl:for-each>
                  <br/>
                </xsl:for-each>
              </td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
