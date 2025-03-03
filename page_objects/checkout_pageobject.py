import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Checkout():
    # -----womens category--------------------------
    click_olivia_light_jacket_XPATH = (By.XPATH,"/html[1]/body[1]/div[2]/main[1]/div[3]/div[1]/div[3]/ol[1]/li[1]/div[1]/div[1]/strong[1]/a[1]")
    quantity_olivia_light_jacket_XPATH=(By.XPATH,'//*[@id="qty"]')
    size_olivia_light_jacket_ID = (By.ID,'option-label-size-143-item-168')
    colour_olivia_light_jacket_ID = (By.ID,'option-label-color-93-item-49')
    add_cart_olivia_jacket_XPATH = (By.XPATH,'//*[@id="product-addtocart-button"]/span')

    click_portia_capri_pants_XPATH = (By.XPATH,"//a[normalize-space()='Portia Capri']")
    quantity_portia_capri_pants_ID = (By.ID,'qty')
    colour_portia_capri_pants_ID = (By.ID,'option-label-color-93-item-50')
    size_portia_capri_pants_ID = (By.ID, 'option-label-size-143-item-171')
    add_cart_portia_capri_pants_XPATH = (By.XPATH, '//*[@id="product-addtocart-button"]/span')

    # ---------mens category---------------------------------------------------
    
    click_proteus_fitness_jacket_XPATH = (By.XPATH,"/html[1]/body[1]/div[2]/main[1]/div[3]/div[1]/div[3]/ol[1]/li[1]/div[1]/div[1]/strong[1]/a[1]")
    quantity_proteus_fitness_jacket_XPATH = (By.XPATH, '//*[@id="qty"]')
    size_proteus_fitness_jacket_ID = (By.ID, 'option-label-size-143-item-168')
    colour_proteus_fitness_jacket_ID = (By.ID, 'option-label-color-93-item-56')
    add_cart_proteus_fitness_jacket_XPATH = (By.XPATH, '//*[@id="product-addtocart-button"]/span')

    click_cronus_yoga_pant_XPATH = (By.XPATH,"//a[normalize-space()='Cronus Yoga Pant']")
    quantity_cronus_yoga_pant_XPATH = (By.XPATH, "//input[@id='qty']")
    size_cronus_yoga_pant_XPATH = (By.XPATH, "//div[@id='option-label-size-143-item-177']")
    colour_cronus_yoga_pant_XPATH = (By.XPATH, "//div[@id='option-label-color-93-item-49']")
    add_cart_cronus_yoga_pant_XPATH = (By.XPATH, "//button[@id='product-addtocart-button']")

    # -------procced to payment-----------------------------------
    click_cart_XPATH = (By.XPATH,"//a[@class='action showcart']")
    click_proceed_to_checkout_XPATH = (By.XPATH,"//button[@id='top-cart-btn-checkout']")
    click_new_address_XPATH = (By.XPATH, "//span[normalize-space()='New Address']")
    enter_company_name_XPATH = (By.XPATH, "/html[1]/body[1]/div[3]/aside[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[3]/div[1]/input[1]")
    enter_street_address_XPATH = (By.XPATH, "/html[1]/body[1]/div[3]/aside[2]/div[2]/div[1]/div[1]/form[1]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/input[1]")
    enter_city_XPATH = (By.XPATH, "/html[1]/body[1]/div[3]/aside[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/input[1]")
    select_state_XPATH = (By.XPATH, "/html[1]/body[1]/div[3]/aside[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[5]/div[1]/select[1]")
    enter_zip_code_XPATH = (By.XPATH, "/html[1]/body[1]/div[3]/aside[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[7]/div[1]/input[1]")
    select_country_XPATH = (By.XPATH, "/html[1]/body[1]/div[3]/aside[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[8]/div[1]/select[1]")
    enter_phone_number_XPATH = (By.XPATH, "/html[1]/body[1]/div[3]/aside[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[9]/div[1]/input[1]")
    click_ship_here_CSS = (By.CSS_SELECTOR,".action.primary.action-save-address")
    select_shipping_method_XPATH = (By.XPATH, "//input[@name='ko_unique_2']")
    click_next_XPATH = (By.XPATH, "//button[@class='button action continue primary']")
    click_place_order_XPATH = (By.XPATH,"/html[1]/body[1]/div[3]/main[1]/div[2]/div[1]/div[2]/div[4]/ol[1]/li[3]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[4]/div[1]/button[1]")
    message_XPATH = (By.XPATH,"//span[@class='base']")
    order_number_XPATH = (By.XPATH,"//div[@class='page-wrapper']//p[1]")





    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,20)

    # -------------------hover actions ---------

    def women_top_jacket_section(self):
        a=ActionChains(self.driver)
        m=self.driver.find_element(By.ID,'ui-id-4')
        n=self.driver.find_element(By.ID,'ui-id-9')
        p=self.driver.find_element(By.XPATH,'//*[@id="ui-id-11"]/span')
        a.move_to_element(m).move_to_element(n).perform()
        a.move_to_element(p).click().perform()

    def women_bottom_pants_section(self):
        a = ActionChains(self.driver)
        m = self.driver.find_element(By.ID, 'ui-id-4')
        n = self.driver.find_element(By.XPATH, '//*[@id="ui-id-10"]/span[2]')
        p = self.driver.find_element(By.XPATH, '//*[@id="ui-id-15"]/span')
        a.move_to_element(m).move_to_element(n).perform()
        a.move_to_element(p).click().perform()

    def men_tops_jacket_section(self):
        a=ActionChains(self.driver)
        m=self.driver.find_element(By.XPATH,'//*[@id="ui-id-5"]/span[2]')
        n=self.driver.find_element(By.ID,'ui-id-17')
        p=self.driver.find_element(By.XPATH,'//*[@id="ui-id-19"]/span')
        a.move_to_element(m).move_to_element(n).perform()
        a.move_to_element(p).click().perform()

    def men_bottom_pants_section(self):
        a=ActionChains(self.driver)
        m = self.driver.find_element(By.XPATH, '//*[@id="ui-id-5"]/span[2]')
        n = self.driver.find_element(By.XPATH, "//a[@id='ui-id-18']//span[contains(text(),'Bottoms')]")
        p = self.driver.find_element(By.XPATH, "//a[@id='ui-id-23']")
        a.move_to_element(m).move_to_element(n).perform()
        a.move_to_element(p).click().perform()

    # ----- category-------------------
    def Click_olivia_light_jacket(self):
        self.driver.find_element(*Checkout.click_olivia_light_jacket_XPATH).click()

    def Quantity_Olivia_Jacket(self,x):
        self.driver.find_element(*Checkout.quantity_olivia_light_jacket_XPATH).clear()
        time.sleep(1)
        self.driver.find_element(*Checkout.quantity_olivia_light_jacket_XPATH).send_keys(x)

    def Size_Olivia_Jacket(self):
        self.driver.find_element(*Checkout.size_olivia_light_jacket_ID).click()

    def Colour_Olivia_Jacket(self):
        self.driver.find_element(*Checkout.colour_olivia_light_jacket_ID).click()

    def Add_Cart_Olivia_Jacket(self):
        self.driver.find_element(*Checkout.add_cart_olivia_jacket_XPATH).click()

    def Click_Portia_Capri_Pants(self):
        self.driver.find_element(*Checkout.click_portia_capri_pants_XPATH).click()

    def Quantity_Portia_Capri_Pants(self,q):
        self.driver.find_element(*Checkout.quantity_portia_capri_pants_ID).clear()
        time.sleep(1)
        self.driver.find_element(*Checkout.quantity_portia_capri_pants_ID).send_keys(q)

    def Size_Portia_Capri_Pants(self):
        self.driver.find_element(*Checkout.size_portia_capri_pants_ID).click()

    def Colour_Portia_Capri_Pants(self):
        self.driver.find_element(*Checkout.colour_portia_capri_pants_ID).click()

    def Add_Cart_Portia_Capri_Pants(self):
        self.driver.find_element(*Checkout.add_cart_portia_capri_pants_XPATH).click()

    def Click_Proteus_Fitness_Jacket(self):
        self.driver.find_element(*Checkout.click_proteus_fitness_jacket_XPATH).click()


    def Quantity_Proteus_Fitness_Jacket(self,q):
        self.driver.find_element(*Checkout.quantity_proteus_fitness_jacket_XPATH).clear()
        time.sleep(1)
        self.driver.find_element(*Checkout.quantity_proteus_fitness_jacket_XPATH).send_keys(q)

    def Size_Proteus_Fitness_Jacket(self):
        self.driver.find_element(*Checkout.size_proteus_fitness_jacket_ID).click()

    def Colour_Proteus_Fitness_Jacket(self):
        self.driver.find_element(*Checkout.colour_proteus_fitness_jacket_ID).click()

    def Add_Cart_Proteus_Fitness_Jacket(self):
        self.driver.find_element(*Checkout.add_cart_proteus_fitness_jacket_XPATH).click()


    def Click_Cronus_Yoga_Pant(self):
        self.driver.find_element(*Checkout.click_cronus_yoga_pant_XPATH).click()

    def Quantity_Cronus_Yoga_Pant(self,q):
        self.driver.find_element(*Checkout.quantity_cronus_yoga_pant_XPATH).clear()
        time.sleep(1)
        self.driver.find_element(*Checkout.quantity_cronus_yoga_pant_XPATH).send_keys(q)

    def Colour_Cronus_Yoga_Pant(self):
        self.driver.find_element(*Checkout.colour_cronus_yoga_pant_XPATH).click()

    def Size_Cronus_Yoga_Pant(self):
        self.driver.find_element(*Checkout.size_cronus_yoga_pant_XPATH).click()

    def Add_Cart_Cronus_Yoga_Pant(self):
        self.driver.find_element(*Checkout.add_cart_cronus_yoga_pant_XPATH).click()

    def CLick_Cart(self):
        self.driver.find_element(*Checkout.click_cart_XPATH).click()

    def Click_Proceed_To_Checkout(self):
        self.driver.find_element(*Checkout.click_proceed_to_checkout_XPATH).click()

    def Click_New_Address(self):
        self.driver.find_element(*Checkout.click_new_address_XPATH).click()

    def Enter_Company_Name(self,name):
        self.wait.until(EC.visibility_of_element_located(self.enter_company_name_XPATH)).send_keys(name)
        # self.driver.find_element(*Checkout.enter_company_name_XPATH).send_keys(name)

    def Enter_Street_Address(self,address):
        self.wait.until(EC.visibility_of_element_located(self.enter_street_address_XPATH)).send_keys(address)
        # self.driver.find_element(*Checkout.enter_street_address_XPATH).send_keys(address)

    def Enter_City(self,city):
        self.wait.until(EC.visibility_of_element_located(self.enter_city_XPATH)).send_keys(city)
        # self.driver.find_element(*Checkout.enter_city_XPATH).send_keys(city)

    def Select_Country(self,x):
        country = Select(self.wait.until(EC.visibility_of_element_located(self.select_country_XPATH)))
        country.select_by_visible_text(x)

    def Select_State(self, x):
        state = Select(self.wait.until(EC.visibility_of_element_located(self.select_state_XPATH)))
        state.select_by_visible_text(x)

    def Enter_Zip_Code(self,zip):
        self.wait.until(EC.visibility_of_element_located(self.enter_zip_code_XPATH)).send_keys(zip)

    def Enter_Phone_Number(self, number):
        self.wait.until(EC.visibility_of_element_located(self.enter_phone_number_XPATH)).send_keys(number)

    def Click_Ship_Here(self):
        self.wait.until(EC.element_to_be_clickable(self.click_ship_here_CSS)).click()
    def Select_Shipping_Method(self):
        self.wait.until(EC.element_to_be_clickable(self.select_shipping_method_XPATH)).click()
        # self.driver.find_element(*Checkout.select_shipping_method_XPATH).click()

    def Click_Next(self):
        self.wait.until(EC.element_to_be_clickable(self.click_next_XPATH)).click()
        # self.driver.find_element(*Checkout.click_next_XPATH).click()

    def Click_Place_Order(self):
        m=self.wait.until(EC.visibility_of_element_located(self.click_place_order_XPATH))
        # self.wait.until(EC.element_to_be_clickable(self.click_place_order_XPATH)).click()
        # self.driver.find_element(*Checkout.click_place_order_XPATH).click()
        self.driver.execute_script("arguments[0].click();",m)

    def Message(self):
        mess = self.wait.until(EC.visibility_of_element_located(self.message_XPATH)).text
        return mess

    def Order_Number(self):
        order = self.wait.until(EC.visibility_of_element_located(self.order_number_XPATH)).text
        return order


    def Status(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.order_number_XPATH))
            return True
        except:
            return False








