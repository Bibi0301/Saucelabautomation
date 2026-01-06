import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://accounts.saucelabs.com/am/XUI/#login/")

# wait = WebDriverWait(driver, 10)
# username=wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
# username.send_keys("standard_user")
#
# wait = WebDriverWait(driver, 10)
# password=wait.until(EC.visibility_of_element_located((By.ID,"password")))
# password.send_keys("secret_sauce")
#
# wait = WebDriverWait(driver, 5)
# login= wait.until(EC.visibility_of_element_located((By.ID,"login-button"))).click()

time.sleep(5)
driver.quit()
