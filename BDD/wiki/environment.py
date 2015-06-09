from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def before_all(context):
    context.browser = webdriver.Firefox()
    context.Keys = Keys

def after_all(context):
    context.browser.quit()