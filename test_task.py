import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
  browser = webdriver.Chrome()
  browser.get(link)

  # Дожидаемся, пока цена снизится до $100 (ждём до 12 секунд)
  price = WebDriverWait(browser, 12).until(
      EC.text_to_be_present_in_element((By.ID, "price"), "$100")
  )

  # Нажимаем на кнопку "Book"
  book_button = browser.find_element(By.ID, "book")
  book_button.click()

  # Считываем значение x для капчи
  x_element = browser.find_element(By.ID, "input_value")
  x = x_element.text

  # Считаем значение функции
  y = calc(x)

  # Вводим ответ в текстовое поле
  answer_input = browser.find_element(By.ID, "answer")
  answer_input.send_keys(y)

  # Нажимаем кнопку Submit
  submit_button = browser.find_element(By.ID, "solve")
  submit_button.click()

finally:
  # Задержка, чтобы успеть скопировать число из alert
  time.sleep(10)
  browser.quit()
