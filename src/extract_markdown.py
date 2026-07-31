def extract_title(markdown: str):
    lines = markdown.strip().split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[line.find('# ') + 1:].strip()
    raise Exception(f"Could not find title. Requires a header 1 '# ...'")

