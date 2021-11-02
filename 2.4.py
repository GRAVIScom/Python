from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from selenium import webdriver
browser=webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
browser.find_element_by_id("book").click()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element=browser.find_element_by_id("input_value")
x=x_element.text
y=calc(x)
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_css_selector("#solve").click()
print(browser.switch_to.alert.text)
