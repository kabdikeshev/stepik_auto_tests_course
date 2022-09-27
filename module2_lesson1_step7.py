from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    
    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(y)
    
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()
    
    browser.execute_script("window.scrollBy(0, 100);")
    
    robot_radio_button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robot_radio_button.click()
    
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='Submit']")
    submit_button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()