import unittest
from pageObjects.BookTicket import BookTicketEB
from pageObjects.SearchWithInterest import SearchEventByInterest
from pageObjects.SkipLoginPage import LandingPageEB
from utils.mywebdriver import Driver


class BookTicketTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = Driver().instance

    def test_book_ticket(self):
        book_ticket = BookTicketEB(self)
        eventbright = LandingPageEB(self.driver)
        searchevent = SearchEventByInterest(self)
        self.driver.implicitly_wait(10)

        eventbright.skip_login_select_location(self.driver)
        searchevent.search_button(self.driver).click()

        # tap to select the location for the events
        searchevent.location(self.driver).click()

        # type the location interested and select it form the list
        searchevent.insert_location(self.driver).send_keys('New York')
        searchevent.select_location_from_list(self.driver).click()

        # click on next button
        searchevent.forward_button(self.driver).click()

        # search for the event
        book_ticket.searchEvent(self.driver).send_keys("Libra Affair at Ravel")

        self.driver.press_keycode(66)

        book_ticket.event_to_select(self.driver).click()
        self.driver.implicitly_wait(10)

        self.assertIn('Libra Affair at Ravel', book_ticket.title_of_selected_event(self.driver).text,
                      'Title does not contain the searched event')

        book_ticket.ticket_button(self.driver).click()

        book_ticket.back_button(self.driver).click()
        book_ticket.ticket_button(self.driver).click()
        self.driver.implicitly_wait(10)
        book_ticket.register_for_event(self.driver).click()

    def tearDown(self):
        self.driver.quit()
