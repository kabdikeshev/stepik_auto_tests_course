from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    magic_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    magic_button.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    
    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(y)
    
    confirm_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    confirm_button.click()
    
    answer_alert = browser.switch_to.alert
    answer_alert_text = answer_alert.text
    print(answer_alert_text)    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()