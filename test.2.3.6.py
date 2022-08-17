# https://stepik.org/lesson/184253/step/6?unit=158843
# python C:\Users\Andrew\EDUCATION\Testing\STEPIK.Selenium.Python\Module2\test.2.1.5.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

    # читаем имя новой вкладки, которая открылась после нажатия прошлой кнопки. 
    # так как вкладки всего две, то новая очевидно будет под индексом 1, а стартовая 0.
    new_window = browser.window_handles[1]
    print(new_window)
    # переключаемся на новоую влкдаку
    browser.switch_to.window(new_window)

    x = browser.find_element(By.CSS_SELECTOR,"span#input_value").text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR,"input#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # выбор итогового кода, который нужно скопировать для решения теста
    s_alert = browser.switch_to.alert.text
    s_code = s_alert.find(": ")
    print(" ")
    print("<!!!> КОД ДЛЯ ВЫПОЛНЕНИЯ ЗАДАНИЯ: " + s_alert[s_code+2:])
    print(" ")

finally:
    # задержка чтобы успесть скопировать код для ответа
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла (зачем?)