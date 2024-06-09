import unittest

from textnode import TextNode
from main import text_node_to_html_node
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

if __name__ == "__main__":
    unittest.main()
