from asyncio import wait_for
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Profile flow
class Profile:
    def __init__(self,driver):
        self.driver = driver

    def openProfile(self):
        # Press on the gear button
        # Using XPATH as element is NAF and no better ways to select it. In real world would ask development to fix it 
        WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((By.XPATH, "//androidx.cardview.widget.CardView[@index='0']//android.widget.LinearLayout[@index='1']")))
        gearButton = self.driver.instance.find_element_by_xpath("//androidx.cardview.widget.CardView[@index='0']/android.widget.LinearLayout[@index='0']/android.widget.LinearLayout[@index='1']/android.widget.LinearLayout[@index='1']")
        gearButton.click()
    
    def openProfilePayments(self):
        ## Waiting for payments screen loaded
        paymentsMenuItem = self.driver.instance.find_element_by_android_uiautomator('new UiSelector().text("Платежи")')
        paymentsMenuItem.click()

        # Wait for cards list to be loaded
        self.driver.instance.implicitly_wait(5)

    def openNewCardForm(self):
        addCardButton = self.driver.instance.find_element_by_android_uiautomator('new UiSelector().text("Добавить карту")')
        addCardButton.click()

        # Wait for form to be loaded
        WebDriverWait(self.driver.instance, 15).until(EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@resource-id='pan']")))
