import unittest
from htmlnode import HTMLNode, LeafNode
from markdown_blocks import markdown_to_html_node

class TestHTMLNode(unittest.TestCase):
    def test_creation(self):
        node_blank = HTMLNode()
        node_full = HTMLNode( 
            tag="a", 
            value="text inside a paragraph", 
            children=node_blank,
            props={"href": ""},
        )
        assert True == True

    def test_props_to_html(self):
        expected_outcome = 'href="https://www.google.com" target="_blank"'
        node = HTMLNode(props={ "href": "https://www.google.com", "target": "_blank" })
        self.assertEqual(expected_outcome, node.props_to_html())

    def test_props_to_html_none(self):
        node = HTMLNode()
        self.assertEqual("", node.props_to_html())

    def test_can_print(self):
        node = HTMLNode(props={ "href": "https://www.google.com", "target": "_blank" })
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(None, None, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        )


class TestLeafNode(unittest.TestCase):
    def test_create_leaf(self):
        leaf_node = LeafNode(None, "testing!")
        leaf_node = LeafNode("", "testing me twice!")
        leaf_node = LeafNode("a", "link me")
        leaf_node = LeafNode("a", "link me", {"href": "boot.dev"})
        assert True == True # no errors thrown

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_no_value_raises(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_repr(self):
        node = LeafNode("span", "some text", {"class": "highlight"})
        self.assertEqual(
            node.__repr__(),
            "LeafNode(span, some text, {'class': 'highlight'})",
        )   


class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


if __name__=='__main__':
    unittest.main()

