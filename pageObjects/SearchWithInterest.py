

class SearchEventByInterest:

    def __init__(self, driver):
        self.driver = driver

    def search_button(self, driver):
        return driver.find_element_by_id('Search events')

    def time_of_event(self, driver):
        return driver.find_element_by_id('com.eventbrite.attendee:id/date_picker')

    def select_time_mood_from_list(self, driver):
        return driver.find_element_by_xpath('//android.widget.TextView[@index=3]')

    def location(self, driver):
        return driver.find_element_by_id('com.eventbrite.attendee:id/location_picker')

    def insert_location(self, driver):
        return driver.find_element_by_id('com.eventbrite.attendee:id/search')

    def select_location_from_list(self, driver):
        return driver.find_element_by_xpath('//android.widget.RelativeLayout[@index=0]')

    def mood(self, driver):
        return driver.find_element_by_id('com.eventbrite.attendee:id/mood_picker')

    def forward_button(self, driver):
        return driver.find_element_by_id('com.eventbrite.attendee:id/fab')

    def selected_time_filter_list(self, driver):
        return driver.find_elements_by_id('com.eventbrite.attendee:id/text')
