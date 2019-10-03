import unittest
from pageObjects.SearchWithInterest import SearchEventByInterest
from pageObjects.SkipLoginPage import LandingPageEB
from utils.mywebdriver import Driver


class SearchByInterestTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = Driver().instance

    def test_search_by_interest(self):
        searchevent = SearchEventByInterest(self)
        eventbright = LandingPageEB(self.driver)
        self.driver.implicitly_wait(10)

        # skip the landing pages and goto homepage
        eventbright.skip_login_select_location(self.driver)

        # start search by interest
        # select search button
        searchevent.search_button(self.driver).click()

        # tap to select the time of the event
        searchevent.time_of_event(self.driver).click()

        # select the time form list
        searchevent.select_time_mood_from_list(self.driver).click()
        selected_time = searchevent.time_of_event(self.driver).text

        # tap to select the location for the events
        searchevent.location(self.driver).click()

        # type the location interested and select it form the list
        searchevent.insert_location(self.driver).send_keys('Chicago')
        searchevent.select_location_from_list(self.driver).click()
        selected_location = searchevent.location(self.driver).text

        # tap to select mood
        searchevent.mood(self.driver).click()

        # select mood from the list
        searchevent.select_time_mood_from_list(self.driver).click()
        selected_mood = searchevent.mood(self.driver).text

        # click on next button
        searchevent.forward_button(self.driver).click()

    def tearDown(self):
        self.driver.quit()
