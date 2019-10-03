from appium import webdriver
import os


class Driver:

    def __init__(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '988923474e43423639',
            'app': os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '../utils/APKs/Eventbrite Discover popular events nearby fun_v6.13.2_apkpure.com.apk')),
            'appPackage': 'com.eventbrite.attendee',
            'appActivity': 'com.eventbrite.attendee.activities.MainActivity'
        }

        self.instance = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
