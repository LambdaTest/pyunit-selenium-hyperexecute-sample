import os
import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from unittest import TestLoader, TestSuite
import HtmlTestRunner
import time

# Username and AccessKey available at https://accounts.lambdatest.com/detail/profile
username = os.environ.get("LT_USERNAME")
access_key = os.environ.get("LT_ACCESS_KEY")

# Get the Present Working Directory since that is the place where the report
# would be stored
current_directory = os.getcwd()

class HyperTestPyUnitTest(unittest.TestCase):
    # Generate capabilites from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case and 
    def setUp(self):
        desired_caps = {
            "build": '[Python] [Test Scenario-1] HyperTest demo using PyUnit framework',
            "name": '[Python] [Test Scenario-1] HyperTest demo using PyUnit framework',
            "platform": 'Windows 10',
            "browserName": 'firefox',
            "version": 'latest'
        }
        self.driver = webdriver.Remote(
           command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),
           desired_capabilities= desired_caps)


# tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

    def test_unit_user_should_able_to_add_item(self):
        driver = self.driver

        # Url
        driver.get("https://lambdatest.github.io/sample-todo-app/")

        # Click on check box
        check_box_one = driver.find_element(By.NAME, "li1")
        check_box_one.click()
        time.sleep(5)

        # Click on check box
        check_box_two = driver.find_element(By.NAME, "li2")
        check_box_two.click()
        time.sleep(5)

        # Enter item in textfield
        textfield = driver.find_element(By.ID, "sampletodotext")
        textfield.send_keys("Yey, Let's add it to list")
        time.sleep(5)

        # Click on add button
        add_button = driver.find_element(By.ID, "addbutton")
        add_button.click()
        time.sleep(3)

        # Verified added item
        added_item = driver.find_element(By.XPATH, "//span[@class='done-false']").text
        time.sleep(3)
        print (added_item)

if __name__ == "__main__":
     unittest.main()
