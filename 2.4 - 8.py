from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


def calc(x):
    import math
    return math.log(abs(12 * math.sin(x)))


link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'book').click()

    x = int(browser.find_element_by_id('input_value').text)
    answer = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(str(answer))
    browser.find_element(By.ID, 'solve').click()



finally:
    sleep(5)
    browser.quit()
