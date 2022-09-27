from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    first_name = browser.find_element(By.CSS_SELECTOR, '[class*="first_block"] input[class*="first"]')
    last_name = browser.find_element(By.CSS_SELECTOR, '[class*="first_block"] input[class*="second"]')
    email = browser.find_element(By.CSS_SELECTOR, '[class*="first_block"] input[class*="third"]')
    phone = browser.find_element(By.CSS_SELECTOR, '[class*="second_block"] input[class*="first"]')
    address = browser.find_element(By.CSS_SELECTOR, '[class*="second_block"] input[class*="second"]')
    
    first_name.send_keys("First name")
    last_name.send_keys("Last name")
    email.send_keys("test@mail.com")
    phone.send_keys("123456784")
    address.send_keys("Boston, MA")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
