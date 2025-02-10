import requests
from bs4 import BeautifulSoup

def scrape_url(url: str) -> str:
    """
    Scrapes the main content from a Wikipedia page.

    Args:
        url (str): The URL to scrape.

    Returns:
        str: The main content of the page.

    Raises:
        Exception: If scraping fails due to network issues, invalid URLs, or other errors.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes (e.g., 404, 500)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract the main content of the page
        main_content = soup.find("div", {"id": "mw-content-text"})

        # Remove unwanted elements (e.g., tables, references, footnotes)
        for element in main_content.find_all(["table", "div", "span", "sup"]):
            element.decompose()

        # Extract text from the main content
        text = main_content.get_text(separator="\n")

        # Clean up the text (remove extra whitespace and empty lines)
        text = "\n".join([line.strip() for line in text.splitlines() if line.strip()])

        # Debug: Print the scraped content (optional)
        print(f"Scraped content from {url}:\n{text}")

        return text

    except requests.exceptions.RequestException as e:
        # Handle request-related errors (e.g., network issues, invalid URLs)
        raise Exception(f"Failed to scrape {url}: Request error - {str(e)}")

    except Exception as e:
        # Handle any other unexpected errors
        raise Exception(f"Failed to scrape {url}: {str(e)}")