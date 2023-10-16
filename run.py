
# run.py

# This module allows the user to input a Reddit URL and saves the HTML content to 'output.txt'.

# Input: Reddit URL entered by the user
# Output: 'output.txt' in 'Data/raw' directory
# Working: Takes a Reddit URL as input, downloads the HTML content using 'redditscrape', and saves it to 'output.txt'.

import RedditScrape.redditscrape as redditscrape
import os
import ExtractComments.extractcomments as extractcomments

if __name__ == "__main__":
    url = input("Enter the Reddit URL: ").strip()
    reddit_html = redditscrape.download_and_save_reddit_html(url)

    if reddit_html is not None:
        # Create 'Data/raw' directory if it doesn't exist
        raw_dir = 'Data/raw'
        if not os.path.exists(raw_dir):
            os.makedirs(raw_dir)

        with open(os.path.join(raw_dir, 'output.txt'), 'w', encoding='utf-8') as file:
            file.write(reddit_html)

        print("Reddit HTML content downloaded and saved to 'Data/raw/output.txt'")

    # Call the function to extract comments
    extractcomments.extract_comments()

    print("Comments extracted and saved to 'Data/processed/comments.txt'")



