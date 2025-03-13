from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from time import sleep

# User credentials
username = "Rifat_X"  # Replace with your username
password = "mirifat7"  # Replace with your password

# URL of the login page
login_url = "https://leetcode.com/accounts/login/"

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Open the login page
    driver.get(login_url)

    # Wait for the username field and input the username
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id_login"))
    ).send_keys(username)

    # Input the password
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id_password"))
    ).send_keys(password)

    # Access the shadow DOM for the checkbox
    shadow_host = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-live='polite']"))
    )
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
    if shadow_root:
        print("Shadow root accessed successfully.")
    else:
        raise Exception("Failed to access shadow root.")

    # Find the checkbox inside the shadow DOM
    checkbox = shadow_root.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
    if checkbox:
        print("Checkbox found.")

    # Click the checkbox using JavaScript
    driver.execute_script("arguments[0].click();", checkbox)
    print("Checkbox clicked.")

    # Wait for a moment to ensure checkbox is processed
    sleep(2)

    # Click the "Sign In" button
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "signin_btn"))
    )
    sign_in_button.click()
    print("Sign In button clicked.")

    # Wait to verify successful login (adjust the condition as needed)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "navbar-right"))
    )
    print("Login successful!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Keep the browser open for manual inspection or close it after pressing Enter
    input("Press Enter to close the browser...")
    driver.quit()
