import unittest
from markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_images, split_nodes_links, text_to_textnodes, markdown_to_html_node
from textnode import ( # pylint:disable=unused-import # noqa: F401
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


class TestMarkdown(unittest.TestCase):

    def test_split_delimiter(self):

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

        self.assertEqual(str(ans), str(result))

    def test_markdown_link_img(self):
        text_img1 = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        text_link1 = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        ans_img_1 = "[('image', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png'), ('another', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png')]"
        ans_link_2 = "[('link', 'https://www.example.com'), ('another', 'https://www.example.com/another')]"
        self.assertEqual(str(extract_markdown_images(text_img1)), str(ans_img_1))
        self.assertEqual(str(extract_markdown_links(text_link1)), str(ans_link_2))

    def test_split_node_images(self):
        test_node_list = [TextNode("![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                    text_type_text),
                TextNode("This is just normal text with no images.", text_type_text),
                TextNode("This node has a single ![PICTURE](https://random.link/sgsgsdfdsf.jpg) with some text and nothing else", text_type_text),
                TextNode("AND THIS IS A RANDOM CODE NODE I GUESS", text_type_code),
            ]
        ans = "[TextNode(image, image, https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png), TextNode( and another , text, None), TextNode(second image, image, https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png), TextNode(This is just normal text with no images., text, None), TextNode(This node has a single , text, None), TextNode(PICTURE, image, https://random.link/sgsgsdfdsf.jpg), TextNode( with some text and nothing else, text, None), TextNode(AND THIS IS A RANDOM CODE NODE I GUESS, code, None)]"

        self.assertEqual(str(split_nodes_images(test_node_list)), str(ans))

    def test_split_node_links(self):
        test_list = [TextNode("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)", text_type_text),
                TextNode("[LINKTEXT](https://www.google.com) text in between followed by [THISLINK](https://www.boot.dev)", text_type_text)
            ]
        ans = "[TextNode(This is text with a , text, None), TextNode(link, link, https://www.example.com), TextNode( and , text, None), TextNode(another, link, https://www.example.com/another), TextNode(LINKTEXT, link, https://www.google.com), TextNode( text in between followed by , text, None), TextNode(THISLINK, link, https://www.boot.dev)]"

        self.assertEqual(str(split_nodes_links(test_list)), str(ans))

    def test_text_to_textnodes(self):
        test_string_1 = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        ans = "[TextNode(This is , text, None), TextNode(text, bold, None), TextNode( with an , text, None), TextNode(italic, italic, None), TextNode( word and a , text, None), TextNode(code block, code, None), TextNode( and an , text, None), TextNode(image, image, https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png), TextNode( and a , text, None), TextNode(link, link, https://boot.dev)]"
        self.assertEqual(str(text_to_textnodes(test_string_1)), str(ans))

    def test_markdown_to_html(self):

        markdown_doc = """# Header 1

## Header 2

This is a paragraph with some **BOLD** and *ITALIC* in it.

> Quote from Obama

```
CHECK OUT MY COOL CODE! IT HAS AN IMAGE IN IT ![alt text for image](url/of/image.jpg)
```

1. I like cheese
2. you like cheese
3. we like cheese
4. uhh cheese

* this is a list
* still a list
"""
        ans = """<div><h1>Header 1</h1><h2>Header 2</h2><p>This is a paragraph with some <b>BOLD</b> and <i>ITALIC</i> in it.</p><blockquote>> Quote from Obama</blockquote><code>CHECK OUT MY COOL CODE! IT HAS AN IMAGE IN IT <img src="url/of/image.jpg" alt="alt text for image"></code><ol><li>I like cheese</li><li>you like cheese</li><li>we like cheese</li><li>uhh cheese</li></ol><ul><li>this is a list</li><li>still a list</li></ul></div>"""
        nodes = markdown_to_html_node(markdown_doc)
        self.assertEqual(str(nodes.to_html()), str(ans))



if __name__ == "__main__":
    unittest.main()
