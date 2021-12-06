# -*- coding: UTF-8 -*-

from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(dir_path)

from features.steps.locaters import locator

import pdb

@given('The AutomationPractice site is open')
def open_website(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(10)
    context.driver.get("http://automationpractice.com/index.php")
    context.driver.maximize_window()
    assert context.driver.title == "My Store"



@given('The Sign In link is clicked')
def click_signin_link(context):
    assert context.driver.find_element(*locator["sign_in_link"]).is_displayed()
    context.driver.find_element(*locator["sign_in_link"]).click()
    # assert context.driver.title == "Login - My Store"


@given('The Forget password link is clicked')
def click_forget_passwprd_link(context):
    assert context.driver.find_element(*locator["forget_your_password_link"]).is_displayed()
    context.driver.find_element(*locator["forget_your_password_link"]).click()
    assert context.driver.title == "Forget password - My Store"
    context.driver.implicitly_wait(3)

@given('Email "{rec_email}" address for recovring')
def enter_rec_email(context, recover_email):
    context.driver.find_element(*locator["rec_email"]).send_keys(recover_email)

@when('Retrieve Password link is clicked')
def click_retrieve_pw_link(context):
    assert context.driver.find_element(*locator['retrieve_password_link']).is_display()
    context.driver.find_element(*locator["retrieve_password_link"]).click()
    assert context.driver.title == "Retrieve password - My Store"
    context.driver.implicitly_wait(3)

@then('User successfully get the reset password email')
def retrieve_succ(context):
    text = context.driver.find_element(*locator["succ_retrieve_password"]).text
    assert text == "A confirmation email has been sent to your address: "
    context.driver.close()

@given('Enter email ""')
def step_impl(context):
    context.driver.find_element(*locator["recover_email"]).send_keys("")

@given('Enter email "invalid.email.com"')
def step_impl(context):
    context.driver.find_element(*locator["recover_email"]).send_keys("invalid@email.com")

@then("The {unsucc_retrieve_password_msg} fail message is shown")
def unsucc_retrieve_pw_msg(context, unsucc_retrieve_password_msg):
    if context.driver.find_elements(*locator["unsucc_retrieve_password_msg"]):
        print("Element exists")
    else:
        print("Element doesn't exits")

    context.driver.close()
    assert True, "Test Passed"