import time
import unittest
from selenium import webdriver

class EdxLogin(unittest.TestCase):

    def setUp(self):
        #Initialize webdriver
        self.driver = webdriver.Firefox()

    def test_login(self):
        # Open the target page
        self.driver.get('https://www.Gmail.com')
        # Assert that 'edX' is present in browser title
        time.sleep(2)        
        self.assertIn('Gmail', self.driver.title)
        # Find and fill the email field
        email_elem = self.driver.find_element_by_css_selector('input[type="email"]')
        email_elem.send_keys('DummyEmail')
        # Find to click the next button
        next_elem = self.driver.find_element_by_css_selector('#identifierNext')
        next_elem.click()
        time.sleep(5)        
        #Find and fill the password field
        pwd_elem = self.driver.find_element_by_css_selector('input[type="password"]')
        pwd_elem.send_keys('DummyPassword')
        # Find and click the submit button
        submit_elem = self.driver.find_element_by_css_selector('#passwordNext')
        submit_elem.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
