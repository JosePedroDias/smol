# https://www.datacamp.com/tutorial/smolagents
from typing import Optional
import json

from smolagents import tool 

from pypdf import PdfReader
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/114.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

@tool
def get_weather(location: str) -> str:
    """
    Get weather in the next days at given location.

    Args:
        location: the location to get the weather for
    """
    return "It's sunny in " + location + ", with mild wind and around 15 degrees celsius!"

# wired
# the verge
# ars technica


@tool
def get_reuters_headlines() -> str:
    """Returns the latest top headlines from Reuters.com"""
    url = "https://www.reuters.com"
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        #print(soup.prettify())

        headlines = []
        for tag in soup.select(".story-card")[:5]:  # Get top 5 headlines
            heading = tag.select_one('[data-testid="Heading"]')
            print('------')
            print(heading.prettify())
            title = heading.get_text(strip=True)
            if title:
                headlines.append(f"- {title}")
        
        return "\n".join(headlines) if headlines else "No headlines found."
    
    except Exception as e:
        return f"Error fetching Reuters headlines: {e}"

@tool
def read_pdf_file(file_path: str, max_pages: Optional[int]) -> str:
    """
    This function reads the first three pages of a PDF file and returns its content as a string.
    Args:
        file_path: The path to the PDF file.
        max_pages: The maximum number of pages to read. If None, all pages will be read.
    Returns:
        A string containing the textual content of the PDF file.
    """
    content = ""
    reader = PdfReader(file_path)
    #print(len(reader.pages))
    pages = reader.pages[:max_pages] if max_pages else reader.pages
    for page in pages:
        content += page.extract_text()
    return content

if __name__ == "__main__":
    #print(get_weather("Lisbon"))
    #print(get_reuters_headlines())
    #print(read_pdf_file('/Users/jdi14/Downloads/Sprint Review - Sprint 97 - gen ai excerpt.pdf', None))
    #print(read_pdf_file('/Users/jdi14/Downloads/Comprovativo.pdf', None))
    pass
    