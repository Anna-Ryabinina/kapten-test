from behave import fixture, use_fixture
from selenium import webdriver


def before_scenario(context, scenario):
    print("Before scenario\n")
    context.browser = webdriver.Chrome('./chromedriver')
    context.browser.implicitly_wait(10)