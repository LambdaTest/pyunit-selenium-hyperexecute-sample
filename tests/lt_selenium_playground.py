import os
import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
import HtmlTestRunner

# Username and AccessKey available at https://accounts.lambdatest.com/detail/profile
username = os.environ.get("LT_USERNAME")
access_key = os.environ.get("LT_ACCESS_KEY")

class HyperTestPyUnitDocTest(unittest.TestCase):
    # Generate capabilites from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case
    def setUp(self):
        desired_caps = {
            "build": '[Python] [Test Scenario-2] HyperTest demo using PyUnit framework',
            "name": '[Python] [Test Scenario-2] HyperTest demo using PyUnit framework',
            "platform": os.environ.get("TARGET_OS"),
            "browserName": 'chrome',
            "version": 'latest'
        }
        self.driver = webdriver.Remote(
           command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),
           desired_capabilities= desired_caps)

    def test_input_forms(self):
        driver = self.driver

        action = ActionChains(driver)
        wait = WebDriverWait(driver, 5)
        driver.get('https://www.lambdatest.com/selenium-playground/')

        element = driver.find_element(By.XPATH, "//a[.='Input Form Submit']")
        element.click()

        URL = driver.current_url
        # Assert if required
        print("Current URL " + URL)
        print()

        name = driver.find_element(By.XPATH, "//input[@id='name']")
        name.send_keys("Testing")
        time.sleep(2)

        email_address = driver.find_element(By.XPATH, "//input[@id='inputEmail4']")
        email_address.send_keys("testing@testing.com")
        time.sleep(2)

        password = driver.find_element(By.XPATH, "//input[@id='inputPassword4']")
        password.send_keys("password")
        time.sleep(2)

        company = driver.find_element(By.CSS_SELECTOR, "#company")
        company.send_keys("LambdaTest")
        time.sleep(2)

        website = driver.find_element(By.CSS_SELECTOR, "#websitename")
        website.send_keys("https://wwww.lambdatest.com")
        time.sleep(2)

        country_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='country']"))
        country_dropdown.select_by_visible_text("United States")
        time.sleep(2)

        city = driver.find_element(By.XPATH, "//input[@id='inputCity']")
        city.send_keys("San Jose")
        time.sleep(2)

        address1 = driver.find_element(By.CSS_SELECTOR, "[placeholder='Address 1']")
        address1.send_keys("Googleplex, 1600 Amphitheatre Pkwy")
        time.sleep(2)

        address2 = driver.find_element(By.CSS_SELECTOR, "[placeholder='Address 2']")
        address2.send_keys("Mountain View, CA 94043")
        time.sleep(2)

        state = driver.find_element(By.CSS_SELECTOR, "#inputState")
        state.send_keys("California")
        time.sleep(2)

        zipcode = self.driver.find_element(By.CSS_SELECTOR, "#inputZip")
        zipcode.send_keys("94088")
        time.sleep(2)

        # Click on the Submit button
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "#seleniumform > div.text-right.mt-20 > button")
        submit_button.click()
        time.sleep(2)

        # Assert if the page contains a certain text
        assert driver.page_source.find("Thanks for contacting us, we will get back to you shortly")
        time.sleep(5)

        print("Input Form Demo complete")

    def test_progress_bars(self):

        driver = self.driver

        action = ActionChains(driver)
        wait = WebDriverWait(driver, 5)

        driver.get('https://www.lambdatest.com/selenium-playground/input-form-demo')
    
        driver.get('https://www.lambdatest.com/selenium-playground/bootstrap-progress-bar-dialog-demo')
        element = driver.find_element(By.XPATH, "//*[@id='__next']/section[2]/div/div/h1")
        element.click()
        # wait.until(EC.element_to_be_clickable(element)).click()
        time.sleep(3)

        # Click on the Drag & Drop Sliders
        driver.get('https://www.lambdatest.com/selenium-playground/drag-and-drop-demo')
        drag_drop = driver.find_element(By.XPATH, "//*[@id='__next']/section[2]/div/div/h1")
        drag_drop.click()
        time.sleep(10)

        print("Progress Bar Test Complete")

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_2'))
