from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    # TestNode = TextNode("This is a text node", "bold", "https://boot,dev")
    # print(TestNode)
    # TestHTMLNode = HTMLNode(tag="a", value="This is a value", props={"href": "https://google.com", "target": "_blank"})
    # print(TestHTMLNode)
    # print(TestHTMLNode.props_to_html())
    # link_node = LeafNode("Click me!", "a", {"href": "https://www.google.com",})
    # print(link_node.to_html())

    TestParent = ParentNode(
        tag="p",
        children=[
            LeafNode(tag="b", value="Bold text"),
            LeafNode(tag=None, value="Normal text"),
            ParentNode(tag="article",
                    children=[
                        LeafNode(tag="i", value="nested italic text"),
                        LeafNode(tag="b", value="nested Bold text"),
                    ]),
            LeafNode(tag="i", value="italic text"),
            LeafNode(tag=None, value="Normal text"),
        ],
    )
    print(TestParent.to_html())
    #print(TestParent.children[1].to_html())







main()