import unittest

from textnode import TextNode
from main import text_node_to_html_node, split_nodes_delimiter
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")

        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold", "boot.dev")
        node2 = TextNode("This is a text node", "bold", "google.com")

        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "boot.dev")

        self.assertIsNone(node.url)
        self.assertIsNotNone(node2.url)

    def test_text_to_html_node(self):
        node1 = TextNode(text_type="bold", text="TEXT GOES HERE :D")
        node2 = TextNode(text_type="link", text="ANCHOR TEXT", url="www.google.com")
        node3 = TextNode(text_type="image", text="IMAGE DESCRIPTION", url="SOURCE/OF/IMAGE.JPG")
        ans1 = LeafNode(tag="b", value="TEXT GOES HERE :D", props=None)
        ans2 = LeafNode(tag="a", value="ANCHOR TEXT", props={'href': 'www.google.com'})
        ans3 = LeafNode(tag="img", value="", props={'src': 'SOURCE/OF/IMAGE.JPG', 'alt': 'IMAGE DESCRIPTION'})

        self.assertEqual(str(text_node_to_html_node(node1)), str(ans1))
        self.assertEqual(str(text_node_to_html_node(node2)), str(ans2))
        self.assertEqual(str(text_node_to_html_node(node3)), str(ans3))

    def test_split_delimiter(self):
        text_type_text = "text"
        text_type_code = "code"
        #text_type_italic = "italic"
        text_type_bold = "bold"
        #text_type_link = "link"
        #text_type_image = "image"
        test_list = [
            TextNode("This is text with a `code block` word and another `code block` word and another `code block` word.", text_type_text),
            TextNode("This is a node without any delimiter", text_type_text),
            TextNode("This is text with a `code block` word", text_type_text),
            TextNode("This is text with a **BOLD WORD** word", text_type_text),
            TextNode("`THIS WHOLE THING IS CODE`", text_type_text),
            TextNode("`THIS IS CODE` but this is **BOLD.**", text_type_text),
        ]
        ans = "[TextNode(This is text with a , text, None), TextNode(code block, code, None), TextNode( word and another , text, None), TextNode(code block, code, None), TextNode( word and another , text, None), TextNode(code block, code, None), TextNode( word., text, None), TextNode(This is a node without any delimiter, text, None), TextNode(This is text with a , text, None), TextNode(code block, code, None), TextNode( word, text, None), TextNode(This is text with a , text, None), TextNode(BOLD WORD, bold, None), TextNode( word, text, None), TextNode(THIS WHOLE THING IS CODE, code, None), TextNode(THIS IS CODE, code, None), TextNode( but this is , text, None), TextNode(BOLD., bold, None)]"
        result = split_nodes_delimiter(test_list, '`', text_type_code)
        result = split_nodes_delimiter(result, '**', text_type_bold)
        self.maxDiff = None
        self.assertEqual(str(ans), str(result))



if __name__ == "__main__":
    unittest.main()
