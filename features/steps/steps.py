import time
from selenium.webdriver.support.select import By
from behave import *

from src.authorization.PersonalInfoPage import PersonalInfoPage
from src.authorization.SignInPage import SignInPage
from src.authorization.SignUpPage import SignUpPage


@given(u'user opens signup page')
def step_impl(context):
    context.browser.get('https://welcome.kapten.com/')
    context.signup_page = SignUpPage(context.browser)


@when(u'user sign up with new valid credentials')
def step_impl(context):

    '''Generate new unique test data'''

    test_email = 'autotest' + str(time.time()) + '@test.com'
    test_phone_number = '06' + str(time.time()).replace('.', '')[2:10]

    context.signup_page\
        .enter_email(test_email)\
        .enter_password('Qwe123456')\
        .click_signup()
    context.personal_info_page = PersonalInfoPage(context.browser)
    context.personal_info_page\
        .enter_first_name('Automation name')\
        .enter_last_name('Automation name')\
        .enter_phone_number(test_phone_number)\
        .click_signup()


@then(u'"{path}" is in url')
def step_impl(context, path):
    assert path in context.browser.current_url


@then(u'user is registered')
def step_impl(context):

    '''This is simple temporary solution specifically for the test assignment.
    Usually I hide location of an element and methods such as is_element_visible() in separate class,
    according to Page Object pattern'''

    assert context.browser.find_element(By.XPATH, '//*[@id="root"]/div/header/div/button/div/div').is_displayed()


@then(u'user is logged in')
def step_impl(context):
    assert context.browser.find_element(By.LINK_TEXT, "Automation name Automation name").is_displayed()


@given(u'user opens signin page')
def step_impl(context):
    context.browser.get('https://welcome.kapten.com/signin')
    context.signin_page = SignInPage(context.browser)


@then(u'user is not logged in')
def step_impl(context):
    elements = context.browser.find_elements(By.LINK_TEXT, "Automation name Automation name")
    assert len(elements) == 0


@then(u'user sees error message')
def step_impl(context):
    assert context.signin_page.is_error_message_displayed()


@when(u'user sign in with "{email}" email and "{password}" password')
def step_impl(context, email, password):
    context.signin_page\
        .enter_email(email)\
        .enter_password(password)\
        .click_continue()





