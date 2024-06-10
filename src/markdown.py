import re
from textnode import (  # pylint:disable=unused-import # noqa: F401
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)


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
    # text_types = {"text", "code", "italic", "bold", "link", "image"}
    new_node_list = []
    for node in old_nodes:
        if node.text_type != text_type_text or delimiter not in node.text:
            new_node_list.append(node)
            continue

        current_strings = node.text.split(delimiter, 2)
        check_split_delim_error(current_strings)

        labeled_strings = [
            [current_strings[0], "text"],
            [current_strings[1], text_type],
        ]
        labeled_strings.extend(
            process_delimited_text(current_strings, delimiter, text_type)
        )

        for node_con in labeled_strings:
            if node_con[0]:
                new_node_list.append(TextNode(str(node_con[0]), str(node_con[1])))

    return new_node_list


def extract_markdown_images(text: str) -> tuple:
    matched_tuples = []
    matched_alt = re.findall(r"!\[(.*?)\]", text)
    matched_link = re.findall(r"\((.*?)\)", text)
    for link, alt in zip(matched_link, matched_alt):
        matched_tuples.append((alt, link))

    return matched_tuples


def extract_markdown_links(text: str) -> tuple:
    matched_tuples = []
    matched_alt = re.findall(r"\[(.*?)\]", text)
    matched_link = re.findall(r"\((.*?)\)", text)
    for link, anchor in zip(matched_link, matched_alt):
        matched_tuples.append((anchor, link))

    return matched_tuples

def split_nodes_images(old_nodes: list) -> list:

    new_node_list = []
    for node in old_nodes:
        if not node.text:
            continue
        if node.text_type != text_type_text:
            new_node_list.append(node)
            continue
        if not extract_markdown_images(node.text):
            new_node_list.append(node)
            continue
        #print(f"NODE: {node}")
        matches = extract_markdown_images(node.text)
        text = node.text
        for image_tup in matches:
            #print(f"IMAGE_TUP: {image_tup}")
            split_text = text.split(f"![{image_tup[0]}]({image_tup[1]})", 1)
            if split_text[0]:
                new_node_list.append(TextNode(split_text[0], text_type_text))
            new_node_list.append(TextNode(image_tup[0], text_type_image, image_tup[1]))
            text = split_text[1]
    return new_node_list

def split_nodes_links(old_nodes: list) -> list:
    new_node_list = []
    for node in old_nodes:
        if not node.text:
            continue
        if node.text_type != text_type_text:
            new_node_list.append(node)
            continue
        if not extract_markdown_links(node.text):
            new_node_list.append(node)
            continue
        matches = extract_markdown_links(node.text)
        text = node.text
        for link_tup in matches:
            split_text = text.split(f"[{link_tup[0]}]({link_tup[1]})", 1)
            if split_text[0]:
                new_node_list.append(TextNode(split_text[0], text_type_text))
            new_node_list.append(TextNode(link_tup[0], text_type_link, link_tup[1]))
            text = split_text[1]
    return new_node_list
