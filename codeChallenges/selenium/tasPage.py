from selenium.webdriver.common.by import By


class TASPage:

    def __init__(self, driver):
        driver.get("https://academy.testifyltd.com/courses/test-automation-simplified")
        self.title = driver.find_element(By.TAG_NAME, 'h1')
        self.body = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[1]/p')
        self.enroll_button = driver.find_element(By.TAG_NAME, 'button')

