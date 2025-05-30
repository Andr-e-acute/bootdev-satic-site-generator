import unittest
from textnode import TextNode,TextType,text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node= TextNode("This is text node", TextType.BOLD)
        node2 = TextNode("This is text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_default_url_is_none(self):
        node= TextNode("text", TextType.LINK)
        node2 = TextNode("text", TextType.LINK,None)
        self.assertEqual(node, node2)
    def test_different_text_type(self):
        node= TextNode("This is text node", TextType.BOLD)
        node2 = TextNode("This is text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_different_text(self):
        node= TextNode("This is text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_different_url(self):
        node= TextNode("This is text node", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is text node", TextType.LINK, "https://www.example.com")
        self.assertNotEqual(node, node2)
      
    if __name__ == "__main__":
        unittest.main()
class TestTextNodeToHtml(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_bold(self):
        node= TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")
    def test_link_node(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})
    def test_image_node(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://www.boot.dev/image.png", "alt": "This is an image"})
    def test_code_node(self):
        node = TextNode("This is code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code")
    def test_italic_node(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic text")