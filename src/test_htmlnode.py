import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html_tags(self):
        para_node = LeafNode(value="This is a paragraph!", tag="p")  # p tag test
        ans = "<p>This is a paragraph!</p>"
        self.assertEqual(para_node.to_html(), ans)

        ital_node = LeafNode(value="This is itallics!", tag="i")  # i tag test
        ital_ans = "<i>This is itallics!</i>"
        self.assertEqual(ital_node.to_html(), ital_ans)

        bold_node = LeafNode(value="This is bold!", tag="b") # b tag test
        bold_ans = "<b>This is bold!</b>"
        self.assertEqual(bold_ans, bold_node.to_html())

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

class TestParent(unittest.TestCase):

    def test_nested_cases(self):
        TestParentNode = ParentNode(
        tag="p",
        children=[
            LeafNode(tag="b", value="Bold text"),
            LeafNode(tag=None, value="Normal text"),
            ParentNode(tag="article",
                    children=[
                        LeafNode(tag="i", value="nested italic text"),
                        LeafNode(tag="b", value="nested Bold text"),
                    ]),
            LeafNode(tag="i", value="italic text"),
            LeafNode(tag=None, value="Normal text"),
        ],
    )
        ans = "<p><b>Bold text</b>Normal text<article><i>nested italic text</i><b>nested Bold text</b></article><i>italic text</i>Normal text</p>"
        self.assertEqual(TestParentNode.to_html(), ans)

    def tests_normal_cases(self):
        TestParentNode = ParentNode(
        tag="p",
        children=[
        LeafNode(tag="b", value="Bold text"),
        LeafNode(tag=None, value="Normal text"),
        LeafNode(tag="i", value="italic text"),
        LeafNode(tag=None, value="Normal text"),
        ],
    )
        ans = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(TestParentNode.to_html(), ans)



if __name__ == "__main__":
    unittest.main()
