import pytest
from selenium.webdriver.common.by import By
from pages.loginpage import LoginPage
from pages.homepage import Home_page
from pages.itemspage import ItemPage
from pages.cafepage import CafePage
from pages.basepage import BasePage

class TestLogin:


    # def test_login(self,driver):
    #     loginPage= LoginPage(driver)
    #     loginPage.login("andu",'pandu')
    #     title = loginPage.get_title()
    #     assert title == "title"
        
    def test_add_item_to_cart(self,driver):
        homepage = Home_page(driver)
        cafepage = CafePage(driver)
        itempage = ItemPage(driver)
        basepage = BasePage(driver)

        homepage.click_cafe_button()
        cafepage.click_newly_launched()
        title = itempage.get_page_title()
        print(title)
        assert title == "Coffee"
        elements = itempage.item_cards()
        print("length off item card is: ",len(elements))
        for e in elements:
            price_elm = e.find_element(By.CSS_SELECTOR, ".cGFDG0.cB6nZL span")
            price = e.itempage.get_price()
            print(price)  # 99





