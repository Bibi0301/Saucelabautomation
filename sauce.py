from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Helper function to click an element
def click_element(driver, xpath):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    element.click()


# Registration function
def signup(driver):
    print("Running registration test with unique email")

    # Navigate to the main page
    driver.get("https://sauce-demo.myshopify.com")
    time.sleep(2)

    # Click the Sign Up link
    sign_up_xpath = "//a[contains(text(),'Sign up')]"
    click_element(driver, sign_up_xpath)
    print("Clicked on Sign up link")
    time.sleep(2)

    # Check if registration page loaded
    if "register" in driver.current_url:
        print("Registration form loaded successfully")
    else:
        print("Warning: Registration form may not have loaded properly - current URL:", driver.current_url)

    # Fill out the registration form
    first_name = driver.find_element(By.ID, "FirstName")
    first_name.send_keys("Test")

    last_name = driver.find_element(By.ID, "LastName")
    last_name.send_keys("User")

    email = driver.find_element(By.ID, "Email")
    unique_email = f"testuser_{int(time.time())}@example.com"
    email.send_keys(unique_email)

    password = driver.find_element(By.ID, "Password")
    password.send_keys("TestPass@123")

    # Click the Create Account button
    create_button_xpath = "//button[contains(text(),'Create')]"
    click_element(driver, create_button_xpath)
    print("Clicked on Create Account button")
    time.sleep(2)

    # Verify registration success
    try:
        logout_element = driver.find_element(By.XPATH, "//a[contains(text(),'Log Out')]")
        if logout_element:
            print("Log Out element found — registration successful")
            return True
    except:
        print("Log Out element not found — registration may have failed")
        return False


# Main execution
if __name__ == "__main__":
    driver = webdriver.Chrome()

    print("Performing registration with unique email...")
    registration_success = signup(driver)

    if registration_success:
        print("Registration test passed ✅")
    else:
        print("Registration test failed ❌")

    # Example test data for login + search
    login_search_data = [
        {
            "email": "sumanaghimire45@gmail.com",
            "password": "Sumana@123",
            "search term": "grey shirt"
        },
        {
            "email": "testuser2@gmail.com",
            "password": "Password2@",
            "search term": "Stripped Top"
        },
        {
            "email": "testuser3@gmail.com",
            "password": "Password3#",
            "search term": "Noir Jacket"
        }
    ]

    driver.quit()