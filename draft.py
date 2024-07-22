from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.7x.ae/")

WebDriverWait(driver, 60).until(
    lambda driver: driver.execute_script("return document.readyState") == "complete"
)

menu = driver.find_element(By.XPATH,"//img[@alt='Open Menu']")
menu.click()
time.sleep(1)
wait = WebDriverWait(driver,600)
portfolio_xpath = "//a[@href='/portfolio']"
portfolio_menu = wait.until(EC.presence_of_element_located((By.XPATH,portfolio_xpath)))
actions = ActionChains(driver)
actions.move_to_element(portfolio_menu).perform()

emirates_post_porfolio = driver.find_element(By.XPATH,"//a[@href='/portfolio#emiratespost']")
emirates_post_porfolio.click()
time.sleep(1)
emirates_post = driver.find_element(By.XPATH,"//a[@href='https://www.emiratespost.ae/']")
emirates_post.click()

close_banner = driver.find_element(By.XPATH,"//button[@aria-label='Close']")
close_banner.click()

login_btn = driver.find_element(By.LINK_TEXT,"Log in / Register")
login_btn.click()
time.sleep(5)

window_handles = driver.window_handles
driver.switch_to.window(window_handles[-1])

username = driver.find_element(By.ID,"b4-Input_Username")
username.send_keys("Testuser1")

password = driver.find_element(By.ID,"b4-Input_Password")
password.send_keys("wrongpass")

login = driver.find_element(By.ID,"b4-b12-Primary")
login.click()
time.sleep(5)
actual_error_message_ID = "b4-b9-ErrorMessage"
error_login_element = driver.find_element(By.ID,"b4-b9-ErrorMessage")
error_message = error_login_element.text
expected_error_message= "Invalid username or password."
assert error_message==expected_error_message, f"Expected: {expected_error_message}, but got {error_message}"



