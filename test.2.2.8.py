# https://stepik.org/lesson/228249/step/8?unit=200781
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR,"input[name='firstname']:required").send_keys("George")
    browser.find_element(By.CSS_SELECTOR,"input[name='lastname']:required").send_keys("Bush")
    browser.find_element(By.CSS_SELECTOR,"input[name='email']:required").send_keys("us.gov@mail.ru") 

    # получаем путь к директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    # добавляем к этому пути имя файла "file.txt"
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element(By.CSS_SELECTOR,"input#file").send_keys(file_path)

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