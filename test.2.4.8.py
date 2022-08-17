# https://stepik.org/lesson/181384/step/8?unit=156009
# python C:\Users\Andrew\EDUCATION\Testing\STEPIK.Selenium.Python\Module2\test.2.1.5.py
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time, math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 15 секунд, пока цена не станет равной $100
    WebDriverWait(browser,15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(By.CSS_SELECTOR,"button#book").click()

    x = browser.find_element(By.CSS_SELECTOR,"span#input_value").text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR,"input#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR,"button#solve").click()

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