import unittest
from inliner_parser import split_nodes_delimiter,extract_markdown_images,extract_markdown_links,split_nodes_image,split_nodes_link
#             new_nodes.append(TextNode(original_text, TextType.TEXT))
from textnode import TextNode,TextType

class TestInlinerParser(unittest.TestCase):
    def test_split_code_inline(self):
        input_node = TextNode("This is `code` in text", TextType.TEXT)
        result = split_nodes_delimiter([input_node], "`", TextType.CODE)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" in text", TextType.TEXT),
            ]
        self.assertEqual(result, expected)
    
    def test_basic_matching(self):
        input_node =TextNode("this is **bold** text", TextType.TEXT)
        result= split_nodes_delimiter([input_node],"**",TextType.BOLD)
        expected= [
           TextNode("this is ",TextType.TEXT),
           TextNode("bold", TextType.BOLD),
           TextNode(" text",TextType.TEXT)
        ]
        self.assertEqual(result, expected)
    def test_no_delimiter(self):
        input_node = TextNode("no formatting here", TextType.TEXT)
        result = split_nodes_delimiter([input_node], "**", TextType.BOLD)
        expected = [TextNode("no formatting here", TextType.TEXT)]
        self.assertEqual(result, expected)
    def test_unmatched_delimiter_raises(self):
        input_node = TextNode("this is *broken", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([input_node], "*", TextType.ITALIC)

    def test_extract_markdown_images(self):
        text = "Here is an image ![alt text](http://example.com/image.png)"
        result = extract_markdown_images(text)
        expected = [("alt text", "http://example.com/image.png")]
        self.assertEqual(result, expected)
    def test_extract_markdown_links(self):
        text = "Here is a link [example](http://example.com)"
        result = extract_markdown_links(text)
        expected = [("example", "http://example.com")]
        self.assertEqual(result, expected)
    def test_extract_markdown_images2(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_nodes_image_single(self):
        node = TextNode("Text before ![alt](https://img.com/x.png) text after", TextType.TEXT)
        result = split_nodes_image([node])

        expected = [
            TextNode("Text before ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "https://img.com/x.png"),
            TextNode(" text after", TextType.TEXT),
        ]   
        self.assertEqual(result, expected)
    def test_split_nodes_image_none(self):
        node = TextNode("Plain text with no images", TextType.TEXT)
        result = split_nodes_image([node])
        expected = [TextNode("Plain text with no images", TextType.TEXT)]
        self.assertEqual(result, expected)


