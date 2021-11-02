import math
import time
from selenium import webdriver
browser=webdriver.Chrome()

link="http://suninjuly.github.io/execute_script.html"
browser.get(link)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
input=browser.find_element_by_css_selector("#answer")
input.send_keys(y)
checkbox=browser.find_element_by_id("robotCheckbox")
checkbox.click()
rb=browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", rb)
rb.click()
button=browser.find_element_by_class_name("btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(10)
browser.quit