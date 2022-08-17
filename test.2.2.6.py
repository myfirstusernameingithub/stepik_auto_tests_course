# https://stepik.org/lesson/228249/step/6?unit=200781
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # собираем число из элемента
    x = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap").text
    # делаем расчёты с учетом выбранного элемента
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    # вводим значение расчёта в поле
    browser.find_element(By.CSS_SELECTOR, "input#answer:required").send_keys(calc(x))

    # кликаем на чекбокс, радио и кнопку
    browser.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
    radio = browser.find_element(By.CSS_SELECTOR, "input[value='robots']")
    # скрол с центром на радио
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # выбор итогового кода, который нужно скопировать для решения теста
    s_alert = browser.switch_to.alert.text
    s_code = s_alert.find(": ")
    print("<!!!> КОД ДЛЯ ВЫПОЛНЕНИЯ ЗАДАНИЯ: " + s_alert[s_code+2:])

finally:
    # задержка чтобы успесть скопировать код для ответа
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла (зачем?)