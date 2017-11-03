'''
Created on 26-Oct-2017

@author: nagasukanya.k
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
class letzNav(unittest.TestCase):


    @classmethod
    def setUpClass(ins):
        ins.driver=webdriver.Chrome("C:\\Users\\nagasukanya.k\\eclipse-workspace\\Selenium\\lib1\\ChromeDriver\\chromedriver.exe")
        ins.driver.implicitly_wait(6)
        ins.driver.maximize_window()
        ins.driver.get("https://navleankit.herokuapp.com")
        ins.driver.title
        
    def test_1(self):
        pass
        self.username=self.driver.find_element_by_css_selector("input[name=username]").send_keys("venkateshwarlu.thota@excers.com") 
        self.password=self.driver.find_element_by_css_selector("input[name=password]").send_keys("Thota@excers169")
        self.login=self.driver.find_element_by_css_selector("button[type=submit]").click() 
        time.sleep(3)
        try:
            self.driver.find_element_by_css_selector("div[class=error top]")
            print ('Entered Username or password is wrong')
        except NoSuchElementException:
            print ('Login Successful')
    def test_2(self):
        pass
        self.searchflows=self.driver.find_element_by_css_selector("input[id=md-input-0]").send_keys("project")
        time.sleep(6)
        self.driver.find_element_by_css_selector("a[title='Export flow documentation in PDF']").click()
        time.sleep(6)
        
    def test_3(self):
        self.driver.find_element_by_css_selector("div[class=flow-card-title]").click()
        time.sleep(4)
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_css_selector("button[class*=primary button-action]").click()
        time.sleep(4)
        self.driver.find_element_by_css_selector("div[class=mat-checkbox-inner-container]").click()
    def test_4(self):
        time.sleep(4)
        self.driver.find_element_by_css_selector("a[routerlink=manage-tags]").click()
        time.sleep(4)
        self.tag=self.driver.find_element_by_css_selector("input[name=tagName]")
        time.sleep(4)
        self.tag.send_keys("Time Management")
        time.sleep(4)
        self.driver.find_element_by_css_selector("button[class=primary mat-button]").click()
      
    #def tearDown(self):
        #self.driver.execute_script("document.body.style.zoom='80%'")
        #time.sleep(6)
        #self.driver.find_element_by_css_selector("span[class*=sidebar-usermenu-username]").click()
        
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        
    
  
       

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()