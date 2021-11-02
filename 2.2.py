import time
import math
from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select

browser=webdriver.Chrome()
link="http://suninjuly.github.io/selects1.html"
link1="http://suninjuly.github.io/selects2.html"

browser.get(link1)
def calc(y,z):
    return str(int(y)+int(z))
y_element=browser.find_element_by_id("num1")
y=y_element.text
z_element=browser.find_element_by_id("input_value")
z=z_element.text
X=calc(y,z)
browser.find_element_by_tag_name("select").click()
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(X)
browser.find_element_by_xpath("/html/body/div/form/button").click()
time.sleep(10)
browser.quit