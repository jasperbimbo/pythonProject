from selenium.webdriver.common.by import By


class STSTPage:

    def __init__(self, driver):
        driver.get("https://academy.testifyltd.com/courses/switch-to-software-testing")
        self.title = driver.find_element(By.TAG_NAME, 'h1')
        self.body = driver.find_element(By.TAG_NAME, 'h2')
        self.enrollNow_button = driver.find_element(By.TAG_NAME, 'button')