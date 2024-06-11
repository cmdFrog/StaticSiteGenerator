from htmlnode import LeafNode

text_type_text = "text"
text_type_code = "code"
text_type_italic = "italic"
text_type_bold = "bold"
text_type_link = "link"
text_type_image = "image"
text_type_list = "list"

class TextNode:
    def __init__(self, text: str, text_type: str, url: str=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    tag_val_nodes = {"italic": "i", "bold": "b", "code": "code", "list": "l"}

    if text_node.text_type in tag_val_nodes:
        return LeafNode(tag=tag_val_nodes[text_node.text_type], value=text_node.text,)

    if text_node.text_type == "text":
        return LeafNode(value=text_node.text)

    if text_node.text_type == "link":
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})

    if text_node.text_type == "image":
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})

    if text_node.text_type == "list":
        return LeafNode(tag="li", value=text_node.value)

    raise ValueError("Incompatible or no text_type in text_node_to_html_node input")
