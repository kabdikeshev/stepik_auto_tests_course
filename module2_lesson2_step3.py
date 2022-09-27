from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = x_element.text
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = y_element.text
    summa = int(x) + int(y)
    
    select = Select(browser.find_element(By.CSS_SELECTOR, "select#dropdown"))
    select.select_by_value(str(summa))
    
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='Submit']")
    submit_button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()