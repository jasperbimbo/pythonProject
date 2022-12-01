import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get(" https://www.bbc.com")
    New_1 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[1]/div/a')
    print("This is the 1th News Headline:", New_1.text)
    New_2 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[2]/div/a')
    print("\nThis is the 2th News Headline:", New_2.text)
    New_3 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[3]/div/a')
    print("\nThis is the 3th News Headline:", New_3.text)
    New_4 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[4]/div/a')
    print("\nThis is the 4th News Headline:", New_4.text)
    New_5 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[5]/div/a')
    print("\nThis is the 5th News Headline:", New_5.text)
    New_6 = driver.find_element(By.CSS_SELECTOR, '#page > section.module.module--content-block > div > div > div:nth-child(2) > div > section.module.module--news.module--collapse-images > div > ul > li.media-list__item.media-list__item--1 > div > a')
    print("\nThis is the 6th News Headline:", New_6.text)
    New_7 = driver.find_element(By.CSS_SELECTOR, '#page > section.module.module--content-block > div > div > div:nth-child(2) > div > section.module.module--news.module--collapse-images > div > ul > li.media-list__item.media-list__item--2 > div > a')
    print("\nThis is the 7th News Headline:", New_7.text)
    New_8 = driver.find_element(By.CSS_SELECTOR, '#page > section.module.module--content-block > div > div > div:nth-child(2) > div > section.module.module--news.module--collapse-images > div > ul > li.media-list__item.media-list__item--3 > div > a')
    print("\nThis is the 8th News Headline:", New_8.text)
    New_9 = driver.find_element(By.CSS_SELECTOR, '#page > section.module.module--content-block > div > div > div:nth-child(2) > div > section.module.module--sport.module--collapse-images > div > ul > li.media-list__item.media-list__item--1 > div > a')
    print("\nThis is the 9th News Headline:", New_9.text)
    New_10 = driver.find_element(By.CSS_SELECTOR, '#page > section.module.module--content-block > div > div > div:nth-child(2) > div > section.module.module--sport.module--collapse-images > div > ul > li.media-list__item.media-list__item--2 > div > a')
    print("\nThis is the 10th News Headline:", New_10.text)
    time.sleep(20)



if __name__ == '__main__':
    main()