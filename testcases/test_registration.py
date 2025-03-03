import time

from page_objects.registration_pageobject import Registration
from utilities.loggen import LogGenerator


class Test_Registration():
    log = LogGenerator.loggen()


    def test_registration(self,setup):
        self.driver= setup
        self.log.info("opening the browser")
        self.rpo=Registration(self.driver)
        self.rpo.Registration()
        self.rpo.First_Name('rahul')
        self.rpo.Last_Name('sharma')
        self.rpo.Email_Address('ashishkumar123@gmail.com')
        self.rpo.Password('rahul@123456')
        self.rpo.Conf_Password('rahul@123456')
        self.rpo.Create_Account()
        if self.rpo.Status()==True:
            print(self.rpo.Message())
            self.driver.save_screenshot(".//screenshots//registration_successful.png")
            time.sleep(1)
            self.rpo.Logout()
        else:
            print('Registration has failed')
            self.driver.save_screenshot(".//screenshots//registration_failure.png")
        print('test case is completed with message')

