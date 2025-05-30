import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )
    def test_basic_parent_render(self):
        node = ParentNode("p", [LeafNode(None, "Hello")])
        self.assertEqual(node.to_html(), "<p>Hello</p>")
        # ✅ Tests basic functionality: parent with one child, no tag on child

    def test_nested_leaf_nodes(self):
        node = ParentNode("p", [
            LeafNode("b", "Bold"),
            LeafNode(None, " text "),
            LeafNode("i", "italic")
        ])
        expected = "<p><b>Bold</b> text <i>italic</i></p>"
        self.assertEqual(node.to_html(), expected)
        # ✅ Tests multiple children and mix of tagged and plain text

    def test_parent_with_props(self):
        node = ParentNode("div", [
            LeafNode(None, "Hello world")
        ], {"class": "highlight"})
        self.assertEqual(node.to_html(), '<div class="highlight">Hello world</div>')
        # ✅ Tests if props are correctly rendered in the parent tag

    def test_deeply_nested_parents(self):
        inner = ParentNode("span", [LeafNode(None, "inner")])
        outer = ParentNode("div", [inner])
        self.assertEqual(outer.to_html(), "<div><span>inner</span></div>")
        # ✅ Tests recursion: parent inside parent

    def test_raises_on_missing_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode(None, "oops")])
        # ✅ Required tag check

    def test_raises_on_missing_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)
        # ✅ Required children check

    def test_empty_children_list(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")
        # ✅ Edge case: no children, but still valid (empty tag)