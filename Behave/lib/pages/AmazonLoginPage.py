from selenium.webdriver.common.by import By
class AmazonLoginPg(object):
    def __init__(self, context=None):
        self.signInLink = (By.XPATH, "//span[text()='Account & Lists']")
        self.usernameField = (By.XPATH, "//input[@id='ap_email']")
        self.continueButton = (By.XPATH, "//input[@id='continue']")
        self.passwordField = (By.XPATH, "// input[ @ id = 'ap_password']")
        self.signInButton = (By.XPATH, "// input[ @ id = 'signInSubmit']")




