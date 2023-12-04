# redditscrape.py

# This module provides functions to download and save Reddit HTML content.

# Input: Reddit URL
# Output: HTML content of the Reddit post and comments
# Working: Initializes a Reddit API instance, retrieves the HTML content, and combines it with comments.

import praw
import requests
from bs4 import BeautifulSoup
import Module_1.config as config
import praw.exceptions
import requests.exceptions
import time

def download_and_save_reddit_html(url):
    # Initialize a Reddit API instance
    reddit = praw.Reddit(
        client_id=config.REDDIT_CLIENT_ID,
        client_secret=config.REDDIT_CLIENT_SECRET,
        username=config.REDDIT_USERNAME,
        password=config.REDDIT_PASSWORD,
        user_agent="my_bot",
    )

    try:
        submission = reddit.submission(url=url)

        # Get the post's HTML content
        post_url = f"https://old.reddit.com{submission.permalink}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

        # Retry logic for making requests
        max_retries = 3
        retry_delay = 5  # in seconds

        for retry in range(max_retries):
            try:
                post_response = requests.get(post_url, headers=headers)
                post_response.raise_for_status()
                break  # Successful request, exit the loop
            except requests.exceptions.RequestException as e:
                print(f"Error for URL {url}: {e}")
                if retry < max_retries - 1:
                    print(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
       
        # Extract HTML content of comments
        comments_htmls = []
        comments = submission.comments.list()
        for comment in comments:
            if isinstance(comment, praw.models.Comment):
                comments_htmls.append(comment.body_html)

        # Combine post content and comments' HTML
        reddit_html = post_response.text + "\n\n" + "\n\n".join(comments_htmls)

        return reddit_html

    except praw.exceptions.PRAWException as e:
        print(f"PRAW Error for URL {url}: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Requests Error for URL {url}: {e}")
        return None

# Example usage:
reddit_url = 'https://www.reddit.com/r/your_subreddit/comments/your_post_id/your_post_title/'
result = download_and_save_reddit_html(reddit_url)
if result:
    print(result)
else:
    print("Failed to download and save Reddit HTML.")