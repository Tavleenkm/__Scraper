from redditscrape import HtmlDownloader

if __name__ == "__main__":
    url = input("Enter the URL: ").strip()  # Prompt for the URL input
    downloader = HtmlDownloader()
    downloader.download_html_from_url(url)
