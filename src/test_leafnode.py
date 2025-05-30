import unittest
from leafnode import LeafNode
class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_with_tag_and_props(self):
        node = LeafNode("a", "Click me", {"href": "https://example.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://example.com">Click me</a>'
        )
        # ✅ Tests attribute rendering

    def test_leaf_to_html_without_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")
        # ✅ Tests raw text output (no tag)

    def test_leaf_raises_if_value_is_none(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)
        # ✅ Tests required value logic

    def test_leaf_handles_multiple_props(self):
        node = LeafNode("img", "alt text", {"src": "img.png", "alt": "An image"})
        self.assertEqual(
            node.to_html(),
            '<img src="img.png" alt="An image">alt text</img>'
        )
        # ✅ Tests multiple attributes and ordering doesn’t break rendering

    def test_leaf_allows_empty_string_value(self):
        node = LeafNode("div", "")
        self.assertEqual(node.to_html(), "<div></div>")
        # ✅ Confirms empty string is allowed as value (not the same as None)