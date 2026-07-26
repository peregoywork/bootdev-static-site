import unittest
from textnode import TextNode, TextType, split_nodes_delimiter, split_nodes_image, split_nodes_link

class TestNodeSplitting(unittest.TestCase):
    def test_basic_delimiter(self):
        node = TextNode("This is a **text** node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD) 
        exp_results = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" node", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, exp_results)


    def test_starting_delimiter(self):
        node = TextNode("**This** is a text node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        exp_results = [
            TextNode("This", TextType.BOLD),
            TextNode(" is a text node", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, exp_results)
        

    def test_ending_delimiter(self):
        node = TextNode("This is a text **node**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        exp_results = [
            TextNode("This is a text ", TextType.TEXT),
            TextNode("node", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, exp_results)
       

    def test_multi_instance_delimiter(self):
        node = TextNode("This is a **text** node with **two** instances", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        exp_results = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" node with ", TextType.TEXT),
            TextNode("two", TextType.BOLD),
            TextNode(" instances", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, exp_results)
        

    def test_malformed_delimiter(self):
        node = TextNode("This is a malformed **text node", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)
        node = TextNode("This is a malformed **text** **node", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    
    def test_each_delimiter(self):
        node_1 = TextNode("This is a malformed **text** node", TextType.TEXT)
        node_2 = TextNode("This is a malformed _text_ node", TextType.TEXT)
        node_3 = TextNode("This is a malformed `text` node", TextType.TEXT)
        node_4 = TextNode("This is a malformed text node", TextType.TEXT)
   

    def test_empty_string(self):
        node = TextNode("", TextType.TEXT)


    def test_multiple_nodes(self):
        nodes = [
            TextNode("This is a bold **text** node", TextType.TEXT),
            TextNode("This is a bold text **node**", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)


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
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )


    def test_split_images_no_images(self):
        nodes = [
            TextNode("This is text with no images", TextType.TEXT),
            TextNode("This text has a link [boot link](https://boot.dev)", TextType.TEXT),
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertListEqual(
            [
                TextNode("This is text with no images", TextType.TEXT),
                TextNode("This text has a link [boot link](https://boot.dev)", TextType.TEXT),
            ],
            new_nodes,
        )


    def test_split_image_or_link_empty(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("", TextType.TEXT),
            ],
            new_nodes,
        )


    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes,
        )


