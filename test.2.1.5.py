# https://stepik.org/lesson/165493/step/5?unit=140087
# python C:\Users\Andrew\EDUCATION\Testing\STEPIK.Selenium.Python\Module2\test.2.1.5.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # собираем число из элемента
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    # делаем расчёты с учетом выбранного элемента
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