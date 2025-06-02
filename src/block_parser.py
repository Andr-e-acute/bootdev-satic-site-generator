from enum import Enum
import re
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks=[]
    splitedMarkdown = markdown.split("\n\n")
    for block in splitedMarkdown:
        cleaned_block = "\n".join(line.strip() for line in block.strip().splitlines())
        if cleaned_block !='': 
            blocks.append(cleaned_block)

    return blocks

def block_to_block_type(block):
    lines = block.splitlines()

    # Heading: starts with 1 to 6 '#' followed by a space
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING

    # Code block: starts and ends with ```
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # Quote block: every line starts with >
    elif all(re.match(r"^> ?", line) for line in lines):
        return BlockType.QUOTE

    # Unordered list: every line starts with '- '
    elif all(re.match(r"^- ", line) for line in lines):
        return BlockType.UNORDERED_LIST

    # Ordered list: every line starts with '1. ', '2. ', etc.
    elif all(re.match(r"^\d+\. ", line) for line in lines):
        return BlockType.ORDERED_LIST

    # Default to paragraph
    else:
        return BlockType.PARAGRAPH