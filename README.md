# Reddit Text Content Scraper

This Python program allows you to scrape HTML content from a Reddit post and its comments. The scraped HTML content is then saved to a text file.

### Prerequisites

Before running the program, ensure you have the following prerequisites installed:

- Python 3.7 or higher
- Conda (for managing the environment, optional)

## Usage

To use this program, follow these steps:

1. **Clone the Repository**

   Clone this GitHub repository to your local machine:

   in your shell
   git clone https://github.com/Tavleenkm/__Scraper

2. create a Conda environment and install the required packages from requirements.yaml:
conda env create -f requirements.yaml

3.In the project directory, locate and open the config.py file. Add your Reddit API credentials (client ID, client secret, username, and password) to the file:
   In config.py
   REDDIT_CLIENT_ID = "your_client_id"
   REDDIT_CLIENT_SECRET = "your_client_secret"
   REDDIT_USERNAME = "your_username"
   REDDIT_PASSWORD = "your_password"

4. Run the main program by executing main.py in your command line or terminal:
python main.py

5. Enter the Reddit URL when prompted.
I used:
https://www.reddit.com/r/travel/comments/15hf4vr/egypt_changed_my_perspective_on_travel/

6. The program will scrape the HTML content of the Reddit post and comments and save it to a text file named output.txt in the project directory.

## Extracting Comments
To extract comments from the output.txt file, the extractcomments.py script uses regular expressions to match comment patterns. If the comments are found, they are saved to the comments.txt file.

## Author:
Tavleen Kaur

## License:
This project is licensed under the MIT License.

This README provides instructions for setting up and running your Reddit text content scraper project.

