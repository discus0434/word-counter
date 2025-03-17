import re
from mcp.server import FastMCP

mcp = FastMCP("WordCounter")

@mcp.tool()
def count_words(text: str) -> int:
    """日本語の文字数を数える"""
    cleaned_text = re.sub(r"[\s\n]", "", text)
    return len(cleaned_text)
