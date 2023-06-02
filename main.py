from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)
driver.get('https://app.jubelio.com/login')
driver.implicitly_wait(15)

username = 'qa.rakamin.jubelio@gmail.com'
password = 'Jubelio123!'
product_name = 'Tws 198'
stock_product = '2'

input_username = wait.until(lambda drv: drv.find_element(By.NAME, 'email'))
input_username.send_keys(f'{username}')
input_password = wait.until(lambda drv: drv.find_element(By.NAME, 'password'))
input_password.send_keys(f'{password}')

button_login = wait.until(lambda drv: drv.find_element(By.XPATH, "//button[normalize-space()='Masuk']"))
button_login.click()

# time.sleep(2)
# text_dash = driver.find_element(By.XPATH, "//h1[contains(text(),'Selamat Datang')]")
# print(text_dash.text)
print("Login Success")

product_menu = wait.until(lambda drv: drv.find_element(By.XPATH, "//span[normalize-space()='Barang']"))
product_menu.click()
stock_menu = wait.until(lambda drv: drv.find_element(By.XPATH, "//span[normalize-space()='Persediaan']"))
stock_menu.click()

stock_button = wait.until(lambda drv: drv.find_element(By.XPATH, "//button[normalize-space()='Penyesuaian Persediaan']"))
stock_button.click()

# product_button = wait.until(lambda drv: drv.find_element(By.XPATH, "//span[normalize-space()='Harap pilih']"))
product_button = wait.until(lambda drv: drv.find_element(By.XPATH, "//span[@class='text-muted']"))
product_button.click()
action = ActionChains(driver)
action.double_click(on_element=product_button)
action.perform()

input_product = wait.until(lambda drv: drv.find_element(By.XPATH, "//input[@class='selectivity-search-input']"))
input_product.send_keys(f'{product_name}')

click_product = wait.until(
    lambda drv: drv.find_element(By.XPATH, "//div[@class='selectivity-result-item highlight']"))
click_product.click()

stock_column = wait.until(lambda drv: drv.find_element(
    By.XPATH, "//div[@id='page-wrapper']/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]"))
print(stock_column.text)
stock_column.click()
actionStock = ActionChains(driver)
actionStock.double_click(on_element=stock_column)
actionStock.perform()

stock_update = wait.until(lambda drv: drv.find_element(By.XPATH, "//input[@class=' editor-main']"))
stock_update.send_keys(f'{stock_product} {Keys.ENTER}')

save_button = wait.until(lambda drv: drv.find_element(By.XPATH, "//button[normalize-space()='Simpan']"))
save_button.click()
print("berhasil")
time.sleep(10)
