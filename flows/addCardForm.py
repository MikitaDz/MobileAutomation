from asyncio import wait_for
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Add card form flow
class AddCardForm:
    def __init__(self,driver):
        self.driver = driver

    # Using XPATH as elements below are NAF and no better ways to select it (despite having id). In real world would ask development to fix it 
    # input card number 
    def fillInCardNumber(self, cardNumber):
        cardNumberInput = self.driver.instance.find_element_by_xpath("//android.widget.EditText[@resource-id='pan']")
        cardNumberInput.send_keys(cardNumber)
    
    # input card date
    def fillInExpiryDate(self, expDate):
        cardNumberDateInput = self.driver.instance.find_element_by_xpath("//android.widget.EditText[@resource-id='expiry']")
        cardNumberDateInput.send_keys(expDate)

    # input cvc/cvv
    def fillInCVC(self, cvc):
        cardCVCInput = self.driver.instance.find_element_by_xpath("//android.widget.EditText[@resource-id='cvc']")
        cardCVCInput.send_keys(cvc)

    # input email
    def fillInEmail(self, email):
        emailInput = self.driver.instance.find_element_by_xpath("//android.widget.EditText[@resource-id='email']")
        emailInput.send_keys("123@yandex.ru")

    # Click pay button
    def clickPayButton(self):
        payButton = self.driver.instance.find_element_by_android_uiautomator('new UiSelector().text("Оплатить")')
        payButton.click()

    def isinvalidCardNumberLabelDisplayed(self) -> bool:
        invalidCardNumberLabel = self.driver.instance.find_element_by_android_uiautomator('new UiSelector().text("Неверный номер карты")')
        return invalidCardNumberLabel.is_displayed()

    def isInvalidCardDateLabelDisplayed(self) -> bool:
        invalidCardDateLabel = self.driver.instance.find_element_by_android_uiautomator('new UiSelector().text("Неверная дата")')
        return invalidCardDateLabel.is_displayed()

    def isinvalidFormDataLabelDisplayed(self) -> bool:
        invalidFormDataLabel = self.driver.instance.find_element_by_android_uiautomator('new UiSelector().text("Проверьте правильность заполнения платежной формы")')
        return invalidFormDataLabel.is_displayed()
