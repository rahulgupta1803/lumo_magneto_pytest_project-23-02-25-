import time

import allure
from allure_commons.types import AttachmentType

from page_objects.login_pageobject import Login
from utilities.excel_sheet import WriteData, RowCount, ReadData
from utilities.loggen import LogGenerator
from utilities.readconfig import ReadConfig


class Test_Login():
    email = ReadConfig().get_email()
    password = ReadConfig.get_password()
    log = LogGenerator().loggen()
    fpath = "D://credence//pytest_projects//lumo_magneto_pytest_project(23-02-25)//testdata//excel//logins_data.xlsx"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://magento.softwaretestingboard.com/")
    @allure.title('test_login')
    @allure.issue('ABC123')
    @allure.story('This is story 1')
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
            allure.attach(self.driver.get_screenshot_as_png(),name=f'{self.email}_{self.password}',attachment_type=AttachmentType.PNG)
            self.log.info('take a screenshot for login success')
            time.sleep(2)
            self.lpo.SignOut()
            self.log.info('click on signout')
        else:
            print('login is failed')
            self.driver.save_screenshot(f".//screenshots//login failed with {self.email}_{self.password}.png")
            allure.attach(self.driver.get_screenshot_as_png(),name=f'{self.email}_{self.password}',attachment_type=AttachmentType.PNG)
            self.log.info('take a screenshot for failed login')

        print('test case is completed')
        self.log.info('test case is completed\n')



    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://magento.softwaretestingboard.com/")
    @allure.title("test_login_param")
    @allure.issue('ABC123')
    @allure.story('This is story 2')
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
            allure.attach(self.driver.get_screenshot_as_png(), name=f"{getloginsdata[0]}_{getloginsdata[1]}_successful",attachment_type=AttachmentType.PNG)
            self.log.info('take a screenshot of successful login')
            print('login is successful')
            self.log.info('print successful message on console\n')
        else:
            self.driver.save_screenshot(f".//screenshots//{getloginsdata[0]}_{getloginsdata[1]}_unsuccessful.png")
            allure.attach(self.driver.get_screenshot_as_png(), name=f"{getloginsdata[0]}_{getloginsdata[1]}_unsuccessful",attachment_type=AttachmentType.PNG)
            self.log.info('take a screenshot of a failed login')
            print('login is failed')
            self.log.info('print failed message on console\n')

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://magento.softwaretestingboard.com/")
    @allure.title("test_login_ddt")
    @allure.issue('ABC123')
    @allure.story('This is story 3')
    def test_login_ddt(self,setup):
        self.driver = setup
        self.log.info('opening the browser')
        self.lpo = Login(self.driver)
        rl = RowCount(self.fpath, "Sheet1")
        self.log.info('count the number of rows in the sheet')
        print('row count is:',rl)
        status =[]
        for r in range(2,rl+1):
            email = ReadData(self.fpath, "Sheet1",r, 2)
            self.log.info('get email from the sheet')
            password = ReadData(self.fpath,"Sheet1",r, 3)
            self.log.info('get password from the sheet')
            exp_result = ReadData(self.fpath, "Sheet1",r,4)
            self.log.info('get expected result from the sheet')
            self.lpo.Signin()
            self.log.info('click on signin')
            self.lpo.Email(email)
            self.log.info('enter email')
            self.lpo.Password(password)
            self.log.info('enter password')
            self.lpo.Click_Signin()
            self.log.info('click on sign in button')
            if self.lpo.Status() == False:
                self.driver.save_screenshot(f".//screenshots//{email}_{password}_successful.png")
                allure.attach(self.driver.get_screenshot_as_png(), name=f"{email}_{password}_successful",attachment_type=AttachmentType.PNG)
                self.log.info('take a screenshot of successful login')
                WriteData(self.fpath,"Sheet1",r, 5, 'correct')
                self.log.info('write correct in actual result column of the excel sheet')
                if exp_result == 'correct':
                    WriteData(self.fpath, "Sheet1",r,6,'Pass')
                    self.log.info('write pass in status column of the sheet')
                    status.append('Pass')
                    self.log.info('append the status list with pass')
                    time.sleep(4)
                    self.lpo.SignOut()
                    self.log.info('click on signout')
                else:
                    WriteData(self.fpath, "Sheet1", r, 6, 'Fail')
                    self.log.info('write fail in status column of the sheet')
                    status.append('Fail')
                    self.log.info('append the status list with fail')
                    time.sleep(4)
                    self.lpo.SignOut()
                    self.log.info('click on signout')
            else:
                self.driver.save_screenshot(f".//screenshots//{email}_{password}_unsuccessful.png")
                allure.attach(self.driver.get_screenshot_as_png(), name=f"{email}_{password}_unsuccessful",attachment_type=AttachmentType.PNG)
                self.log.info('take a screenshot of unsuccessful login')
                WriteData(self.fpath, "Sheet1", r, 5, 'incorrect')
                self.log.info('write incorrect in the actual result column of the sheet')
                if exp_result=='incorrect':
                    WriteData(self.fpath, "Sheet1", r, 6, 'Pass')
                    self.log.info('write pass in the status column of the sheet')
                    status.append('Pass')
                    self.log.info('append the status list with pass')
                else:
                    WriteData(self.fpath, "Sheet1", r, 6, 'Fail')
                    self.log.info('write fail in the status column of the sheet')
                    status.append('Fail')
                    self.log.info('append the list with fail')
        print("status:",status)
        self.log.info('print status list')
        if "Fail" not in status:
            self.log.info('complete the test with assert true\n')
            assert True

        else:
            self.log.info('complete the test with assert false\n')
            assert False


# pytest -v -s D:\credence\pytest_projects\lumo_magneto_pytest_project(23-02-25)\testcases\test_combined_login.py --browser edge --alluredir="D:\credence\pytest_projects\lumo_magneto_pytest_project(23-02-25)\allure_report" --html=html_report/combined_login.html
