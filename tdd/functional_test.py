# function test == acceptance test == end to end test
# It follows a user story
import unittest
import argparse
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


HEADLESS = True
VERBOSE = False

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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')

        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )
        
        # He types "Buy shawarma" into a text box
        inputbox.send_keys('Buy shawarma')

        # When He hits enter, the page updates, and now the page lists
        # "1: Buy shawarma" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy shawarma' for row in rows)
        )
        # There is still a text box inviting his to add another item. He
        # enters "Eat shawarma"
        self.fail('Finish the test')
        # The page updates again, and now shows both items on his list

        # Hammas wonders whether the site will remember his list. Then He sees
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
