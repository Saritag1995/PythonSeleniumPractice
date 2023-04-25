
import time

from behave import given, when, then

from Behave.lib.pages.AmazonHomePage import AmazonHomePage
from Behave.lib.pages.google_home.google_home_page import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *
from selenium.webdriver.common.keys import Keys
from Behave.lib.pages import *

use_step_matcher("re")

@given('the user opens google')
def open_google_website(context):
    context.browser.driver.get("https://www.amazon.com/")


@when('the user searches a product in search box (.*)')
def the_user_searches_a_product_in_search_box(context, search_string):
    driver = context.browser.driver
    wait = WebDriverWait(driver, timeout=2, poll_frequency=0.5)
    page = AmazonHomePage(context)

    msg = "google search field not displayed"
    search_field = wait.until(EC.element_to_be_clickable(page.productSearchField), msg)
    search_field.send_keys(search_string)
   # search_field.send_keys(Keys.ENTER)


@then('the user clicks on search button')
def the_user_clicks_on_search_button(context):
    driver = context.browser.driver
    wait = WebDriverWait(driver, timeout=2, poll_frequency=0.5)
    page = AmazonHomePage(context)

    msg = "Search button did not get clicked"
    wait.until(EC.element_to_be_clickable(page.productSearchButton), msg).click()


@when('user click on searched item')
def user_click_on_searched_item(context):
    driver = context.browser.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = GoogleHomePage(context)

    msg = "Product not displayed"
    #wait.until(EC.element_to_be_clickable(page.), msg).click()