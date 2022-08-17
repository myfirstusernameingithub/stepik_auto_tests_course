# 
# python C:\Users\Andrew\EDUCATION\Testing\STEPIK.Selenium.Python\Module2\test.2.1.5.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")

    

    # выбор итогового кода, который нужно скопировать для решения теста
    s_alert = browser.switch_to.alert.text
    s_code = s_alert.find(": ")
    print(" ")
    print("<!!!> КОД ДЛЯ ВЫПОЛНЕНИЯ ЗАДАНИЯ: " + s_alert[s_code+2:])
    print(" ")

finally:
    # задержка чтобы успесть скопировать код для ответа
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла (зачем?)