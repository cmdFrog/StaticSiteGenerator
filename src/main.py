from textnode import TextNode
from htmlnode import HTMLNode

def main():
    TestNode = TextNode("This is a text node", "bold", "https://boot,dev")
    print(TestNode)
    TestHTMLNode = HTMLNode(tag="<a>", value="This is a value", props={"href": "https://google.com", "target": "_blank"})
    print(TestHTMLNode)

main()