import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com")
    locate_by_XPATH(driver)
    locate_by_css_selector(driver)



def locate_by_XPATH(driver):
    explore_courses = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[1]/div/button')
    print("XPATH-Explore Courses:", explore_courses)
    element_subscribe = driver.find_element(By.CSS_SELECTOR, "#__next > main > section.relative.bg-\[\#FCFCFC\].dark\:bg-\[\#013069\].pt-16.md\:pt-20.lg\:pt-28.pb-24.md\:pb-28.lg\:pb-32.xl\:pb-36 > div > div > div.w-full.md\:w-5\/12.xl\:w-4\/12 > h2")
    print("XPATH-Element with Subscribe:", element_subscribe)


def locate_by_css_selector(driver):
    explore_courses = driver.find_element(By.CSS_SELECTOR, "#__next > main > section.relative.bg-primary.dark\:bg-\[\#013069\] > div > div > div:nth-child(1) > div > button")
    print("CssSelector-Explore Courses:", explore_courses)
    element_subscribe = driver.find_element(By.CSS_SELECTOR, "#__next > main > section.relative.bg-\[\#FCFCFC\].dark\:bg-\[\#013069\].pt-16.md\:pt-20.lg\:pt-28.pb-24.md\:pb-28.lg\:pb-32.xl\:pb-36 > div > div > div.w-full.md\:w-5\/12.xl\:w-4\/12 > h2")
    print("CssSelector-Element with Subscribe:", element_subscribe)




if __name__ == '__main__':
    main()





