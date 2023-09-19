# Reddit Scraper

This is a simple Reddit scraper program that allows you to download the text content of a web page by providing a URL.

## Features

- Downloads text content from a given URL.
- Saves the content to a text file.
- Supports URLs with or without "https://" or "www."
 
## Installation

1. Clone the repository to your local machine:

git clone https://github.com/Tavleenkm/__Scraper
Navigate to the project directory:


cd _scraper
Create and activate a Conda environment:

conda create -n my_project_env python=3.8
conda activate my_project_env
Install the required libraries:


pip install requests beautifulsoup4

Usage
Run the program by providing a URL as an argument:

python main.py 
it will ask for url
type the url
I gave reddit.com/r/travel/comments/15hf4vr/egypt_changed_my_perspective_on_travel/

The program will download the text content of the URL and save it to a file named output.txt in the same directory.

Example output.txt file is added. 

Examples
Download content from a Reddit page:


python web_scraper.py https://www.reddit.com/r/travel/comments/15hf4vr/egypt_changed_my_perspective_on_travel/

Export Conda Environment
To export the Conda environment to a YAML file:

conda env export --name my_project_env > requirements.yaml

Contributing
If you'd like to contribute to this project, please open an issue or submit a pull request on GitHub.



