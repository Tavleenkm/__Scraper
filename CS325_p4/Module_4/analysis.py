import openai
import os
import csv
import Module_1.config as config  # Assuming your config module is named 'config.py'

def perform_sentiment_analysis():
    # Set your OpenAI API key from the config module
    api_key = config.api_key

    # Initialize the OpenAI library
    openai.api_key = api_key

    # Define the path to the comments.txt file in the 'processed' directory
    comments_file_path = os.path.join("Data", "processed", "comments.txt")

    # Create a "Sentiments" folder if it doesn't exist
    sentiments_folder = os.path.join("Data", "Sentiments")
    os.makedirs(sentiments_folder, exist_ok=True)

    # Define the path for the CSV file to store sentiments
    sentiments_file_path = os.path.join(sentiments_folder, "sentiments.csv")

    try:
        # Open the CSV file for writing with 'utf-8' encoding
        with open(sentiments_file_path, mode='w', newline='', encoding='utf-8') as sentiments_file:
            sentiments_writer = csv.writer(sentiments_file)

            # Write the header row to the CSV file
            sentiments_writer.writerow(['Comment', 'Sentiment'])

            # Read comments from the comments.txt file with UTF-8 encoding
            with open(comments_file_path, 'r', encoding='utf-8') as file:
                comments = file.readlines()

            # Analyze the sentiment of the first 50 non-empty comments and write to the CSV file
            analyzed_comments = 0  # Counter for analyzed comments

            for comment in comments:
                comment = comment.strip()
                if not comment:
                    continue  # Skip empty lines
                prompt = f"What is the sentiment of the sentence: '{comment}'?"
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=prompt,
                    max_tokens=50,
                )
                sentiment = response.choices[0].text.strip()

                # Write the comment and sentiment to the CSV file
                sentiments_writer.writerow([comment, sentiment])

                analyzed_comments += 1
                if analyzed_comments >= 50:
                    break

        print(f"Sentiments for the first 50 comments saved to {sentiments_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle the error appropriately, e.g., logging or reporting the error