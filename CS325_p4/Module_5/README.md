# Reddit Text Content Scraper

This Python program allows you to scrape HTML content from a Reddit post and its comments. The scraped HTML content is then saved to a text file.

## Prerequisites

Before running the program, ensure you have the following prerequisites installed:

- Python 3.7 or higher
- Conda (for managing the environment, optional)

## Usage

### 1. Clone the Repository

Clone this GitHub repository to your local machine:

git clone https://github.com/Tavleenkm/__Scraper

2. Set Up Environment
Create a Conda environment and install the required packages from requirements.yaml:
conda env create -f requirements.yaml

3. Add Reddit API Credentials
In the project directory, locate and open the config.py file. Add your Reddit API credentials (client ID, client secret, username, and password) to the file:

# In config.py
REDDIT_CLIENT_ID = "your_client_id"
REDDIT_CLIENT_SECRET = "your_client_secret"
REDDIT_USERNAME = "your_username"
REDDIT_PASSWORD = "your_password"
4. Run the Main Program
Execute main.py in your command line or terminal:

python run.py
Enter the Reddit URL when prompted. Example URL: https://old.reddit.com/r/travel/comments/15hf4vr/egypt_changed_my_perspective_on_travel/

The program will scrape the HTML content of the Reddit post and comments, saving it to a text file named output.txt in the project directory.

5. Extract Comments and Perform Sentiment Analysis
Comment extraction and sentiment analysis will be automatically triggered after scraping the Reddit content.

Authors
Tavleen Kaur
Chen Yang

License
This project is licensed under the MIT License.


This README includes the instructions for cloning the repository, setting up the environment, adding Reddit API credentials, running the main program, and the automatic execution of comment extraction and sentiment analysis. 
