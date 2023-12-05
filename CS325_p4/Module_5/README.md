# Reddit Text Content Scraper

This Python program allows you to scrape HTML content from a Reddit post and its comments. The scraped HTML content is then saved to a text file.

## Prerequisites

Before running the program, ensure you have the following prerequisites installed:

- Python 3.7 or higher
- Conda 

## Clone the Repository

Clone this GitHub repository to your local machine:

git clone https://github.com/Tavleenkm/__Scraper

## Set Up Environment
Create a Conda environment and install the required packages from requirements.yaml:
conda env create -f requirements.yaml

## Add Reddit and OpenAI API Credentials
In the project directory, locate and open the config.py file. Add your Reddit API credentials (client ID, client secret, username, and password) to the file:


# In config.py
REDDIT_CLIENT_ID = "your_client_id"
REDDIT_CLIENT_SECRET = "your_client_secret"
REDDIT_USERNAME = "your_username"
REDDIT_PASSWORD = "your_password"

api_key = "your_api_key"

To use OpenAI for sentiment analysis, obtain an API key:

Visit OpenAI.
Sign up or log in.
Obtain your API key from the OpenAI dashboard.
In the project directory, in config.py paste your API key.


## Run the Main Program
Execute run.py in your command line or terminal:

python run.py

The program will access the 'urls.txt' file, scrape the HTML content of all the Reddit posts and their comments from the provided URLs, and save the information to a text file named 'output.txt' in the project directory.

## Extract Comments and Perform Sentiment Analysis
Comment extraction and sentiment analysis will be automatically triggered after scraping the Reddit content.

## Generate Plots
To generate sentiment analysis plots, run:

python plots.py
The program will create plots based on sentiment analysis data and save them in the folder Plots under Data Directory.

## Authors:

Tavleen Kaur

Chen Yang

## License

This project is licensed under the MIT License.


This README includes the instructions for cloning the repository, setting up the environment, adding Reddit API credentials, running the main program, and the automatic execution of comment extraction, sentiment analysis and ploting graphs using matplotlib and pandas libraries. 
