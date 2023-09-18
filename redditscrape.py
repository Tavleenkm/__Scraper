import os
import requests
from urllib.parse import urlparse

def download_html_from_url(url):
    # Add 'https://' prefix if missing
    if not urlparse(url).scheme:
        url = 'https://' + url

    # Add 'www' prefix if missing
    parsed_url = urlparse(url)
    if not parsed_url.netloc.startswith('www.'):
        url = parsed_url.scheme + '://www.' + parsed_url.netloc + parsed_url.path

    try:
        response = requests.get(url)
        response.raise_for_status()

        # Save the raw HTML content to a text file
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(response.text)

        print(f"HTML content downloaded and saved to 'output.txt'")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Enter the URL: ").strip()  # Prompt for the URL input
    download_html_from_url(url)