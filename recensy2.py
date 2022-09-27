from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    ...
    lnk = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
    lnk.send_keys("Ivan")
    lnk = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
    lnk.send_keys("Petrov")
    lnk = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/div[3]/input")
    lnk.send_keys("Moscov")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()