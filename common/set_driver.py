import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def set_driver():
    current_path = os.path.dirname(__file__)
    Firefox_path = os.path.join(current_path, '..\\Webdriver/geckodriver.exe')  # geckodriver
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://127.0.0.1/zentao/user-login.html")
    return driver