from textnode import TextNode
from htmlnode import HTMLNode, LeafNode

def main():
    TestNode = TextNode("This is a text node", "bold", "https://boot,dev")
    print(TestNode)
    TestHTMLNode = HTMLNode(tag="a", value="This is a value", props={"href": "https://google.com", "target": "_blank"})
    print(TestHTMLNode)
    print(TestHTMLNode.props_to_html())
    link_node = LeafNode("Click me!", "a", {"href": "https://www.google.com",})
    print(link_node.to_html())
main()