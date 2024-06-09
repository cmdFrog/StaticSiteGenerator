import pprint
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
    test_list = [
            TextNode("This is text with a `code block` word and another `code block` word and another `code block` word.", text_type_text),
            TextNode("This is a node without any delimiter", text_type_text),
            TextNode("This is text with a `code block` word", text_type_text),
            TextNode("This is text with a **BOLD WORD** word", text_type_text),
            TextNode("`THIS WHOLE THING IS CODE`", text_type_text),
            TextNode("`THIS IS CODE` but this is **BOLD.**", text_type_text),
        ]
    result = split_nodes_delimiter(test_list, '`', text_type_code)
    result = split_nodes_delimiter(result, '**', text_type_bold)
    pprint.pp(result)





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

def check_split_delim_error(current_string):
    if len(current_string) < 3:
        raise SyntaxError("Invalid Markdown syntax, no closing delimiter found")

def process_delimited_text(current_strings, delimiter, text_type):
    labeled_strings = []
    while delimiter in current_strings[-1]:
        current_strings = current_strings[-1].split(delimiter, 2)
        check_split_delim_error(current_strings)
        labeled_strings.append([current_strings[0], "text"])
        labeled_strings.append([current_strings[1], text_type])
    labeled_strings.append([current_strings[2], "text"])
    return labeled_strings

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: str) -> list:
    #text_types = {"text", "code", "italic", "bold", "link", "image"}
    new_node_list = []
    for node in old_nodes:
        if node.text_type != text_type_text or delimiter not in node.text:
            new_node_list.append(node)
            continue

        current_strings = node.text.split(delimiter, 2)
        check_split_delim_error(current_strings)

        labeled_strings = [[current_strings[0], "text"], [current_strings[1], text_type]]
        labeled_strings.extend(process_delimited_text(current_strings, delimiter, text_type))

        for node_con in labeled_strings:
            if node_con[0]:
                new_node_list.append(TextNode(str(node_con[0]), str(node_con[1])))

    return new_node_list



if __name__ == "__main__":
    main()
