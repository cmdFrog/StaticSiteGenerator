import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, block_type_code, block_type_heading, block_type_ordered_list, block_type_paragraph

class TestMarkdownBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):

        test_string = """ This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items """
        ans = ['This is **bolded** paragraph', 'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', '* This is a list\n* with items']
        self.assertEqual(str(markdown_to_blocks(test_string)), str(ans))

    def test_block_to_block_type(self):
        test_line = """```
This is code
```"""
        test_line_2 = """##### HEADING"""
        test_line_3 = """1. Item 1
2. Item 2
3. Item 3"""
        test_line_4 = """This is a paragraph"""
        test_list = [test_line, test_line_2, test_line_3, test_line_4]
        ans_list = [block_type_code, block_type_heading, block_type_ordered_list, block_type_paragraph]
        for test, ans in zip(test_list, ans_list):
            #print(test, ans)
            self.assertEqual(block_to_block_type(test), ans)

if __name__ == "__main__":
    unittest.main()
