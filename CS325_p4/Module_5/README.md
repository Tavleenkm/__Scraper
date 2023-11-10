Reddit Text Content Scraper
This Python program allows you to scrape HTML content from a Reddit post and its comments. The scraped HTML content is then saved to a text file.

Prerequisites
Before running the program, ensure you have the following prerequisites installed:

Python 3.7 or higher
Conda (for managing the environment, optional)
Usage
To use this program, follow these steps:

Clone the Repository

Clone this GitHub repository to your local machine:

in your shell git clone https://github.com/Tavleenkm/__Scraper

create a Conda environment and install the required packages from requirements.yaml: conda env create -f requirements.yaml

In the project directory, locate and open the config.py file. Add your Reddit API credentials (client ID, client secret, username, and password) to the file: In config.py

REDDIT_CLIENT_ID = "your_client_id"
REDDIT_CLIENT_SECRET = "your_client_secret"
REDDIT_USERNAME = "your_username"
REDDIT_PASSWORD = "your_password"
Run the main program by executing main.py in your command line or terminal: python main.py

Enter the Reddit URL when prompted. I used: https://old.reddit.com/r/travel/comments/15hf4vr/egypt_changed_my_perspective_on_travel/

The program will scrape the HTML content of the Reddit post and comments and save it to a text file named output.txt in the project directory.

Extracting Comments
To extract comments from the output.txt file, the extractcomments.py script uses regular expressions to match comment patterns. If the comments are found, they are saved to the comments.txt file.

Sentiment Analysis
Generate your OpenAI API key and update the api_key in the Config/config.py file.

Install the OpenAI Python package:

pip install openai==0.28
Run the sentiment analysis script by executing analysis.py:

python analysis.py
The sentiment analysis results will be saved to a CSV file in the Data/Sentiments directory.

Authors
Tavleen Kaur
Chen Yang

License
This project is licensed under the MIT License.
