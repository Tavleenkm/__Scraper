# analysis.py

import openai
import os
import csv
import Module_1.config as config

def perform_sentiment_analysis(comments_file_path):
    api_key = config.api_key
    openai.api_key = api_key

    data_directory = "Data"
    sentiments_folder = os.path.join(data_directory, "sentiments")
    os.makedirs(sentiments_folder, exist_ok=True)

    try:
        file_number = os.path.splitext(os.path.basename(comments_file_path))[0].replace("comments", "")
        sentiments_file_path = os.path.join(sentiments_folder, f"sentiments{file_number}.csv")

        with open(sentiments_file_path, mode='w', newline='', encoding='utf-8') as sentiments_file:
            sentiments_writer = csv.writer(sentiments_file)
            sentiments_writer.writerow(['Comment', 'Sentiment'])

            with open(comments_file_path, 'r', encoding='utf-8') as file:
                comments = file.readlines()

            analyzed_comments = 0

            for comment in comments:
                comment = comment.strip()
                if not comment:
                    continue  # Skip empty lines

                prompt = f"What is the sentiment: '{comment}'?"
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=prompt,
                    max_tokens=50,
                )
                sentiment = response.choices[0].text.strip()

                sentiments_writer.writerow([comment, sentiment])

                analyzed_comments += 1

                if analyzed_comments >= 50:
                    break

            print(f"Sentiments for {comments_file_path} saved to {sentiments_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Remove the following line if you want to keep the original function
# perform_sentiment_analysis()
