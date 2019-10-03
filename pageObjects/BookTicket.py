

class BookTicketEB:

    def __init__(self, driver):
        self.driver = driver

    def searchEvent(self, driver):
        return driver.find_element_by_id('com.eventbrite.attendee:id/search')

    def event_to_select(self, driver):
        return driver.find_element_by_xpath("//android.widget.RelativeLayout[@index ='1']/"
                                            "android.widget.TextView[@index='1']")

    def title_of_selected_event(self, driver):
        return driver.find_element_by_id('com.eventbrite.attendee:id/title')

    def ticket_button(self, driver):
        return driver.find_element_by_id('com.eventbrite.attendee:id/ticket_button')

    def back_button(self, driver):
        return driver.find_element_by_id('Navigate up')

    def register_for_event(self, driver):
        return driver.find_element_by_id('event_order_start_register_button')

    def first_name(self, driver):
        return driver.find_element_by_id('id_first_name')

    def last_name(self, driver):
        return driver.find_element_by_id('id_last_name')

    def email(self, driver):
        return driver.find_element_by_id('id_email')

    def first_name_error(self, driver):
        return driver.find_element_by_id('id_first_name_error')

    def last_name_error(self, driver):
        return driver.find_element_by_id('id_last_name_error')

    def email_error(self, driver):
        return driver.find_element_by_id('id_email_error')




