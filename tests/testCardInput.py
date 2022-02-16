from asyncio import wait_for
from re import A
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from driver.driver import Driver
from flows.login import Login
from flows.profile import Profile
from flows.addCardForm import AddCardForm

class TestCardDataValidation(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()

    def tearDown(self):
        self.driver.instance.quit()

    def testCardDataInputValidation(self):
        # Login to the app
        login = Login(self.driver)
        login.loginAsAlrearyLoggedInUser()

        # Open profile
        profile = Profile(self.driver)
        profile.openProfile()

        # Open profile payments
        profile.openProfilePayments()

        # Open new card form
        profile.openNewCardForm()
        addCardForm = AddCardForm(self.driver)

        addCardForm.fillInCardNumber("1234 1234 1234 1234")

        # Assert label about invalid card number is displayed. In Requirements - "Неверный код карты" - but I assume functionally is the same
        self.assertTrue(addCardForm.isinvalidCardNumberLabelDisplayed())

        addCardForm.fillInExpiryDate("03/05")

        # Assert label about invalid card date is displayed
        self.assertTrue(addCardForm.isInvalidCardDateLabelDisplayed())

        # Fill in rest of the form
        addCardForm.fillInCVC("123")
        addCardForm.fillInEmail("alex@mail.ru")

        addCardForm.clickPayButton()

        # Assert label about invalid card form data is displayed
        self.assertTrue(addCardForm.isinvalidFormDataLabelDisplayed())

