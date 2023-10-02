from bs4 import BeautifulSoup

# Function to extract comments from text content
def extract_comments(text):
    comments = []

    # Parse the text content as HTML using BeautifulSoup
    soup = BeautifulSoup(text, 'html.parser')

    # Find all <div> elements with class "md"
    comment_divs = soup.find_all('div', class_='md')

    for comment_div in comment_divs:
        # Find the <p> element within each <div>
        comment_text = comment_div.find('p')

        # Check if a <p> element was found
        if comment_text:
            comments.append(comment_text.get_text())

    return comments

# Read the text content from the file (ouput.txt)
with open('output.txt', 'r', encoding='utf-8') as file:
    text_content = file.read()

# Try to extract comments
extracted_comments = extract_comments(text_content)

# Write the extracted comments to comments.txt
with open('comments.txt', 'w', encoding='utf-8') as file:
    for comment in extracted_comments:
        file.write(comment + '\n')

print("Comments extracted and saved to 'comments.txt'")
