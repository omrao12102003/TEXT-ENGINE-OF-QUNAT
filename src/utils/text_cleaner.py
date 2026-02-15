import re

def clean_text(text: str) -> str:
    """Normalize user input for parsing."""
    text = text.lower().strip()
    text = re.sub(r'\s+', ' ', text)  # Multiple spaces → single
    text = text.replace('%', ' percent ')
    return text
