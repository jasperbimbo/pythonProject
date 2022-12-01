import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



def print_element_fields(element):
    print("\nText", element.text)

def print_element_properties(element):
    print("\nText Length:", element.get_property("text_length"))

def print_element_attributes(element):
    print("\nID:", element.get_attribute("id"))
    print("Class:", element.get_attribute("class"))
    print("Style:", element.get_attribute("style"))
    print("Inner Text:", element.get_attribute("innerText"))
    print("Inner HTML:", element.get_attribute("innerHTML"))



def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com")
    element = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]')
    print_element_fields(element)
    print_element_properties(element)
    print_element_attributes(element)






if __name__ == '__main__':
    main()



