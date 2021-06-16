from selenium import webdriver
import math
from time import sleep

link = 'http://suninjuly.github.io/math.html'

try:
    chrome = webdriver.Chrome()
    chrome.get(link)

    x = int(chrome.find_element_by_id('input_value').text)
    answer = math.log(abs(12 * math.sin(x)))

    chrome.find_element_by_id('answer').send_keys(str(answer))

    chrome.find_element_by_id('robotCheckbox').click()
    chrome.find_element_by_id('robotsRule').click()

    chrome.find_element_by_tag_name('button').click()

finally:
    sleep(11)
    chrome.quit()

