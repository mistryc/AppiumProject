

class LoginEB:

    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(10)

    def more_button(self, driver):
        return driver.find_element_by_id("More")

    def login_button(self, driver):
        return self.driver.find_element_by_id("com.eventbrite.attendee:id/login_button")

    def saved_email_popup(self, driver):
        return self.driver.find_element_by_id("com.google.android.gms:id/credential_picker_layout")

    def cancel_popup(self, driver):
        return self.driver.find_element_by_id("com.google.android.gms:id/cancel")

    def email_text(self, driver):
        return self.driver.find_element_by_id("com.eventbrite.attendee:id/edittext_verify_email")

    def continue_buton(self, driver):
        return self.driver.find_element_by_id("com.eventbrite.attendee:id/button_continue")

    def password_text(self, driver):
        return self.driver.find_element_by_id("com.eventbrite.attendee:id/edittext_password")

    def saved_email(self):
        if self.saved_email_popup(self.driver).is_displayed():
            return True
        else:
            return False
        # assertEqual("Name is displayed")

    def enter_un_pw(self):
        self.email_text(self.driver).send_keys("chetanmistry02@yahoo.com")
        self.driver.hide_keyboard()
        self.continue_buton(self.driver).click()
        self.password_text(self.driver).send_keys("Chetan@02")
        self.driver.hide_keyboard()
        self.continue_buton(self.driver).click()
