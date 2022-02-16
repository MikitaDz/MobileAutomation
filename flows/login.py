from asyncio import wait_for
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Login flow
class Login:
    def __init__(self,driver):
        self.driver = driver

    def loginAsAlrearyLoggedInUser(self):
        ## Skipping onboarding
        skipOnboardingButton = self.driver.instance.find_element_by_android_uiautomator('new UiSelector().text("Пропустить")')
        skipOnboardingButton.click()

        ## Waiting for login button loaded 
        WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((By.ID, "ru.sberbank.sdakit.companion.prod:id/companion_button_text")))

        # Login to the app
        loginButton = self.driver.instance.find_element_by_id('ru.sberbank.sdakit.companion.prod:id/companion_button_text')
        loginButton.click()

        ## Waiting for main screen loaded
        WebDriverWait(self.driver.instance, 15).until(EC.presence_of_element_located((By.ID, "ru.sberbank.sdakit.companion.prod:id/title_card_container")))
