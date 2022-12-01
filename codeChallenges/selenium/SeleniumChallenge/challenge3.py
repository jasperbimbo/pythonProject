import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://weather.com")
    Current_Weather_Result = driver.find_element(By.XPATH, '//*[@id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034"]/div/section/div/div[2]')
    print("This is the Current Weather:", Current_Weather_Result.text)
    Morning_Weather = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"]/section/div/ul/li[1]/a')
    print("\nThis is the Morning Weather:", Morning_Weather.text)
    Afternoon_Weather = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"]/section/div/ul/li[2]/a')
    print("\nThis is the Afternoon Weather:", Afternoon_Weather.text)
    Evening_Weather = driver.find_element(By.CSS_SELECTOR, '#WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a > section > div > ul > li:nth-child(3) > a')
    print("\nThis is the Evening Weather:", Evening_Weather.text)
    Overnight_Weather = driver.find_element(By.CSS_SELECTOR, '#WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a > section > div > ul > li:nth-child(4) > a')
    print("\nThis is the Overnight Weather:", Overnight_Weather.text)
    time.sleep(20)



if __name__ == '__main__':
    main()
