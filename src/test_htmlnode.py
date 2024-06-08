import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self): # Check if given node == expected answer
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        ans = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(ans, node.props_to_html())

    def test_props_to_html_2(self): # Check if given node == expected answer with more args given
        node = HTMLNode(tag="a", value="body of text", props={"href": "https://www.google.com", "target": "_blank"})
        ans = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(ans, node.props_to_html())

    def test_props_to_html_NTarg(self): # Test hyperlink creation without target in dictionary
        node = HTMLNode(tag="a", value="body of text", props={"href": "https://www.google.com"})
        ans = ' href="https://www.google.com"'
        self.assertEqual(ans, node.props_to_html())

class TestLeafNode(unittest.TestCase):

    def test_to_html_para(self):
        para_node = LeafNode(value="This is a paragraph!", tag="p")
        ans = "<p>This is a paragraph!</p>"
        self.assertEqual(para_node.to_html(), ans)

    def test_to_html_link(self):
        link_node = LeafNode(value="Click me!", tag="a", props={"href": "https://www.google.com"})
        ans_link = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(link_node.to_html(), ans_link)

        link_node_target = LeafNode(value="Click me!", tag="a", props={"href": "https://www.google.com", "target": "_blank"})        
        ans_link_tar = '<a href="https://www.google.com" target="_blank">Click me!</a>'
        self.assertEqual(link_node_target.to_html(), ans_link_tar)

    def test_no_tag(self):
        node = LeafNode(value="I'm a string lol")
        ans = "I'm a string lol"
        self.assertEqual(node.to_html(), ans)

    def test_value_err(self):
        node = LeafNode(value=None)
        self.assertRaises(ValueError, node.to_html)



if __name__ == "__main__":
    unittest.main()
