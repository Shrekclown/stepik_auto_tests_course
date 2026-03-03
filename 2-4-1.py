from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    print("Страница открыта")

    # Ждем, пока цена не станет равной $100
    # text_to_be_present_in_element проверяет, что текст элемента содержит указанное значение
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    print("Цена достигла $100! Бронируем...")

    # Нажимаем кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()
    print("Кнопка Book нажата")

    # --- Решение математической задачи (как в предыдущих шагах) ---
    # Ждем появления элемента с x
    x_element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "input_value"))
    )
    x = x_element.text
    print(f"x = {x}")

    # Вычисляем y
    y = calc(x)

    # Вводим ответ
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Отмечаем чекбокс
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Выбираем радиокнопку
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    print("Форма отправлена")

    # Получаем код из алерта
    alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
    alert_text = alert.text
    print(f"КОД ДЛЯ ОТВЕТА: {alert_text}")
    alert.accept()

finally:
    time.sleep(10)
    browser.quit()