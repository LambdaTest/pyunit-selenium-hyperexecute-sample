import unittest
import HtmlTestRunner
import os
import lt_sample_todo
import lt_selenium_playground

# Get the Present Working Directory since that is the place where the report
# would be stored

current_directory = os.getcwd()

class HTML_TestRunner_TestSuite(unittest.TestCase):
    def test_consolidated_suite(self):

        # Create a TestSuite comprising the two test cases
        consolidated_test = unittest.TestSuite()

        # Add the test cases to the Test Suite
        consolidated_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(lt_sample_todo.HyperTestPyUnitTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(lt_selenium_playground.HyperTestPyUnitDocTest)
        ])

        output_file = open(current_directory + "\\HTML_Test_Reports_1", "w")

        html_runner = HtmlTestRunner.HTMLTestRunner(
            stream=output_file,
            report_title='Test_3 Report - PyUnit on Hypertest',
            descriptions='Test_3 Report - PyUnit on Hypertest'
        )
        html_runner.run(consolidated_test)

    def test_consolidated_suite_2(self):

        # Create a TestSuite comprising the two test cases
        consolidated_test = unittest.TestSuite()

        # Add the test cases to the Test Suite
        consolidated_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(lt_sample_todo.HyperTestPyUnitTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(lt_selenium_playground.HyperTestPyUnitDocTest)
        ])

        output_file = open(current_directory + "\\HTML_Test_Runner_Reports_2", "w")

        html_runner = HtmlTestRunner.HTMLTestRunner(
            stream=output_file,
            report_title='Test_4 Report - PyUnit on Hypertest',
            descriptions='Test_4 Report - PyUnit on Hypertest'
        )
        html_runner.run(consolidated_test)

if __name__ == '__main__':
    unittest.main()