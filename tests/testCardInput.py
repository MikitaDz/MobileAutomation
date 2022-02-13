from asyncio import wait_for
from lib2to3.pgen2 import driver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium import webdriver

class TestSalutSmokeTestCase(unittest.TestCase):

    ##TBD  - settings to config
    def setUp(self): # test method names begin with 'test'
        desired_capabilities = {}
        desired_capabilities['platformName'] = 'Android'
        desired_capabilities['deviceName'] = 'RF8M620Z7VV'
        desired_capabilities['appPackage'] = 'ru.sberbank.sdakit.companion.prod'
        desired_capabilities['appActivity'] = 'ru.sberbank.sdakit.companion.main.presentation.screen.CompanionMainActivity'
        desired_capabilities['unicodeKeyboard'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities)

    def tearDown(self):
        self.driver.quit()

    #TBD - Setup separate classes for login, page objects?, DDT
    def testInvalidCardInputSalut(self):
        ## Waiting for login button loaded 
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "ru.sberbank.sdakit.companion.prod:id/companion_button_text")))

        #Login to the app
        elementLoginButton = self.driver.find_element_by_id('ru.sberbank.sdakit.companion.prod:id/companion_button_text')
        elementLoginButton.click()

        ## Waiting for main screen loaded
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "ru.sberbank.sdakit.companion.prod:id/title_card_container")))

        #Press on the gear button
        #Using XPATH as element is NAF and no better ways to select it. In real world would ask development to fix it 
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//androidx.cardview.widget.CardView[@index='0']//android.widget.LinearLayout[@index='1']")))
        elementGearButton = self.driver.find_element_by_xpath("//androidx.cardview.widget.CardView[@index='0']/android.widget.LinearLayout[@index='0']/android.widget.LinearLayout[@index='1']/android.widget.LinearLayout[@index='1']")
        elementGearButton.click()

        ## Waiting for main screen loaded
        ##WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By., "Платежи")))ndElementByAndroidUIAutomator("text(\"Text\")")
        paymentsMenuItem = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Платежи")')
        paymentsMenuItem.click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "ru.sberbank.sdakit.companion.prod:id/companion_button_text")))

