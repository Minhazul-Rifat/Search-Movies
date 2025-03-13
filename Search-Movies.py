from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
from time import sleep
import tkinter as tk
from tkinter import simpledialog

# Create a pop-up window to ask for the movie name
root = tk.Tk()
root.withdraw()  # Hide the main Tkinter window
root.geometry("600x400")
name = simpledialog.askstring("Movie Search", "Enter the movie name:")

if not name:  # If user cancels or enters nothing, exit
    print("No movie name entered. Exiting...")
    exit()

urls = "http://10.16.100.244/"

# Initialize Chrome driver
driver = webdriver.Chrome()

try:
    driver.get(urls)
    driver.maximize_window()

    # Search for the movie
    search_box = driver.find_element(By.ID, "psearch")
    search_box.send_keys(name)
    pyautogui.press('down')
    sleep(1)
    pyautogui.press('enter')
    sleep(2)

    # Wait and click the movie link
    movie_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id=\"news-stories\"]/div[1]/div[2]/div/a"))
    )
    driver.execute_script("arguments[0].click();", movie_link)
    sleep(2)

    # Close disclaimer popup
    #driver.find_element(By.XPATH, "//*[@id=\"disclaimer\"]/div/div/div[1]/button").click()
    #sleep(1)

    # Click play/download link
    driver.find_element(By.XPATH, "/html/body/div[3]/main/div[2]/div[2]/div/a").click()

    # Click the three-dot menu button in the video player
    sleep(5)
    pyautogui.click(x=1865, y=915)
    sleep(0.5)

    # Press enter (if needed for confirmation)
    pyautogui.press('enter')
    sleep(1)

    # Open Downloads tab
    pyautogui.hotkey('ctrl', 'j')

    while True:
        sleep(1)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    input("Press Enter to close the browser...")
    driver.quit()
