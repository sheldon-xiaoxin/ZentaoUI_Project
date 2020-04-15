import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


current_path = os.path.dirname(__file__)
Firefox_path = os.path.join( current_path , '../..\\Webdriver/geckodriver.exe') #geckodriver

class MenulinkCase(unittest.TestCase):
    def setUp(self) -> None:  # 把selenium的初始化配置放入
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1/zentao/user-login.html")
        self.driver.find_element(By.XPATH, '//input[@id="account"]').send_keys("admin")
        self.driver.find_element(By.XPATH, '//input[@type ="password"]').send_keys("idontKNOW666")
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    def tearDown(self) -> None:  #测试清理操作 浏览器关闭
        time.sleep(2)
        self.driver.quit()

    def test_my_link(self):
        '''case04  验证我的地盘菜单能否正确链接'''
        self.driver.find_element(By.XPATH, '//li[@data-id="my"]').click()
        # 等待10s,等待过程中判断网页标题是否是"百度一下，你就知道"
        # 如果是就继续执行后续代码，反之等待10s结束时报错
        #WebDriverWait(driver, 10).until(EC.title_is("百度一下，你就知道"))
        self.assertTrue(EC.title_is(" 我的地盘--禅道"))

    def test_product_link(self):
        '''case05  验证我的地盘产品主页菜单能否正确链接'''
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH, '//span[@class="user-name"]'),'admin'),'test_login用例执行失败')
        self.driver.find_element(By.XPATH, '//li[@data-id="product"]').click()
        self.assertTrue(EC.title_is(" 产品主页--禅道"))

if __name__ == "__main__":
    unittest.main()