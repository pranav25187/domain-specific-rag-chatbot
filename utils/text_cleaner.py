import re

def clean_text(text: str) -> str:
    """
    Cleans extracted PDF text
    """
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\n+', '\n', text)
    text = text.strip()
    return text
