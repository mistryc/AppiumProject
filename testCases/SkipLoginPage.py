import unittest
from pageObjects.SkipLoginPage import LandingPageEB
from utils.mywebdriver import Driver


class LandingPageTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = Driver().instance

    def test_EventBright_Launches(self):
        eventbright = LandingPageEB(self.driver)
        eventbright.skip_login_select_location(self.driver)
        heading = eventbright.homepage_check(self.driver).text
        heading = heading.replace(u'\xa0', ' ')
        self.assertEqual(heading, "What’s good in", 'Successfully landed on homepage')

    def test_wrong_input_location(self):
        eventbright = LandingPageEB(self.driver)
        eventbright.skip_login_select_location(self.driver)
        eventbright.homepage_location_search(self.driver).click()
        eventbright.search_location(self.driver).send_keys('NewYork')
        message = eventbright.wrong_location_message(self.driver).text
        message = message.replace(u'\xa0', ' ')
        self.assertEqual(message, "We’re not getting a match… try something else", 'Wrong location entered')

    def tearDown(self):
        self.driver.quit()

