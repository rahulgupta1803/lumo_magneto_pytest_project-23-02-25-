from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Amount_Verification():
    click_view_and_edit_cart_XPATH = (By.XPATH,"//span[normalize-space()='View and Edit Cart']")
    length_category_XPATH = (By.XPATH,'//*[@id="cart-totals"]/div/table/tbody/tr/th')
    length_amount_XPATH = (By.XPATH,'//*[@id="cart-totals"]/div/table/tbody/tr/td/span')
    text_order_total_XPATH = (By.XPATH,'//*[@id="cart-totals"]/div/table/tbody/tr[4]/td/strong/span')





    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)


    def Click_View_Edit_Cart(self):
        self.driver.find_element(*Amount_Verification.click_view_and_edit_cart_XPATH).click()

    def Category_iteration(self,a):
        m = self.driver.find_element(By.XPATH,'//*[@id="cart-totals"]/div/table/tbody/tr['+str(a)+']/th').text
        return m

    def Amount_iteration(self,b):
        m = self.driver.find_element(By.XPATH,'//*[@id="cart-totals"]/div/table/tbody/tr['+str(b)+']/td/span').text
        return m

    def Length_Amount(self):
        m=len(self.driver.find_elements(*Amount_Verification.length_amount_XPATH))
        return m

    def Length_Category(self):
        m=len(self.driver.find_elements(*Amount_Verification.length_category_XPATH))
        return m

    def Text_Order_Total(self):
        order = self.driver.find_element(*Amount_Verification.text_order_total_XPATH).text
        return order