# https://stepik.org/lesson/228249/step/3?unit=200781
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "h2>#num1.nowrap").text
    y = browser.find_element(By.CSS_SELECTOR, "h2>#num2.nowrap").text
    # сложение взятых значений элемента путём перевода их в число, а затем обратно в строку чтобы её можно было выбрать
    result = str(int(x)+int(y))
    # вариант того что выше, только через метод, раз уж импортировали мат метод
    #def sum(x, y):
    #    return str(x + y)

    # выбор выпадающего списка через тэг select
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    # ищем элемент с текстом расчёта, который проводили выше
    select.select_by_value(result)

    browser.find_element(By.CSS_SELECTOR,"button[type='submit']").click()  

finally:
    # задержка чтобы успесть скопировать код для ответа
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла (зачем?)