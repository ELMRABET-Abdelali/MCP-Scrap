import webbrowser
import httpx
from bs4 import BeautifulSoup
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP(
    'My Tools',
    dependencies=[
        'beautifulsoup4',
    ],
)


@mcp.tool(
    name='Open-Page-In-Browser',
    description='Open a URL in the default web browser',
)
def open_page_in_browser(url: str) -> None:
    """Open a URL in the default web browser."""
    try:
        webbrowser.open(url)
        return f"Opened {url} in the default web browser."
    except Exception as e:
        return f"Error opening URL: {str(e)}"



def extract_web_content(url: str) -> str | None:
    """
    Extract text content from a web page.

    Args:
        url: URL of the web page to extract content from.

    Returns:
        str: Extracted text content from the web page.
    """
    try:
        response = httpx.get(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0'
            },
            timeout=10.0,
            follow_redirects=True,
        )

        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text().replace('\n', ' ').replace('\r', ' ').strip()
    except Exception as e:
        return f"Error fetching content: {str(e)}"












