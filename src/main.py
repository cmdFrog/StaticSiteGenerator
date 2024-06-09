from textnode import TextNode
from htmlnode import LeafNode


def main():
    print("Quiche Eater")

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    tag_val_nodes = {"italic": "i", "bold": "b", "code": "code"}

    if text_node.text_type in tag_val_nodes:
        return LeafNode(tag=tag_val_nodes[text_node.text_type], value=text_node.text,)

    if text_node.text_type == "text":
        return LeafNode(value=text_node.text)

    if text_node.text_type == "link":
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})

    if text_node.text_type == "image":
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})

    raise ValueError("Incompatible or no text_type in text_node_to_html_node input")





if __name__ == "__main__":
    main()
