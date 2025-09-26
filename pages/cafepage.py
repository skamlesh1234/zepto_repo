from pages.basepage import BasePage
from selenium.webdriver.common.by import By
class CafePage(BasePage):

    NEWLY_LAUNCHED = (By.CSS_SELECTOR,"a[aria-label='Newly Launched']")

    def click_newly_launched(self, timeout=10):
        """Clicks the 'Newly Launched' section on Cafe page."""
        self.click(self.NEWLY_LAUNCHED, timeout)