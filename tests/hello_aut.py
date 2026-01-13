import unittest, sys
from selenium import webdriver
from selenium.webdriver.common.by import By

class AutTest(unittest.TestCase):

    def setUp(self):
        # Get browser from command line argument, default to firefox
        browser = sys.argv[2] if len(sys.argv) > 2 else 'firefox'
        
        if browser.lower() == 'chrome':
            options = webdriver.ChromeOptions()
        elif browser.lower() == 'edge':
            options = webdriver.EdgeOptions()
        else:
            options = webdriver.FirefoxOptions()
            
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        server = 'http://localhost:4444'

        self.browser = webdriver.Remote(command_executor=server, options=options)
        self.addCleanup(self.browser.quit)

    def test_homepage(self):
        if len(sys.argv) > 1:
            url = sys.argv[1]
        else:
            url = "http://localhost"
            
        browser_name = sys.argv[2] if len(sys.argv) > 2 else 'firefox'

        self.browser.get(url)
        self.browser.save_screenshot(f'screenshot-{browser_name}.png')
        expected_result = "Welcome back, Guest!"
        actual_result = self.browser.find_element(By.TAG_NAME, 'p')

        self.assertIn(expected_result, actual_result.text)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, warnings='ignore')