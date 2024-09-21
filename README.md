# YouTube Comments Scraper

This Python project uses Selenium WebDriver to extract comments from a given YouTube video and save them to a text file. The script will scroll through the page to load more comments, retrieve the author and comment content, and store them in `youtube_comments.txt`.

## Features

- Fetches YouTube comments along with the author name.
- Saves the comments in a text file (`youtube_comments.txt`).
- Automatically scrolls down to load more comments.
- Option to run in headless mode for background execution.

## Requirements

- Python 3.x
- [Google Chrome](https://www.google.com/chrome/) (latest version)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) (corresponding version to your Chrome browser)

## Installation

1. Clone the repository or download the script.
2. Install the required Python packages using pip:
   ```bash
   pip install selenium
3. Run the script:
   ```bash
   python youtube-comments.py
4. Enter the URL of Video

Enjoy! 
