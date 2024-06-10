from textnode import ( # pylint:disable=unused-import # noqa: F401
        TextNode,
        text_type_text,
        text_type_bold,
        text_type_italic,
        text_type_code,)

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
