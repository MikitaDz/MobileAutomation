from appium import webdriver

#Driver initialization class
class Driver:
    def __init__(self):
        desired_capabilities = {
            'platformName': 'Android',
            'deviceName': 'RF8M620Z7VV',
            'appPackage': 'ru.sberbank.sdakit.companion.prod',
            'appActivity': 'ru.sberbank.sdakit.companion.main.presentation.screen.CompanionMainActivity',
            'unicodeKeyboard': True
        }
        self.instance = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities)