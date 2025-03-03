from page_objects.login_pageobject import Login
from utilities.loggen import LogGenerator


class Test_Login_Param():
    log = LogGenerator.loggen()

    def test_login_param(self,setup, getloginsdata):
        self.driver=setup
        self.log.info('open the browser')
        self.lpo = Login(self.driver)
        self.lpo.Signin()
        self.log.info('click on sign in')
        self.lpo.Email(getloginsdata[0])
        self.log.info('enter the email')
        self.lpo.Password(getloginsdata[1])
        self.log.info('enter the password')
        self.lpo.Click_Signin()
        self.log.info('click on sign in button')
        if self.lpo.Status()== False:
            self.driver.save_screenshot(f".//screenshots//{getloginsdata[0]}_{getloginsdata[1]}_successful.png")
            self.log.info('take a screenshot of successful login')
            print('login is successful')
            self.log.info('print successful message on console\n')
        else:
            self.driver.save_screenshot(f".//screenshots//{getloginsdata[0]}_{getloginsdata[1]}_unsuccessful.png")
            self.log.info('take a screenshot of a failed login')
            print('login is failed')
            self.log.info('print failed message on console\n')



