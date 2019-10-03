from appium.webdriver.common.touch_action import TouchAction


class LandingPageEB:

    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(10)

    def skip_button(self, driver):
        return driver.find_element_by_id("com.eventbrite.attendee:id/skip")

    def saved_email_popup(self, driver):
        return self.driver.find_element_by_id("com.google.android.gms:id/credential_picker_layout")

    def cancel_saved_email_option(self, driver):
        return driver.find_element_by_id("com.google.android.gms:id/cancel")

    def skip_login_page(self, driver):
        return driver.find_element_by_id("com.eventbrite.attendee:id/skip")

    def location(self, driver):
        return driver.find_element_by_id("com.eventbrite.attendee:id/location")

    def search_location(self, driver):
        return driver.find_element_by_id("com.eventbrite.attendee:id/search")

    def select_location_from_options(self, driver):
        return driver.find_element_by_xpath("//android.widget.RelativeLayout[@index='0']")

    def wrong_location_message(self, driver):
        return driver.find_element_by_id('com.eventbrite.attendee:id/state_layout_subtitle')

    def homepage_check(self, driver):
        return driver.find_element_by_xpath("//android.widget.TextView[@index='0']")

    def homepage_location_search(self, driver):
        return driver.find_element_by_id('com.eventbrite.attendee:id/header_location')

    def skip_login_process(self, driver):
        self.skip_login_page(self.driver).click()
        self.select_location(self.driver)

    def select_location(self, driver):
        self.location(self.driver).click()
        self.search_location(self.driver).send_keys('New York')
        self.driver.hide_keyboard()
        touch = TouchAction(self.driver)
        touch.press(x=670, y=2094).move_to(x=662, y=1464).release().perform()
        self.select_location_from_options(self.driver).click()

    def skip_login_select_location(self, driver):
        self.skip_button(self.driver).click()
        if self.saved_email_popup(self.driver):
            self.cancel_saved_email_option(self.driver).click()
            self.skip_login_process(self.driver)
        else:
            self.skip_login_process(self.driver)
