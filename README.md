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
Download the appropriate version of ChromeDriver for your system:
ChromeDriver Downloads
Extract the chromedriver executable and place it in your system's PATH, or specify the path in the script.
Usage
Run the script:

bash
python youtube-comments.py
Enter the YouTube video URL when prompted.

The script will scrape the comments and save them to a file named youtube_comments.txt in the same directory.

Optional: Headless Mode
To run the script in the background (without opening a Chrome window), uncomment the following line in the code:

python
# options.add_argument("--headless")
Notes

Scroll Limitation: The script scrolls down to load more comments until it reaches the bottom of the page. For very long comment sections, it might take longer to load all comments.
Explicit Wait: The script uses an explicit wait to ensure that the comments section is loaded before scraping begins.
Troubleshooting
Chromedriver not found: Ensure the chromedriver is in your system’s PATH or specify the path to it in the script.
Page Not Loading: Make sure the video URL is valid and that you have a stable internet connection.
