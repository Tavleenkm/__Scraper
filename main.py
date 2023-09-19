import os
from redditscrape import download_html_from_url

if __name__ == "__main__":
    url = input("Enter the URL: ").strip()  # Prompt for the URL input
    html_content = download_html_from_url(url)

    if html_content is not None:
        # Save the raw HTML content to a text file
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(html_content)

        print("HTML content downloaded and saved to 'output.txt'")
