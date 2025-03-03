import time

from selenium.webdriver.common.by import By


class Login():
    click_signin_XPATH = (By.XPATH,"/html/body/div[2]/header/div[1]/div/ul/li[2]/a")
    enter_email_ID = (By.ID,"email")
    enter_passowrd_ID = (By.ID,"pass")
    click_signin_button_XPATH = (By.XPATH,"//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]")
    status_failed_XPATH = (By.XPATH,'//*[@id="maincontent"]/div[2]/div[2]/div/div/div')
    click_logout_button_XPATH = (By.XPATH,"/html/body/div[2]/header/div[1]/div/ul/li[2]/span/button")
    click_sign_out_XPATH = (By.XPATH,"/html/body/div[2]/header/div[1]/div/ul/li[2]/div/ul/li[3]/a")
    def __init__(self, driver):
        self.driver = driver

    def Signin(self):
        self.driver.find_element(*Login.click_signin_XPATH).click()
    def Email(self,email):
        self.driver.find_element(*Login.enter_email_ID).send_keys(email)
    def Password(self,password):
        self.driver.find_element(*Login.enter_passowrd_ID).send_keys(password)
    def Click_Signin(self):
        self.driver.find_element(*Login.click_signin_button_XPATH).click()
    def Status(self):
        try:
            self.driver.find_element(*Login.status_failed_XPATH)
            return True
        except:
            return False

    def SignOut(self):
        self.driver.find_element(*Login.click_logout_button_XPATH).click()
        time.sleep(1)
        self.driver.find_element(*Login.click_sign_out_XPATH).click()



        