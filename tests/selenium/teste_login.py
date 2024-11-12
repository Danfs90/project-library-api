from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_login():
    # Setup
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://localhost:5000/")
    
    try:
        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys("example@example.com.br")
        
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("password")
        
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        time.sleep(3)
                
    finally:

        time.sleep(15)
        driver.quit()

if __name__ == "__main__":
    test_login()
