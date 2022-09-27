from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    button = browser.find_element(By.ID, "book")
    cost_label = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button.click()
    
    # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
    button = WebDriverWait(browser, 5).until_not(
            EC.element_to_be_clickable((By.ID, "verify"))
        )
        
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    
    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(y)
    
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
finally:
    time.sleep(10)
    browser.quit()