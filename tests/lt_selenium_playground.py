import os
import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
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
        options = webdriver.ChromeOptions()
        options.browser_version = 'latest'
        options.platform_name = os.environ.get("TARGET_OS")

        # LambdaTest specific capabilities
        lt_options = {
            "build": '[Python] [Test Scenario-2] HyperTest demo using PyUnit framework',
            "name": '[Python] [Test Scenario-2] HyperTest demo using PyUnit framework',
        }
        options.set_capability('LT:Options', lt_options)

        self.driver = webdriver.Remote(
           command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),
           options=options)

    # Standard helper: re-finds the element fresh (waits up to 20s, ignoring
    # stale references) right before it is used, so a handle can never go stale.
    # Mirrors the C# SpecFlow WaitForElement(By) pattern.
    def wait_for_element(self, locator):
        wait = WebDriverWait(
            self.driver, 20,
            ignored_exceptions=(StaleElementReferenceException,))
        return wait.until(lambda d: d.find_element(*locator))

    def test_input_forms(self):
        driver = self.driver

        # Navigate directly to the Input Form page instead of clicking the link
        # on the selenium-playground home page. The home page re-renders while
        # loading, which makes the link go stale between find and click.
        driver.get('https://www.lambdatest.com/selenium-playground/input-form-demo')

        # Wait for the Input Form page to finish loading before interacting.
        self.wait_for_element((By.XPATH, "//input[@id='name']"))

        URL = driver.current_url
        # Assert if required
        print("Current URL " + URL)
        print()

        self.wait_for_element((By.XPATH, "//input[@id='name']")).send_keys("Testing")
        self.wait_for_element((By.XPATH, "//input[@id='inputEmail4']")).send_keys("testing@testing.com")
        self.wait_for_element((By.XPATH, "//input[@id='inputPassword4']")).send_keys("password")
        self.wait_for_element((By.CSS_SELECTOR, "#company")).send_keys("LambdaTest")
        self.wait_for_element((By.CSS_SELECTOR, "#websitename")).send_keys("https://wwww.lambdatest.com")

        country_dropdown = Select(self.wait_for_element((By.XPATH, "//select[@name='country']")))
        country_dropdown.select_by_visible_text("United States")

        self.wait_for_element((By.XPATH, "//input[@id='inputCity']")).send_keys("San Jose")
        self.wait_for_element((By.CSS_SELECTOR, "[placeholder='Address 1']")).send_keys("Googleplex, 1600 Amphitheatre Pkwy")
        self.wait_for_element((By.CSS_SELECTOR, "[placeholder='Address 2']")).send_keys("Mountain View, CA 94043")
        self.wait_for_element((By.CSS_SELECTOR, "#inputState")).send_keys("California")
        self.wait_for_element((By.CSS_SELECTOR, "#inputZip")).send_keys("94088")

        # Click on the Submit button
        self.wait_for_element((By.CSS_SELECTOR, "#seleniumform > div.text-right.mt-20 > button")).click()
        time.sleep(2)

        # Assert if the page contains a certain text
        assert driver.page_source.find("Thanks for contacting us, we will get back to you shortly")

        print("Input Form Demo complete")

    def test_progress_bars(self):

        driver = self.driver

        driver.get('https://www.selenium.dev/selenium/web/web-form.html')

        # Wait for the form to be ready before interacting.
        self.wait_for_element((By.CSS_SELECTOR, "#my-text-id"))

        current_url = driver.current_url
        print("Current URL is " + current_url)

        # Fill the form
        self.wait_for_element((By.CSS_SELECTOR, "#my-text-id")).send_keys("Testing")
        self.wait_for_element((By.CSS_SELECTOR, "input[name='my-password']")).send_keys("password")
        self.wait_for_element((By.CSS_SELECTOR, "textarea[name='my-textarea']")).send_keys("Hello from Selenium on LambdaTest")

        dropdown = Select(self.wait_for_element((By.CSS_SELECTOR, "select[name='my-select']")))
        dropdown.select_by_visible_text("Three")

        self.wait_for_element((By.CSS_SELECTOR, "input[name='my-datalist']")).send_keys("Seattle")

        # Click on the Submit button
        self.wait_for_element((By.CSS_SELECTOR, "button[type='submit']")).click()

        # Verify the form was submitted successfully
        message = self.wait_for_element((By.CSS_SELECTOR, "#message")).text
        assert "Received!" in message

        print("Selenium Web Form Demo complete")

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_2'))