from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class ItemPage(BasePage):
    title = (By.CSS_SELECTOR,".gwQYw h1")
    item_card = (By.CSS_SELECTOR,".grid.h-full a")
    price = (By.CSS_SELECTOR, ".cGFDG0.cB6nZL span")


    def get_page_title(self):
       return self.get_text(self.title,10)
    
    def item_cards(self):
        item_list = self.findall(self.item_card)
        return item_list
    
    def get_price(self):
        return self.get_clean_text(self.price)