import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def send_keys_to_element(element, *keys):
    element.send_keys(keys)

def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.google.com")
    send_keys_to_element(driver.find_element(By.TAG_NAME, "input"), "Python", '\ue007')
    time.sleep(10)
    Search_Result = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div/div[1]/div/div/div')
    print("Wikipedia Result:", Search_Result.text)
    time.sleep(10)
    driver.close()



if __name__ == '__main__':
    main()