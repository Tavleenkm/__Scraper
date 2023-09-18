import os
import requests
from urllib.parse import urlparse

class HtmlDownloader:
    def __init__(self):
        self.output_dir = "html_files"
        os.makedirs(self.output_dir, exist_ok=True)

    def download_html_from_url(self, url):
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

            # Extract a filename from the path (e.g., "15hf4vr_egypt_changed_my_perspective_on_travel.html")
            filename = os.path.join(self.output_dir, parsed_url.path.lstrip('/').replace('/', '_') + '.html')
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(response.text)

            print(f"HTML content downloaded and saved to '{filename}'")
        except Exception as e:
            print(f"Error: {e}")
