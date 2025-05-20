import requests
from bs4 import BeautifulSoup
import os
import time
import html
import re


def format_table(table):
    """Converts an HTML table to Markdown table format."""
    headers = []
    rows = []

    # Extract table headers
    header_row = table.find("tr")
    if header_row:
        headers = [th.get_text(strip=True) for th in header_row.find_all("th")]

    # Extract table rows
    for row in table.find_all("tr")[1:]:  # Skip the header row
        cells = [cell.get_text(strip=True) for cell in row.find_all(["td", "th"])]
        rows.append(cells)

    # Build Markdown table
    output = []
    if headers:
        output.append("| " + " | ".join(headers) + " |")
        output.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in rows:
        output.append("| " + " | ".join(row) + " |")
    return "\n".join(output)


def scrape_sequential_content(url):
    output = []
    try:
        # Send a GET request to the URL with a user agent to mimic a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract and print the page title
        title = soup.title.string.strip() if soup.title else "No title found"
        output.append(f"# {title}\n")

        # Find all relevant elements in the page in order of appearance
        elements = soup.find_all(["table", "h2", "h3", "p", "div"])

        skip_elements = (
            set()
        )  # Track all nested elements inside <div id="previewFrame">

        for element in elements:
            # Skip processing nested elements inside <div id="previewFrame">
            if element.name == "div" and element.get("id") == "previewFrame":
                output.append("```html")
                
                # Find the inner content div (second div inside previewFrame)
                inner_div = element.find('div', class_=lambda c: c and 'rounded-box' in c)
                
                if inner_div:
                    # Extract the content inside the inner div with proper formatting
                    content_elements = [child for child in inner_div.children if child.name]
                    content_html = ''
                    for child in content_elements:
                        # Preserve indentation and formatting
                        formatted_child = child.prettify()
                        # Remove the closing div tags from the output
                        content_html += formatted_child + '\n'
                else:
                    # Fallback to the content of the previewFrame div
                    content_elements = [child for child in element.children if child.name]
                    content_html = ''
                    for child in content_elements:
                        # Preserve indentation and formatting
                        formatted_child = child.prettify()
                        # Remove the closing div tags from the output
                        content_html += formatted_child + '\n'
                
                # Fix common encoding issues
                content_html = html.unescape(content_html)
                # Remove excessive whitespace but maintain indentation
                content_html = re.sub(r'\n\s*\n', '\n', content_html)
                
                # Add the cleaned HTML content
                output.append(content_html)
                output.append("```")
                
                skip_elements.update(
                    element.find_all(["p", "h2", "h3", "table"])
                )  # Track child elements
                continue

            # Skip any elements previously tracked as nested in <div id="previewFrame">
            if element in skip_elements:
                continue

            # Handle tables
            if element.name == "table":
                output.append("table:")
                output.append(format_table(element))  # Format table as Markdown
                output.append("")  # Add a blank line after table

            # Handle headers (h2)
            elif element.name == "h2":
                output.append("h2:")
                output.append(f"  - {element.get_text(strip=True)}")
                output.append("")  # Add a blank line after h2

            # Handle headers (h3)
            elif element.name == "h3":
                output.append("h3:")
                output.append(f"  - {element.get_text(strip=True)}")
                output.append("")  # Add a blank line after h3

            # Handle paragraphs with inline <code>
            elif element.name == "p":
                # Process inline <code> elements
                for code in element.find_all("code"):
                    code_text = (
                        f" {code.get_text(strip=True)} "  # Add spaces around the text
                    )
                    code.replace_with(code_text)  # Replace <code> tag with text

                # Get the complete text of the paragraph
                text = element.get_text(strip=True)
                if text:
                    # Fix common encoding issues
                    text = html.unescape(text)
                    output.append("p:")
                    output.append(f"  - {text}")
                    output.append("")  # Add a blank line after paragraph

    except requests.exceptions.RequestException as e:
        output.append(f"**An error occurred: {e}**\n")

    return "\n".join(output)


def get_doc_links(base_url):
    try:
        # Send a GET request to fetch the page content with a user agent
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()

        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all <a> tags with 'href' attribute
        links = soup.find_all("a", href=True)

        # Filter the links that start with "/docs"
        doc_links = [link["href"] for link in links if link["href"].startswith("/docs")]

        return doc_links
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve the webpage: {e}")
        return []


# Base URL for the website
base_url = "https://flyonui.com"

# URL for fetching document links
doc_links_url = "https://flyonui.com/components/"

# Get document links
doc_links = get_doc_links(doc_links_url)

# Create the directory for saving outputs if it doesn't exist
output_dir = "./docs"
os.makedirs(output_dir, exist_ok=True)

# Scrape each document link
for i, link in enumerate(doc_links):
    full_url = base_url + link
    print(f"Scraping ({i+1}/{len(doc_links)}): {full_url}")

    # Add a small delay between requests to avoid rate limiting
    if i > 0:
        time.sleep(1.5)  # 1.5 second delay between requests

    # Scrape the content sequentially
    scraped_content = scrape_sequential_content(full_url)

        # Determine the file name based on the link
    link_parts = link.strip("/").split("/")
    file_name = f"{link_parts[-1]}.txt"
    file_path = os.path.join(output_dir, file_name)

    # Save the scraped content to a text file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(scraped_content)

    print(f"Saved content to {file_path}")
    
    # Check if we've successfully scraped the content
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        print(f"✓ Successfully scraped {file_name}")
    else:
        print(f"✗ Failed to scrape content for {file_name}")
