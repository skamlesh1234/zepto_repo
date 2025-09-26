from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import re
from selenium.webdriver.support  import expected_conditions as EC
class BasePage:
    def __init__(self,driver):
        self.driver = driver
    
    def find(self,locator,timeout =10):
        return WebDriverWait(self.driver,timeout=timeout).until(EC.presence_of_element_located(locator))
    
    def findall(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
        lambda d: d.find_elements(*locator)
    )
    
    def click(self,locator,timeout =10):
        self.find(locator,timeout).click()
    
    def type(self,locator,text,timeout=10):
        element = self.find(locator,timeout)
        element.clear()
        element.send_keys(text)
    
    def get_text(self,locator,timeout=10):
        return self.find(locator,timeout).text
    

    def get_clean_text(self, locator, timeout=10):
        text = self.find(locator, timeout).text
        return re.findall(r"\d+", text)[0]  # returns only digits as string

