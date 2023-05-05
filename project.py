# import necessary classes from lxml
from lxml import etree
from lark.tree import Tree
from lark import Lark, Transformer
from lark.visitors import CollapseAmbiguities

# Define the grammar for xml parser
grammar = """
    start: element

    element: "<" NAME attribute* ">" (element | TEXT)* "</" NAME ">"

    attribute: NAME "=" ESCAPED_STRING

    TEXT: /[^\>\<]+/

    NAME: /[a-zA-Z_][a-zA-Z0-9_-]*/

    %import common.ESCAPED_STRING
    %import common.WS
    %ignore WS
"""

# Define the Node class to create a xml nodes
class Node:
    def __init__(self, tag, children=None):
        self.tag = tag
        self.children = children or []

    def __str__(self):
        return self.tag

    def __repr__(self):
        return f"{self.tag}: {self.children}"

    def add_child(self, child):
        self.children.append(child)

    def pretty(self, indent=0):
        result = " " * indent + str(self) + "\n"
        for child in self.children:
            result += child.pretty(indent=indent + 2)
        return result

# Define the xml file reader function
def parse_xml_file(file_name):
    with open(file_name) as f:
        xml = f.read()
        # Create a Lark parser object using the XML grammar
        xml_parser = Lark(grammar)
        # Parse the XML string into a Lark Tree object
        tree = xml_parser.parse(xml)
        # Create a list to hold the root-level nodes of the XML tree
        children = []
        # Iterate over the children of the root-level node
        for child in tree.children:
            # Create a Node object for the child
            node = Node(child.data)
            children.append(node)
            # Iterate over the children of the child node
            for subchild in child.children:
                # If the child is a string, create a Node object with the string as the tag
                if isinstance(subchild, str):
                    node.add_child(Node(subchild.strip()))
                else:
                    node.add_child(node_builder(subchild))

        if tree:
            new_tree = node_builder(Tree(tree.data, children))
        else:
            new_tree = node_builder(Tree("", children))
        return new_tree

# Define a function to apply XSLT transformations to an XML document
def transform_xml(xml_str, xslt_file):
    # Parse the XSLT file
    xslt_doc = etree.parse(xslt_file)
    # Parse the XML string
    xml_doc = etree.fromstring(xml_str)
    # Apply the XSLT transformation to the XML document
    transform = etree.XSLT(xslt_doc)
    result = transform(xml_doc)
    # Return the transformed result as a string
    return str(result)

if __name__ == "__main__":
    # Define a list of XML file names to parse
    file_names = ["example2.xml","example3.xml"]
    
    # Define the XSLT file name to use for transformation
    xslt_names = ["transform.xslt","transform1.xslt"]

    # Parse each XML file, apply XSLT transformation, and print the resulting string
    for file_name,xslt_file in zip(file_names,xslt_names):
        xml_str = open(file_name).read()
        print(f"--- Parsing and transforming {file_name} ---")
        transformed_str = transform_xml(xml_str, xslt_file)
        print(transformed_str)
