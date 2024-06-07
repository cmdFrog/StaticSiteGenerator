import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self): # Check if given node == expected answer
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        ans = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(ans, node.props_to_html())
    def test_props_to_html_2(self): # Check if given node == expected answer with more args given
        node = HTMLNode(tag="<a>", value="body of text", props={"href": "https://www.google.com", "target": "_blank"})
        ans = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(ans, node.props_to_html())


if __name__ == "__main__":
    unittest.main()
