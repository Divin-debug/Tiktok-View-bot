import os
from selenium import webdriver
from time import sleep 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from colorama import init, Fore, Style


init(autoreset=True)

def main():
    print(Style.BRIGHT + '''
---------- TikTok Views Bot ----------'''  + Fore.RED +
 "\n\n\n ---------- KyuStream.com ---------- \n ---------- https://github.com/Divin-debug ----------")

def getViews():
    sleep(2)
    try:
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div[1]/div[3]/div/div/button").click()
    except:
        print("Something went wrong")
        driver.refresh()
        getViews()

    try:
        sleep(2)
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/form/div/input").send_keys(videoURL)
        sleep(1)
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/form/div/div/button").click()
        sleep(1)
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div/div[1]/h5/button[2]").click()
        sleep(10)
        driver.refresh()
        print("____ Views Successfully sent! _____")
        sleep(600)
        getViews()
    except:
        print("Generic error occured. Trying again..")
        driver.refresh()
        sleep(30)
        getViews()

if __name__ == '__main__':
    main()

videoURL = input("\nInsert Tiktok Video URL : ")
chrome_options = Options()
chrome_options.add_argument('--incognito')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get("https://freer.es/")

getViews()

