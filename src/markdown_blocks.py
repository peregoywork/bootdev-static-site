from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown: str) -> str:
    return [
        md.strip()
        for md in markdown.split("\n\n")
        if md != ""
    ]


def block_to_block_type(md_block: str) -> BlockType:
    is_heading = re.match(r"(#{1,6})", md_block)
    is_code = re.match(r"\s*`{3}[\s\S]*`{3}\s*", md_block)
    is_quote = [
        re.match(r"(>)", md)
        for md in md_block.split('\n')
    ]
    is_unordered_list = [
        re.match(r"(- )", md)
        for md in md_block.split('\n')
    ]
    is_ordered_list = [
        re.match(r"(\w\. )", md)
        for md in md_block.split('\n')
    ]
    #
    if is_heading: return BlockType.HEADING
    if is_code: return BlockType.CODE
    if all(is_quote): return BlockType.QUOTE
    if all(is_unordered_list): return BlockType.UNORDERED_LIST
    if all(is_ordered_list): return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
