import unittest
from htmlnode import HTMLNode


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


if __name__=='__main__':
    unittest.main()

