# run.py

# This module serves as the main entry point for the Reddit Text Content Scraper project. It allows the user to input a Reddit URL, and then performs the following tasks:

# 1. Downloads the HTML content of the Reddit post and its comments using the 'redditscrape' module.
# 2. Saves the raw HTML content to 'output.txt' in the 'Data/raw' directory.
# 3. Initiates sentiment analysis on the extracted comments using the 'analysis' module ('analysis.py').

# Requirements:
# - 'redditscrape' module for downloading HTML content.
# - 'analysis' module for sentiment analysis.
# - Ensure Reddit API credentials and OpenAI API key is set in the 'Config' module.

# Usage:
# 1. Run this script and enter a Reddit URL when prompted.
# 2. The program will download the HTML content and save it to 'output.txt'.
# 3. Sentiment analysis will be performed on the comments using 'analysis.py'.

import os
import Module_2.redditscrape as redditscrape
import Module_3.extractcomments as extractcomments
import Module_4.analysis as analysis
def main():
    url = input("Enter the Reddit URL: ").strip()
    reddit_html = redditscrape.download_and_save_reddit_html(url)

    if reddit_html is not None:
        # Get the current working directory
        current_directory = os.getcwd()

        # Create 'Data/raw' directory if it doesn't exist
        raw_dir = os.path.join(current_directory, 'Data', 'raw')
        if not os.path.exists(raw_dir):
            os.makedirs(raw_dir)

        # Save the 'output.txt' file in the 'Data/raw' directory
        with open(os.path.join(raw_dir, 'output.txt'), 'w', encoding='utf-8') as file:
            file.write(reddit_html)

        print("Reddit HTML content downloaded and saved to 'Data/raw/output.txt'")
        # Extract comments from the output.txt file
        extractcomments.extract_comments()

        # Perform sentiment analysis on the extracted comments
        analysis.perform_sentiment_analysis()

if __name__ == "__main__":
    main()
