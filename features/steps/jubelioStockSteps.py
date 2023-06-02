from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

@when('Click on menu Barang and click on sub menu Persediaan')
def clickSidebar(context):
    product_menu = context.driver.find_element(By.XPATH, "//span[normalize-space()='Barang']")
    product_menu.click()
    stock_menu = context.driver.find_element(By.XPATH, "//span[normalize-space()='Persediaan']")
    stock_menu.click()

@when('Click on Penyesuaian Persediaan button')
def clickButtonStock(context):
    stock_button = context.driver.find_element(By.XPATH, "//button[normalize-space()='Penyesuaian Persediaan']")
    stock_button.click()

@when('Fill name product with "{product_name}" and fill stock product with "{stock_product}"')
def inputStock(context, product_name, stock_product):
    product_button = context.driver.find_element(By.XPATH, "//span[@class='text-muted']")
    product_button.click()
    action = ActionChains(context.driver)
    action.double_click(on_element=product_button)
    action.perform()

    input_product = context.driver.find_element(By.XPATH, "//input[@class='selectivity-search-input']")
    input_product.send_keys(f'{product_name}')

    click_product = context.driver.find_element(By.XPATH, "//div[@class='selectivity-result-item highlight']")
    click_product.click()

    stock_column = context.driver.find_element(By.XPATH,
        "//div[@id='page-wrapper']/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]")
    stock_column.click()
    actionStock = ActionChains(context.driver)
    actionStock.double_click(on_element=stock_column)
    actionStock.perform()

    stock_update = context.driver.find_element(By.XPATH, "//input[@class=' editor-main']")
    stock_update.send_keys(f'{stock_product} {Keys.ENTER}')

@when('Click on Simpan button')
def clickButtonSave(context):
    save_button = context.driver.find_element(By.XPATH, "//button[normalize-space()='Simpan']")
    save_button.click()

@then('User must successfully Update stock product')
def backToInventoryMenu(context):
    time.sleep(10)
    context.driver.close()
