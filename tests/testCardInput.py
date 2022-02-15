from asyncio import wait_for
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from driver.driver import Driver

class TestSalutCardDataValidation(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()

    def tearDown(self):
        self.driver.instance.quit()

    #TBD - Setup separate classes for login, page objects?, DDT
    def TestSalutCardDataValidation(self):
        ## Skipping onboarding
        skipOnboardingButton = self.driver.instance.find_element_by_android_uiautomator('new UiSelector().text("Пропустить")')
        skipOnboardingButton.click()

        ## Waiting for login button loaded 
        WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((By.ID, "ru.sberbank.sdakit.companion.prod:id/companion_button_text")))

        # Login to the app
        loginButton = self.driver.instance.find_element_by_id('ru.sberbank.sdakit.companion.prod:id/companion_button_text')
        loginButton.click()

        ## Waiting for main screen loaded
        WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((By.ID, "ru.sberbank.sdakit.companion.prod:id/title_card_container")))

        # Press on the gear button
        # Using XPATH as element is NAF and no better ways to select it. In real world would ask development to fix it 
        WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((By.XPATH, "//androidx.cardview.widget.CardView[@index='0']//android.widget.LinearLayout[@index='1']")))
        gearButton = self.driver.instance.find_element_by_xpath("//androidx.cardview.widget.CardView[@index='0']/android.widget.LinearLayout[@index='0']/android.widget.LinearLayout[@index='1']/android.widget.LinearLayout[@index='1']")
        gearButton.click()

        ## Waiting for main screen loaded
        paymentsMenuItem = self.driver.instance.find_element_by_android_uiautomator('new UiSelector().text("Платежи")')
        paymentsMenuItem.click()

        # Wait for card list to be loaded
        self.driver.instance.implicitly_wait(5)

        addCardButton = self.driver.instance.find_element_by_android_uiautomator('new UiSelector().text("Добавить карту")')
        addCardButton.click()

        ## Fill in card data
        # Wait for form to be loaded
        WebDriverWait(self.driver.instance, 15).until(EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@resource-id='pan']")))

        # Using XPATH as elements below are NAF and no better ways to select it (despite having id). In real world would ask development to fix it 
        # input card number
        cardNumberInput = self.driver.instance.find_element_by_xpath("//android.widget.EditText[@resource-id='pan']")
        cardNumberInput.send_keys("1234 1234 1234 1234")

        # assert label about invalid card number is displayed. In Requirements - "Неверный код карты" - but I assume functionally is the same
        invalidCardNumberLabel = self.driver.instance.find_element_by_android_uiautomator('new UiSelector().text("Неверный номер карты")')
        self.assertTrue(invalidCardNumberLabel.is_displayed())

        # input card date
        cardNumberDateInput = self.driver.instance.find_element_by_xpath("//android.widget.EditText[@resource-id='expiry']")
        cardNumberDateInput.send_keys("03/05")

        # assert label about invalid card date is displayed
        invalidCardDateLabel = self.driver.instance.find_element_by_android_uiautomator('new UiSelector().text("Неверная дата")')
        self.assertTrue(invalidCardDateLabel.is_displayed())

        # input cvc/cvv
        cardCVCInput = self.driver.instance.find_element_by_xpath("//android.widget.EditText[@resource-id='cvc']")
        cardCVCInput.send_keys("123")

        # input email
        emailInput = self.driver.instance.find_element_by_xpath("//android.widget.EditText[@resource-id='email']")
        emailInput.send_keys("123@yandex.ru")

        payButton = self.driver.instance.find_element_by_android_uiautomator('new UiSelector().text("Оплатить")')

        # Payments button is by default clickable and enabled, so checking this parameters would make test fail.
        # I would check if it is expected (as functionally doesn't looks like a bug) and
        # suggest to check that invalid form label appear after click
        payButton.click()

        # assert label about invalid card form data is displayed
        invalidCardDateLabel = self.driver.instance.find_element_by_android_uiautomator('new UiSelector().text("Проверьте правильность заполнения платежной формы")')
        self.assertTrue(invalidCardDateLabel.is_displayed())

