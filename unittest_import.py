from selenium import webdriver
import time
import unittest

# Ваш код, который заполняет обязательные поля
class TestAbs(unittest.TestCase):
    def test_1(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        input1=browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.first_class > input")
        input1.send_keys("Test")
        input2=browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.second_class > input")
        input2.send_keys("Test")
        input3=browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.third_class > input")
        input3.send_keys("Test")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        
        # Проверяем, что смогли зарегистрироваться
        # # ждем загрузки страницы
        time.sleep(1)
        
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
    def test_2(self):
        link1 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link1)
        input1=browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.first_class > input")
        input1.send_keys("Test")
        input2=browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.second_class > input")
        input2.send_keys("Test")
        input3=browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.third_class > input")
        input3.send_keys("Test")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        
        # Проверяем, что смогли зарегистрироваться
        # # ждем загрузки страницы
        time.sleep(1)
        
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
if __name__=="__main__":
    unittest.main()