from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path='/home/daniil/D_info/Netology/geckodriver')
driver.get('https://passport.yandex.ru/auth/')
element = driver.find_element_by_name("login")
time.sleep(2)
element.send_keys("user28")
time.sleep(1)
element.send_keys(Keys.RETURN)
time.sleep(2)
assert "Операция прошла успешно" not in driver.page_source
driver.close()
driver.quit()
