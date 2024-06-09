from textnode import TextNode
from htmlnode import LeafNode

text_type_text = "text"
text_type_code = "code"
text_type_italic = "italic"
text_type_bold = "bold"
text_type_link = "link"
text_type_image = "image"

def main():
    print("Quiche Eater")
    testing_node = TextNode("This is text with a `code block` word and another `code block` word and another `code block` word.", text_type_text)
    testing_node2 = TextNode("This is a node without any delimiter", text_type_text)
    testing_node3 = TextNode("This is text with a `code block` word", text_type_text)
    testing_bold = TextNode("This is text with a **BOLD WORD** word", text_type_text)
    test_list = [testing_node, testing_node2, testing_node3]
    test_list2 = [testing_node3]
    new_nodes = split_nodes_delimiter([testing_bold], "**", text_type_bold)
    new_nodes_code = split_nodes_delimiter(test_list, '`', text_type_code)
    print(new_nodes)
    print(new_nodes_code)





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


def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: str) -> list:
    #text_types = {"text", "code", "italic", "bold", "link", "image"}
    new_node_list = []
    current_strings = []
    labeled_strings = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_node_list.append(node)

        if delimiter not in node.text:
            new_node_list.append(node)

        if delimiter in node.text:
            current_strings = node.text.split(delimiter, 2)

            if len(current_strings) < 3:
                raise SyntaxError("Invalid Markdown syntax, no closing delimiter found")

            labeled_strings.append([current_strings[0], "text"])
            labeled_strings.append([current_strings[1], text_type])

            while delimiter in current_strings[-1]:
                current_strings = current_strings[-1].split(delimiter, 2)

                if len(current_strings) < 3:
                    raise SyntaxError("Invalid Markdown syntax, no closing delimiter found")

                labeled_strings.append([current_strings[0], "text"])
                labeled_strings.append([current_strings[1], text_type])
            labeled_strings.append([current_strings[2], "text"])

            for node_con in labeled_strings:
                new_node_list.append([TextNode(str(node_con[0]), str(node_con[1]))])

    return new_node_list



if __name__ == "__main__":
    main()
