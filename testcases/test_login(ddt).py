import time

from page_objects.login_pageobject import Login
from utilities.excel_sheet import ReadData, RowCount, WriteData
from utilities.loggen import LogGenerator


class Test_Login_ddt():
    fpath = "D://credence//pytest_projects//lumo_magneto_pytest_project(23-02-25)//testdata//excel//logins_data.xlsx"
    log = LogGenerator.loggen()

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





