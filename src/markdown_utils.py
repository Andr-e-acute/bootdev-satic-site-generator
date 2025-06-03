def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith('# '):
            return line.lstrip('# ').strip()
        else: 
            raise ValueError("Markdown does not contain a title starting with '# '")
        