# https://stepik.org/lesson/165493/step/7?unit=140087
# python C:\Users\Andrew\EDUCATION\Testing\STEPIK.Selenium.Python\Module2\test.2.1.7.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "img#treasure").get_attribute("valuex")
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    # Заполняем поле мат ответом, выбираем чекбокс/радио и кликаем на кнопку отправить
    browser.find_element(By.CSS_SELECTOR,"input#answer").send_keys(y)

    browser.find_element(By.CSS_SELECTOR,"input#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR,"input#robotsRule").click()
    browser.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

finally:
    # задержка чтобы успесть скопировать код для ответа
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла (зачем?)