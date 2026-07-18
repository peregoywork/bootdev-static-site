import unittest
from htmlnode import HTMLNode, LeafNode


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
        print(node)

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


if __name__=='__main__':
    unittest.main()

