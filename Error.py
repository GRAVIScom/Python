from selenium import webdriver
import os
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
input1=browser.find_element_by_xpath("/html/body/div/form/div/input[1]")
input1.send_keys("1")
input2=browser.find_element_by_xpath("/html/body/div/form/div/input[2]")
input2.send_keys("2")
browser.find_element_by_xpath("/html/body/div/form/div/input[3]").send_keys("3")
with open("test.txt", "w") as file:
    content = file.write("automation")
dispath=browser.find_element_by_css_selector("#file")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')
dispath.send_keys(file_path)
browser.find_element_by_xpath("/html/body/div/form/button").click()
time.sleep(10)
browser.quit
