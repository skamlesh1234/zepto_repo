from pages.basepage import BasePage
from selenium.webdriver.common.by import By
class Home_page(BasePage):
    signup_button = (By.XPATH, "//div[contains(text(),'Signup')]")
    cafe_button = (By.XPATH,"//button/span[contains(text(),'Cafe')]")
    
    def click_cafe_button(self):
        self.click(self.cafe_button,10)

