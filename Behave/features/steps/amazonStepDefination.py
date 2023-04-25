import time

from behave import given, when, then

from Behave.lib.pages.AmazonLoginPage import AmazonLoginPg
from Behave.lib.pages.google_home.google_home_page import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expectedConditions
from behave import *
from selenium.webdriver.common.keys import Keys

use_step_matcher("re")

@given('the user enters url')
def open_amazon_website(context):
    context.browser.driver.get("https://www.amazon.com/")


@when('clicks on sign in link')
def clicks_on_sign_in_link(context):
    driver = context.browser.driver
    wait = WebDriverWait(driver, timeout=2, poll_frequency=0.5)
    page = AmazonLoginPg(context)

    msg = "google sign in link not displayed"
    signInLink = wait.until(expectedConditions.element_to_be_clickable(page.signInLink), msg)
    signInLink.click();

@Then('user enter username and password (.*)(.*)')
def user_enter_username_and_password(context, username_string, password_string):
    driver = context.browser.driver
    wait = WebDriverWait(driver, timeout=2, poll_frequency=0.5)
    page = AmazonLoginPg(context)

    msg = "google search field not displayed"
    usernameField = wait.until(expectedConditions.element_to_be_clickable(page.usernameField))
    usernameField.send_keys(username_string)

    passwordField = wait.until(expectedConditions.element_to_be_clickable(page.passwordField))
    passwordField.send_keys(password_string)

@Then('user clicks on sign in button')
def user_clicks_on_sign_in_button(context):
    driver = context.browser.driver
    wait = WebDriverWait(driver, timeout=2, poll_frequency=0.5)
    page = AmazonLoginPg(context)
    signInButton = wait.until(expectedConditions.element_to_be_clickable(page.signInButton))
    signInButton.click();