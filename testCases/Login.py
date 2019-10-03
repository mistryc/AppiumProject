import unittest
from pageObjects.Login import LoginEB
from pageObjects.SkipLoginPage import LandingPageEB
from utils.mywebdriver import Driver


class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = Driver().instance

    def test_EventBright_Login(self):
        eventbright = LandingPageEB(self.driver)
        eventbright.skip_login_select_location(self.driver)

        login = LoginEB(self.driver)
        login.more_button(self.driver).click()
        self.driver.implicitly_wait(10)
        login.login_button(self.driver).click()
        self.driver.implicitly_wait(10)
        if login.saved_email():
            login.cancel_popup(self.driver).click()
            login.enter_un_pw()
        else:
            login.enter_un_pw()

    def tearDown(self):
        self.driver.quit()

