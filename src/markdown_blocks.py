from enum import Enum
from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ORDERED_LIST = "ordered_list"
    UNORDERED_LIST = "unordered_list"


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def text_to_code(text: str):
    text = text[4:-3]
    inner_node = TextNode(text, TextType.CODE)
    html_node = text_node_to_html_node(inner_node)
    return html_node

def text_to_quoteblock(text: str):
    text = text.replace('> ', '').replace('\n', ' ')
    return text_to_children(text)

def text_to_unordered_list(text: str):
    return [
        ParentNode('li', text_to_children(line[2:].strip()))
        for line in text.split('\n') 
    ]

def text_to_ordered_list(text: str):
    return [
        ParentNode('li', text_to_children(line.split('.')[1].strip()))
        for line in text.split('\n') 
    ]

def text_to_children(text: str):
    textnodes = text_to_textnodes(text.replace('\n', ' '))
    htmlnodes = [text_node_to_html_node(t) for t in textnodes]
    return htmlnodes

def block_to_html_node(block, block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            children = text_to_children(block)
            return ParentNode('p', children)
        case BlockType.HEADING:
            level = block.split(' ')[0].count('#')
            block = block[level + 1:]
            children = text_to_children(block)
            return ParentNode(f'h{level}', children)
        case BlockType.CODE:
            code_node = text_to_code(block)
            return ParentNode('pre', [code_node])
        case BlockType.QUOTE:
            quote_node = text_to_quoteblock(block)
            return ParentNode('blockquote', quote_node)
        case BlockType.UNORDERED_LIST:
            list_nodes = text_to_unordered_list(block)
            return ParentNode('ul', list_nodes)
        case BlockType.ORDERED_LIST:
            list_nodes = text_to_ordered_list(block)
            return ParentNode('ol', list_nodes)

def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    child_nodes = []
    for block in blocks:
        if block == "":
            continue
        block_type = block_to_block_type(block)
        node = block_to_html_node(block, block_type)
        child_nodes.append(node)
    return ParentNode('div', child_nodes)



