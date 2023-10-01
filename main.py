# main.py

import redditscrape

if __name__ == "__main__":
    url = input("Enter the Reddit URL: ").strip()
    reddit_html = redditscrape.download_and_save_reddit_html(url)

    if reddit_html is not None:
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(reddit_html)

        print("Reddit HTML content downloaded and saved to 'output.txt'")
