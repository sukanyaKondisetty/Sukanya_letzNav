'''
Created on 26-Oct-2017

@author: nagasukanya.k
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

class CA_PPM(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome("C:\\Users\\nagasukanya.k\\eclipse-workspace\\Selenium\\lib1\\ChromeDriver\\chromedriver.exe")
        cls.driver.implicitly_wait(6)
        cls.driver.maximize_window()
        cls.driver.get("http://clarityv15.excers.com")
        cls.driver.title
        
    def setUp(self):
        self.username=self.driver.find_element_by_id('ppm_login_username').send_keys("admin")
        self.password=self.driver.find_element_by_id('ppm_login_password').send_keys("clarity1")
        self.driver.find_element_by_id('ppm_login_button').click()
    def test_1(self):
        time.sleep(4)
        self.driver.find_element_by_class_name('letznav-black-label').click()
        self.search=self.driver.find_element_by_class_name('letznav-search-box').send_keys("Assign a Resource to a Task")
        time.sleep(3)
        self.driver.find_element_by_link_text("Assign a Resource to a Task").click()
        self.home=self.driver.find_element_by_css_selector('span[alt="Home"]')
        self.hover=ActionChains(self.driver).move_to_element(self.home)
        time.sleep(4)
        self.hover.perform()
    def test_2(self):
        time.sleep(4)
        self.driver.find_element_by_class_name('letznav-black-label').click()
        self.search=self.driver.find_element_by_class_name('letznav-search-box').send_keys("Project")
        time.sleep(3)
        self.driver.find_element_by_link_text("project").click()
        self.home=self.driver.find_element_by_css_selector('span[alt="Home"]')
        self.hover=ActionChains(self.driver).move_to_element(self.home)
        time.sleep(4)
        self.hover.perform()
    def tearDown(self):
        time.sleep(4)
        self.driver.find_element_by_css_selector("a[id=ppm_header_logout]").click()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        
    
    
    
    
if __name__ == "__main__":
   
    
    
    #import sys;sys.argv = ['', 'Test.testName']
   unittest.main()