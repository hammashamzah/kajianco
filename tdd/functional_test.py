# function test == acceptance test == end to end test
# It follows a user story
import unittest
import argparse
from selenium import webdriver

HEADLESS = True
VERBOSE = True

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        if HEADLESS:
            self.chrome_options = webdriver.chrome.options.Options()
            self.chrome_options.add_argument("--headless")
            self.browser = webdriver.Chrome(options=self.chrome_options)
        else:
            self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):     
        # Hammas has heard about a cool new online to-do app. 
        # He goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # He is invited to enter a to-do item straight away

        # He types "Buy shawarma" into a text box

        # When He hits enter, the page updates, and now the page lists
        # "1: Buy shawarma" as an item in a to-do list

        # There is still a text box inviting his to add another item. He
        # enters "Eat shawarma"

        # The page updates again, and now shows both items on his list

        # Edith wonders whether the site will remember his list. Then He sees
        # that the site has generated a unique URL for his -- there is some
        # explanatory text to that effect.

        # He visits that URL - his to-do list is still there.

        # Satisfied, He goes back to sleep

def main():
    # parser = argparse.ArgumentParser(description='Functional Test.')
    # parser.add_argument('--headless', action='store_true')
    # isHeadless = parser.parse_args(['--headless'])
    # print(isHeadless)

    if VERBOSE:
        unittest.main()
    else:
        unittest.main(warnings='ignore')

if __name__ == '__main__':
    main()
