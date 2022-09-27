from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    
    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(y)
    
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()
    
    robot_radio_button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robot_radio_button.click()
    
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='Submit']")
    submit_button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()