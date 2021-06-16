from selenium import webdriver
from selenium.webdriver.common.by import By
import math

import time

link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.ID, 'treasure').get_attribute('valuex'))
    answer = math.log(abs(12 * math.sin(x)))

    browser.find_element(By.ID, 'answer').send_keys(str(answer))
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(5)
    browser.quit()
