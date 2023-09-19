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

        return response.text
    except Exception as e:
        print(f"Error: {e}")
        return None
