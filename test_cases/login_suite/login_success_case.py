import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import HTMLTestRunner
from common import set_driver
from common import login

current_path = os.path.dirname(__file__)
Firefox_path = os.path.join( current_path , '../..\\Webdriver/geckodriver.exe') #geckodriver

class loginSuccessCase(unittest.TestCase):
    def setUp(self) -> None:  # 把selenium的初始化配置放入
        self.driver = set_driver.set_driver()

    def tearDown(self) -> None:  #测试清理操作 浏览器关闭
        time.sleep(2)
        self.driver.quit()

    def test_login_1(self):
        '''case01 admin  admin 测试能否登录'''
        login.login(self.driver, 'admin', 'idontKNOW666')
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH, '//span[@class="user-name"]'),'admin'),'test_login用例执行失败')

    def test_login_2(self):
        '''case01 使用test01  test01 测试能否登录'''
        self.driver.find_element(By.XPATH, '//input[@id="account"]').send_keys("test01")
        self.driver.find_element(By.XPATH, '//input[@type ="password"]').send_keys("xin123456")
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()


if __name__ == "__main__":
    suite01 = unittest.TestSuite(unittest.makeSuite(loginSuccessCase))
    now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
    file = open('result_%s.html' %now_time, 'wb')
    html_runnner =HTMLTestRunner.HTMLTestRunner(stream=file,
                                                title='小新测试',
                                                description='测试描述')
    html_runnner.run(suite01)