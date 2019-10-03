import unittest
from pyunitreport import HTMLTestRunner
import os
from testCases.SkipLoginPage import LandingPageTestCase
from testCases.Login import LoginTestCase
from testCases.SearchWithInterest import SearchByInterestTestCase
from testCases.BookTicket import BookTicketTestCase

# get the directory path to output report file
directory = os.getcwd()

# get all tests from SearchText and HomePageTest class
landing_page = unittest.TestLoader().loadTestsFromTestCase(LandingPageTestCase)
login_user = unittest.TestLoader().loadTestsFromTestCase(LoginTestCase)
search_with_interest = unittest.TestLoader().loadTestsFromTestCase(SearchByInterestTestCase)
book_ticket = unittest.TestLoader().loadTestsFromTestCase(BookTicketTestCase)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([landing_page, login_user, search_with_interest, book_ticket])

report = {
    "output": directory+"\Reports",
}

runner = HTMLTestRunner(**report)

# run the suite using HTMLTestRunner
runner.run(test_suite)
