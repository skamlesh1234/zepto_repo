from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.basepage import BasePage

class LoginPage(BasePage):
    USERNAME =(By.XPATH,'USERNAME')
    PASSWORD =(By.XPATH,'PASSWORD')
    Login_TITLE = (By.XPATH,'Tittle')
    LOGIN_BUTTON =(By.XPATH,'LOGIN')

    def login(self,username,password):
        self.type(self.USERNAME,username)
        self.type(self.PASSWORD,password)
        self.click(self.LOGIN_BUTTON)

    def get_title(self):
        self.get_text(self.Login_TITLE)

