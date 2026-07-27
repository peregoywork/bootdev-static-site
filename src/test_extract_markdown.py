import unittest
from inline_markdown import extract_markdown_images, extract_markdown_links


class TestTextNode(unittest.TestCase):  
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertListEqual([
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with an [booty](https://boot.dev)"
        )
        self.assertListEqual([("booty", "https://boot.dev")], matches)

    def test_extract_multiple_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual([
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ], matches)

    def test_extract_markdown_mixture(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and an image ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        link_matches = extract_markdown_links(text)
        image_matches = extract_markdown_images(text)
        #
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], link_matches)
        self.assertListEqual([("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], image_matches)


