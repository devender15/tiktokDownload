import string
import random
import datetime
from time import sleep
import requests
import os

# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



def getUniqueName():

    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    digits_chars =  string.digits

    # we will add all the characters in this array using extend function
    completeComboArray = []

    completeComboArray.extend(uppercase_chars)
    completeComboArray.extend(lowercase_chars)
    completeComboArray.extend(digits_chars)

    # just changing the order of all the chars so that every time they will be different
    random.shuffle(completeComboArray)

    random_chars = "".join(random.sample(completeComboArray, 15))

    # concatinating random_chars with current day

    current_time = datetime.datetime.now()
    uniqueName = current_time.strftime("%d%m%Y") + random_chars

    return uniqueName


def getVideoDownloadLink(videoLink):
    # url of the site from where it is going to download the video
    URL = "https://snaptik.app/en"

    # here is the link of the video which have to be downloaded
    VIDEO_URL = videoLink

    # adding chrome_options so that we can modify some changes
    chrome_options = Options()
    chrome_options.add_argument("--headless") # it will open the browser in background
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    # sending the request to the server
    driver.get(URL)
    sleep(2) # waiting for 1 second


    # selecting the inputBox
    inputBox = driver.find_element(By.XPATH, '/html/body/main/section[1]/div[3]/div/div/form/div[2]/input[1]')
    # pasting the link so that we can download
    inputBox.send_keys(
        VIDEO_URL)
    sleep(1)

    driver.find_element(By.XPATH, '/html/body/main/section[1]/div[3]/div/div/form/button').click()

    sleep(10)

    get_link = driver.find_element(
        By.XPATH, '/html/body/main/section[2]/div/div/article/div[2]/div/a[1]')

    link = get_link.get_attribute('href')

    driver.close() # closing the browser

    return link    

def downloadVideo(link, videoName):
        
    # now downloading the video file by sending the get request to the video url
    video_response = requests.get(link, stream=True)
    video_name = videoName + ".mp4" # naming a video file

    # creating a folder in which file will be downloaded
    if(not os.path.exists('videos')):
        os.mkdir('videos')

    # this is the actual path of the video file
    file_path = os.path.join('videos', video_name)

    with open(file_path, "wb") as f:
        for chunk in video_response.iter_content(chunk_size=1024):
            if(chunk):
                f.write(chunk)

        f.close()

    print("Video downloaded successfully")