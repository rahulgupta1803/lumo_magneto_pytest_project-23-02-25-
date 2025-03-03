import time

from page_objects.login_pageobject import Login
from utilities.loggen import LogGenerator
from utilities.readconfig import ReadConfig


class Test_Login():
    email = ReadConfig().get_email()
    password = ReadConfig.get_password()
    log = LogGenerator().loggen()

    def test_login(self,setup):
        self.driver = setup
        self.log.info('opening the browser')
        self.lpo = Login(self.driver)
        self.lpo.Signin()
        self.log.info('click on sign in')
        self.lpo.Email(self.email)
        self.log.info('enter email id')
        self.lpo.Password(self.password)
        self.log.info('enter password')
        self.lpo.Click_Signin()
        self.log.info('click on sign in button')
        if self.lpo.Status()==False:
            print('login is successful')
            time.sleep(2)
            self.driver.save_screenshot(f".//screenshots/login successful with {self.email}_{self.password}.png")
            self.log.info('take a screenshot for login success')
            time.sleep(2)
            self.lpo.SignOut()
            self.log.info('click on signout')
        else:
            print('login is failed')
            self.driver.save_screenshot(f".//screenshots//login failed with {self.email}_{self.password}.png")
            self.log.info('take a screenshot for failed login')

        print('test case is completed')
        self.log.info('test case is completed\n')

