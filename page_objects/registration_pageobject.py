import time

from selenium.webdriver.common.by import By


class Registration():
    click_registration_XPATH = (By.XPATH,"/html/body/div[2]/header/div[1]/div/ul/li[3]/a")
    enter_first_name_ID = (By.ID,"firstname")
    enter_last_name_ID = (By.ID,"lastname")
    enter_email_ID = (By.ID,"email_address")
    enter_password_ID = (By.ID,"password")
    enter_confirm_password_ID = (By.ID,"password-confirmation")
    click_create_account_XPATH = (By.XPATH ,'//*[@id="form-validate"]/div/div[1]/button/span')
    status_XPATH = (By.XPATH,'//*[@id="maincontent"]/div[1]/div[2]/div/div/div')
    click_on_button_XPATH = (By.XPATH,'/html/body/div[2]/header/div[1]/div/ul/li[2]/span/button')
    click_on_signout_XPATH = (By.XPATH,'/html/body/div[2]/header/div[1]/div/ul/li[2]/div/ul/li[3]/a')

    def __init__(self,driver):
        self.driver = driver

    def Registration(self):
        self.driver.find_element(*Registration.click_registration_XPATH).click()

    def First_Name(self, first_name):
        self.driver.find_element(*Registration.enter_first_name_ID).send_keys(first_name)

    def Last_Name(self, last_name):
        self.driver.find_element(*Registration.enter_last_name_ID).send_keys(last_name)

    def Email_Address(self, email):
        self.driver.find_element(*Registration.enter_email_ID).send_keys(email)

    def Password(self, password):
        self.driver.find_element(*Registration.enter_password_ID).send_keys(password)

    def Conf_Password(self, password):
        self.driver.find_element(*Registration.enter_confirm_password_ID).send_keys(password)

    def Create_Account(self):
        self.driver.find_element(*Registration.click_create_account_XPATH).click()

    def Status(self):
        try:
            self.driver.find_element(*Registration.status_XPATH)

            return True
        except:
            return False

    def Message(self):
        message = self.driver.find_element(*Registration.status_XPATH).text
        return message

    def Logout(self):
        self.driver.find_element(*Registration.click_on_button_XPATH).click()
        time.sleep(1)
        self.driver.find_element(*Registration.click_on_signout_XPATH).click()
