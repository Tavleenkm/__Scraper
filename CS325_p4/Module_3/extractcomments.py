# extractcomments.py

# This module extracts comments from the 'output.txt' file and saves them to 'comments.txt'.

# Input: 'output.txt' in 'Data/raw' directory
# Output: 'comments.txt' in 'Data/processed' directory
# Working: Reads the 'output.txt' file, extracts comments using BeautifulSoup, and saves them to 'comments.txt'.

import os
from bs4 import BeautifulSoup

# Function to extract comments from text content
def extract_comments():
    with open(os.path.join('Data/raw', 'output.txt'), 'r', encoding='utf-8') as file:
        text_content = file.read()

    comments = []

    # Parse the text content as HTML using BeautifulSoup
    soup = BeautifulSoup(text_content, 'html.parser')

    # Find all <div> elements with class "md"
    comment_divs = soup.find_all('div', class_='md')

    for comment_div in comment_divs:
        # Find the <p> element within each <div>
        comment_text = comment_div.find('p')

        # Check if a <p> element was found
        if comment_text:
            comments.append(comment_text.get_text())

    # Create 'Data/processed' directory if it doesn't exist
    processed_dir = 'Data/processed'
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)

    # Write the extracted comments to comments.txt
    with open(os.path.join(processed_dir, 'comments.txt'), 'w', encoding='utf-8') as file:
        for comment in comments:
            file.write(comment + '\n')

    print("Comments extracted and saved to 'Data/processed/comments.txt'")