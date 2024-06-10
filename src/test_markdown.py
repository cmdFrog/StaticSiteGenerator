import unittest
from markdown import split_nodes_delimiter
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


if __name__ == "__main__":
    unittest.main()
