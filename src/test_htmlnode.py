import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
  def test_props_to_html_none(self):
    node = HTMLNode(props=None)
    self.assertEqual(node.props_to_html(), "")
  def test_props_to_html_empty(self):
    node = HTMLNode(props={})
    self.assertEqual(node.props_to_html(), "")
  def test_props_to_html_single(self):
    node = HTMLNode(props={"href": "https://example.com"})
    self.assertEqual(node.props_to_html(), ' href="https://example.com"')
  def test_props_to_html_multiple(self):
    node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
    result = node.props_to_html()
    valid_outputs = [
        ' href="https://example.com" target="_blank"',
        ' target="_blank" href="https://example.com"',
    ]
    self.assertIn(result, valid_outputs)
