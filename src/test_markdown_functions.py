import unittest
from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type


class TestMarkdownBlock(unittest.TestCase):  
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_extra_spacing(self):
        md = """testing some     extra
            spacing between characters and

                at the beginning and end of a new line    
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "testing some     extra\n            spacing between characters and",
                "at the beginning and end of a new line",
            ]
        )
                
    def test_markdown_to_blocks_incorrect_extra_spacing(self):
        md = """ let's start with some extra    
                      
                      spacing 

                            for 

                                fun

                                    testing
        """
        blocks = markdown_to_blocks(md)
        self.assertNotEqual(
            blocks,
            [
                "let's start with some extra",
                "spacing",
                "for",
                "fun",
                "testing",
            ]
        )

    def test_markdown_block_type_paragraph(self):
        md = """just any old words"""
        block = markdown_to_blocks(md)[0]
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_markdown_block_type_header(self):
        md = """
# header one

## header two

### header three

#### header four

##### header five

###### header six
        """
        blocks = markdown_to_blocks(md)
        block_types = [block_to_block_type(block) for block in blocks]
        for block_type in block_types:
            self.assertEqual(block_type, BlockType.HEADING)

    def test_markdown_block_type_code(self):
        md = """
``` 
x = [i % 2 for i in range(10)]
print(x)
```
        """
        block = markdown_to_blocks(md)[0]
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)


    def test_markdown_block_type_quote(self):
        md = """
> one big quote
> section
>with optional spacing on this line
        """
        block = markdown_to_blocks(md)[0]
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_markdown_block_type_unordered_list(self):
        md = """
- one
- two
- three
        """
        block = markdown_to_blocks(md)[0]
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_markdown_block_type_ordered_list(self):
        md = """
1. one
2. two
3. three
        """
        block = markdown_to_blocks(md)[0]
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)



