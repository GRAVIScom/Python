import math
import time
from selenium import webdriver
browser=webdriver.Chrome()

link="http://suninjuly.github.io/alert_accept.html"
link1="http://suninjuly.github.io/redirect_accept.html"
browser.get(link1)
browser.find_element_by_css_selector("body > form > div > div > button").click()
#confirm = browser.switch_to.alert
#confirm.accept()
#current_window = browser.current_window_handle
new_window=browser.window_handles[1]
browser.switch_to.window(new_window)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
z_element=browser.find_element_by_id("input_value")
z=z_element.text
y = calc(z)
input=browser.find_element_by_id("answer")
input.send_keys(y)
button=browser.find_element_by_tag_name("button")
button.click()
print(browser.switch_to.alert.text)
browser.quit