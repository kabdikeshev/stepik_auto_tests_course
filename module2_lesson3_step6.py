from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    
    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(y)
    
    submit_button2 = browser.find_element(By.CSS_SELECTOR, "button[type='Submit']")
    submit_button2.click()
    
    answer_alert = browser.switch_to.alert
    answer_alert_text = answer_alert.text
    print(answer_alert_text)
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()