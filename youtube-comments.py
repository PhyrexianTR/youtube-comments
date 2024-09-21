from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# get comments
def get_youtube_comments(video_url):
    # webdriver
    options = webdriver.ChromeOptions()
    # background working? uncomment the line if you want to hide the process.
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    # open the youtube video
    driver.get(video_url)

    # Explicit wait
    try:
        # wait for comments
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "comments"))
        )
    except Exception as e:
        print("Yorum bölümü yüklenemedi:", e)
        driver.quit()
        return []

    # scroll down to the end of the page to load all the comments.(it can take forever due to the comments length.) // NEEDS TO BE IMPROVED
    # Unfortunately youtube loads the comments on demand so this is why we are trying to scroll to the bottom to load all the comments.
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    
    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(3)  # wait for a bit
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        
        if new_height == last_height:  # no comment? then we are at the end of the page.
            break
        last_height = new_height

        comments_data = driver.execute_script("""
            let comments = document.querySelectorAll('ytd-comment-thread-renderer');
            let commentList = [];
            comments.forEach((comment) => {
                let author = comment.querySelector('#author-text span').innerText; // comment author
                let commentText = comment.querySelector('#content-text').innerText; // comment content
                commentList.push({author: author, comment: commentText});
            });
            return commentList;
        """)

    driver.quit()  # kill

    return comments_data

# main function
if __name__ == "__main__":
    video_url = input("Youtube Video Link: ")
    comments = get_youtube_comments(video_url)

    # write the comments to any file
    if comments:
        with open("youtube_comments.txt", "w", encoding="utf-8") as file:
            for comment_data in comments:
                file.write(f"Author: {comment_data['author']}\nComment: {comment_data['comment']}\n\n")
        print(f"{len(comments)} comments have been fetched and saved to 'youtube_comments.txt' file.")
    else:
        print("No comments.")
