import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from common import set_driver
from common import login


current_path = os.path.dirname(__file__)
Firefox_path = os.path.join( current_path , '../..\\Webdriver/geckodriver.exe') #geckodriver

class loginFailCase(unittest.TestCase):
    def setUp(self) -> None:  # 把selenium的初始化配置放入
        self.driver = set_driver.set_driver()

    def tearDown(self) -> None:  #测试清理操作 浏览器关闭
        time.sleep(2)
        self.driver.quit()

    def test_login(self):
        '''case03 admin  admin 测试能否登录'''
        login.login(self.driver, 'admin', 'idontKNOW666')
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH, '//span[@class="user-name"]'),'admin'),'test_login用例执行失败')
        self.assertTrue(WebDriverWait(self.driver,10).until(EC.alert_is_present()))


if __name__ == "__main__":
    unittest.main()