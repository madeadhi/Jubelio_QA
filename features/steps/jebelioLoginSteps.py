from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('Launch chrome browser')
def launchChrome(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    context.driver = webdriver.Chrome(options=options)

@when('I am on the www.app.jubelio.com Login Page')
def openLoginPage(context):
    context.driver.get('https://app.jubelio.com/login')
    context.driver.implicitly_wait(15)

@when('Fill email field with "{email}" and Fill password with "{password}"')
def fillField(context, email, password):
    input_username = context.driver.find_element(By.NAME, 'email')
    input_username.send_keys(email)
    input_password = context.driver.find_element(By.NAME, 'password')
    input_password.send_keys(password)

@when('Click on Masuk button')
def clickButton(context):
    button_login = context.driver.find_element(By.XPATH, "//button[normalize-space()='Masuk']")
    button_login.click()

@then('Home Page Jubelio should appear')
def openHomePage(context):
    try:
        time.sleep(2)
        text_dashboard = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Selamat Datang')]").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text_dashboard == "Selamat Datang":
        context.driver.close()
        assert False, "Test Passed"