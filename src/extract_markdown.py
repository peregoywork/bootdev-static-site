import re


def extract_markdown_images(text: str) -> tuple[str]:
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
def extract_markdown_links(text: str) -> tuple[str]:
    return re.findall(r"(?<!\!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


