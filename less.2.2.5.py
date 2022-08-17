# https://stepik.org/lesson/228249/step/5?unit=200781
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    # В метод execute_script мы передали текст js-скрипта и найденный элемент button, 
    # к которому нужно будет проскроллить страницу. После выполнения кода элемент button должен оказаться в верхней части страницы.
    # Подробнее о методе см https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView .
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Также можно проскроллить всю страницу целиком на строго заданное количество пикселей. 
    # Эта команда проскроллит страницу на 100 пикселей вниз:
    #browser.execute_script("window.scrollBy(0, 100);")

    # Для сравнения приведем скрипт на этом языке, который делает то же, что приведенный выше пример для WebDriver:
    # javascript:
    #button = document.getElementsByTagName("button")[0];
    #button.scrollIntoView(true);

    # В этом примере можно справится без кода на Javascript. Для этого нужно использовать ActionChains:
    #_ = button.location_once_scrolled_into_view
    #button.click()

finally:
    # задержка чтобы успесть скопировать код для ответа
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла (зачем?)