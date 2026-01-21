import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sauce-demo.myshopify.com/account/login")
def click_element(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    element.click()
def send_keys_to_element(driver, xpath, keys):
    element = driver.find_element(By.XPATH, xpath)
    element.clear()
    element.send_keys(keys)




# SignUp = "//a[contains(text(),'Sign up')]"
# click_element(driver, SignUp)
# print("Clicked on Sign up link")
#
# time.sleep(2)
#
# if "register" in driver.current_url:
#     print("Registration form loaded successfully")
# else:
#     print("Warning: Registration form may not have loaded properly - current URL:", driver.current_url)
# FirstName = "//input[@id='first_name']"
# send_keys_to_element(driver, FirstName, "Bibisha")
# print("First name entered")
# LastName = "//input[@id='last_name']"
# send_keys_to_element(driver, LastName, "thapa")
# print("Last name entered")
# Email = "//input[@id='email']"
#
# unique_email = f"testuser_{int(time.time())}@gmail.com"
# send_keys_to_element(driver, Email, unique_email)
# print("Email entered")
# Password = "//input[@id='password']"
# send_keys_to_element(driver, Password, "Bibisha@123")
# print("Password entered")
# CreateButton = "//input[@type='submit' and @value='Create']"
# click_element(driver, CreateButton)
# print("Clicked on Create button")
#
# time.sleep(5)


login_search_data = [
    #1's case
    {"email": "bibisha0301@gmail.com",
     "password": "Bibisha@123",
     "search_term": "product",
     },


]
print("\nPerforming login and search tests...")

for i, user_data in enumerate(login_search_data):
    driver.get("https://sauce-demo.myshopify.com/account/login")
    time.sleep(5)

# login_link = "//a[@id='customer_login_link']"
# click_element(driver, login_link)
# print("login link entered")
# time.sleep(5)
#
# email_input = "//input[@id='customer_email']"
# send_keys_to_element(driver, email_input, "bibisha0301@gmail.com")
# print("Email entered")
#
# password_input = "//input[@id='customer_password']"
# send_keys_to_element(driver, password_input, user_data["password"])
# print("Password entered")
# time.sleep(10)

  try:
      search_input

ddti