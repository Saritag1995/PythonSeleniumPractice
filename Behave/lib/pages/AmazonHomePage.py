from selenium.webdriver.common.by import By
class AmazonHomePage(object):
    def __init__(self, context=None):
        self.productSearchField = (By.XPATH, "//input[@id='twotabsearchtextbox']")
        self.productSearchButton = (By.XPATH, "//input[@id='nav-search-submit-button']")

        self.gmail_link = (By.XPATH, "//a[text()='Gmail']")
        self.image_link = (By.XPATH, "//a[@class='gb_d' and text() = 'Images']")
