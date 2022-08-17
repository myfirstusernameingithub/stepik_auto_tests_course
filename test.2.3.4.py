# https://stepik.org/lesson/184253/step/4?unit=158843
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    browser.switch_to.alert.accept()

    x = browser.find_element(By.CSS_SELECTOR,"span#input_value").text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR,"input#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    
    # выбор итогового кода, который нужно скопировать для решения теста
    s_alert = browser.switch_to.alert.text
    s_code = s_alert.find(": ")
    print("<!!!> КОД ДЛЯ ВЫПОЛНЕНИЯ ЗАДАНИЯ: " + s_alert[s_code+2:])

finally:
    # задержка чтобы успесть скопировать код для ответа
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла (зачем?)