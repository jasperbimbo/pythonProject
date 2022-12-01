import time
from tasPage import TASPage
from ststPage import STSTPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    stst_page = STSTPage(driver)
    print(stst_page.title.text, stst_page.body.text)
    stst_page.enrollNow_button.click()
    tas_page = TASPage(driver)
    print(tas_page.title.text, tas_page.body.text)
    tas_page.enroll_button.click()
    time.sleep(20)


if __name__ == '__main__':
    main()