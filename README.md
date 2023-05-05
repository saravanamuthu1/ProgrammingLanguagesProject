# ProgrammingLanguagesProject
This code defines a Python module for parsing and transforming XML files using the lxml library and Lark parser. It includes a grammar for the XML format, a Node class for building a tree structure from the parsed XML, and functions for reading XML files, transforming them using XSLT, and printing the resulting strings.

The module begins by importing necessary classes from the lxml and Lark libraries. It then defines a grammar for the XML format using Lark syntax. The grammar includes rules for parsing elements, attributes, and text nodes, and ignoring whitespace.

Next, the Node class is defined. It represents a node in the XML tree and includes methods for adding child nodes and printing the tree in a readable format.

The module also includes a function for reading an XML file and building an XML tree using the Lark parser. The function takes a file name as input, reads the file, parses the XML string into a Lark Tree object, and builds a Node object from the tree. The resulting Node object represents the root-level node of the XML tree.

Finally, the module includes a function for transforming an XML document using XSLT. The function takes an XML string and XSLT file name as input, parses the XSLT file and XML string into lxml objects, applies the XSLT transformation to the XML document using the lxml XSLT class, and returns the transformed result as a string.
