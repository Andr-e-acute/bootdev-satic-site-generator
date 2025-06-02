import unittest
from block_parser import markdown_to_blocks, block_to_block_type, BlockType
class TestMarkdownToBlocks(unittest.TestCase):
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
        def test_simple_paragraphs(self):
            md = "This is a paragraph.\n\nThis is another paragraph."
            self.assertEqual(
                markdown_to_blocks(md),
                ["This is a paragraph.", "This is another paragraph."]
            )
        def test_inner_linebreaks_and_indentation(self):
            md = "  First paragraph line one  \n    Line two indented  \n\n  Second paragraph  "
            self.assertEqual(
                markdown_to_blocks(md),
                ["First paragraph line one\nLine two indented", "Second paragraph"]
            )
        def test_heading_and_paragraph(self):
            md = "   # Heading   \n\n   Paragraph with spaces   "
            self.assertEqual(
                markdown_to_blocks(md),
                ["# Heading", "Paragraph with spaces"]
            )
        class TestBlockToBlockType(unittest.TestCase):
            def test_heading(self):
                block = "# Heading"
                self.assertEqual(block_to_block_type(block), BlockType.HEADING)
                self.assertEqual(block_to_block_type("###### Deep heading"), BlockType.HEADING)

            def test_code_block(self):
                block = "```\ncode\n```"
                self.assertEqual(block_to_block_type(block), BlockType.CODE)

            def test_quote_block(self):
                block = "> This is a quote\n> Another line of quote"
                self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

            def test_unordered_list(self):
                block = "- Item 1\n- Item 2"
                self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

            def test_ordered_list(self):
                block = "1. First item\n2. Second item"
                self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

            def test_paragraph(self):
                block = "This is a simple paragraph."
                self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
            
            def test_mixed_content_falls_back_to_paragraph(self):
                mixed = "- list?\nbut no second item\nand no consistency"
                self.assertEqual(block_to_block_type(mixed), BlockType.PARAGRAPH)