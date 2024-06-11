import pprint # pylint:disable=unused-import # noqa: F401
import re
from htmlnode import HTMLNode, ParentNode, LeafNode # pylint:disable=unused-import # noqa: F401
from textnode import text_node_to_html_node
from textnode import (  # pylint:disable=unused-import # noqa: F401
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)
from markdown_blocks import ( # pylint:disable=unused-import # noqa: F401
block_type_code,
block_type_heading,
block_type_ordered_list,
block_type_paragraph,
block_type_quote,
block_type_unordered_list,
block_to_block_type,
markdown_to_blocks
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
    to_match = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    if not to_match:
        return
    matched_tuples = []
    #print(to_match)
    for txt in to_match:
        #print(txt)
        matched_tuples.append((txt[0], txt[1]))
    #print(matched_tuples)

    return matched_tuples


def extract_markdown_links(text: str) -> tuple:
    to_match = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    if not to_match:
        return
    matched_tuples = []
    #print(to_match)
    for txt in to_match:
        #print(txt)
        matched_tuples.append((txt[0], txt[1]))
    #print(matched_tuples)

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
            #print(split_text)
            if split_text[0]:
                new_node_list.append(TextNode(split_text[0], text_type_text))
            new_node_list.append(TextNode(image_tup[0], text_type_image, image_tup[1]))
            #print(split_text)
            text = split_text[1]
        if text:
            new_node_list.append(TextNode(text, text_type_text))
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
            #print(split_text)
            text = split_text[1]
        if text:
            new_node_list.append(TextNode(text, text_type_text))
    return new_node_list

def text_to_textnodes(text: str) -> list:
    node = TextNode(text, text_type_text)
    #print(f'ORIGINAL TEXT: {text}')
    new_list = split_nodes_images([node])
    #pprint.pp(f'SPLIT NODES IMAGES: {new_list}')
    new_list = split_nodes_links(new_list)
    #pprint.pp(f'SPLIT NODES LINKS: {new_list}')
    new_list = split_nodes_delimiter(new_list, '`', text_type_code)
    #pprint.pp(f'SPLIT CODE: {new_list}')
    new_list = split_nodes_delimiter(new_list, '**', text_type_bold)
    #pprint.pp(f'SPLIT ITALIC: {new_list}')
    new_list = split_nodes_delimiter(new_list, '*', text_type_italic)
    #pprint.pp(f'SPLIT BOLD: {new_list}')
    return new_list

def block_to_html_node_code(block: str, block_type: str) -> HTMLNode:
    removed_marks = block.strip("\n```\n")
    child_text_nodes = text_to_textnodes(removed_marks)
    child_leaf_nodes = []
    for child in child_text_nodes:
        child_leaf_nodes.append(text_node_to_html_node(child))
    html_node = ParentNode(tag=block_type, children=child_leaf_nodes)
    return html_node

def block_to_html_node_header(block: str, block_type: str) -> HTMLNode:
    removed_marks = block.strip("# ")
    num_hashes = len(block) - len(removed_marks) - 1
    child_text_nodes = text_to_textnodes(removed_marks)
    child_leaf_nodes = []
    for child in child_text_nodes:
        print(child)
        child_leaf_nodes.append(text_node_to_html_node(child))
    html_node = ParentNode(tag=f"h{num_hashes}", children=child_leaf_nodes)
    return html_node

def block_to_html_node_olist(block: str, block_type: str) -> HTMLNode:
    cleaned_items = []
    list_items = block.split("\n")
    for item in list_items:
        if not item:
            continue
        string = item[3:]
        children = []
        for textnode in text_to_textnodes(string):
            html = text_node_to_html_node(textnode)
            children.append(html)
        cleaned_items.append(ParentNode(tag="li", children=children))
    return ParentNode(tag="ol", children=cleaned_items)

def block_to_html_node_ulist(block: str, block_type: str) -> HTMLNode:
    cleaned_items = []
    list_items = block.split("\n")
    for item in list_items:
        if not item:
            continue
        string = item[2:]
        children = []
        for textnode in text_to_textnodes(string):
            html = text_node_to_html_node(textnode)
            children.append(html)
        cleaned_items.append(ParentNode(tag="li", children=children))
    return ParentNode(tag="ul", children=cleaned_items)

def block_to_html_para(block: str, block_type: str) -> HTMLNode:
    split = block.split("\n")
    text = " ".join(split)
    children = []
    textnodes = text_to_textnodes(text)
    for textnode in textnodes:
        html = text_node_to_html_node(textnode)
        children.append(html)
    return ParentNode(tag="p", children=children)

def block_to_html_quote(block: str, block_type: str) -> HTMLNode:
    split = block.split("\n")
    text = " ".join(split)
    children = []
    textnodes = text_to_textnodes(text)
    for textnode in textnodes:
        html = text_node_to_html_node(textnode)
        children.append(html)
    return ParentNode(tag="blockquote", children=children)
