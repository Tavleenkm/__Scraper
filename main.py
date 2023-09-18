from redditscrape import HtmlDownloader

if __name__ == "__main__":
    downloader = HtmlDownloader()
    url = input("Enter the URL: ").strip()
    downloader.download_html_from_url(url)

