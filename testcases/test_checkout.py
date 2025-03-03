import time

from page_objects.checkout_pageobject import Checkout
from page_objects.login_pageobject import Login
from utilities.loggen import LogGenerator
from utilities.readconfig import ReadConfig


class Test_Checkout():
    log = LogGenerator.loggen()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()


    def test_checkout(self, setup):
        self.driver = setup
        self.lpo =Login(self.driver)
        self.cpo = Checkout(self.driver)
        self.lpo.Signin()
        self.lpo.Email(self.email)
        self.lpo.Password(self.password)
        self.lpo.Click_Signin()
        self.cpo.women_top_jacket_section()
        self.cpo.Click_olivia_light_jacket()
        self.cpo.Quantity_Olivia_Jacket(2)
        self.cpo.Colour_Olivia_Jacket()
        self.cpo.Size_Olivia_Jacket()
        self.cpo.Add_Cart_Olivia_Jacket()
        self.cpo.women_bottom_pants_section()
        self.cpo.Click_Portia_Capri_Pants()
        self.cpo.Quantity_Portia_Capri_Pants(3)
        self.cpo.Colour_Portia_Capri_Pants()
        self.cpo.Size_Portia_Capri_Pants()
        self.cpo.Add_Cart_Portia_Capri_Pants()
        self.cpo.men_tops_jacket_section()
        self.cpo.Click_Proteus_Fitness_Jacket()
        self.cpo.Quantity_Proteus_Fitness_Jacket(4)
        self.cpo.Colour_Proteus_Fitness_Jacket()
        self.cpo.Size_Proteus_Fitness_Jacket()
        self.cpo.Add_Cart_Proteus_Fitness_Jacket()
        self.cpo.men_bottom_pants_section()
        self.cpo.Click_Cronus_Yoga_Pant()
        self.cpo.Quantity_Cronus_Yoga_Pant(5)
        self.cpo.Colour_Cronus_Yoga_Pant()
        self.cpo.Size_Cronus_Yoga_Pant()
        self.cpo.Add_Cart_Cronus_Yoga_Pant()
        self.cpo.CLick_Cart()
        self.cpo.Click_Proceed_To_Checkout()
        time.sleep(2)
        self.cpo.Click_New_Address()
        # time.sleep(3)
        # self.cpo.Switch_Window()
        # time.sleep(2)
        self.cpo.Enter_Company_Name('home')
        self.cpo.Enter_Street_Address('121/3, Roorkee')
        self.cpo.Enter_City('Raipur')
        self.cpo.Select_Country('India')
        self.cpo.Select_State('Chhattisgarh')
        self.cpo.Enter_Zip_Code('324567')
        self.cpo.Enter_Phone_Number('9876876543')
        self.cpo.Click_Ship_Here()
        self.cpo.Select_Shipping_Method()
        self.cpo.Click_Next()
        self.cpo.Click_Place_Order()
        if self.cpo.Status()==True:
            print(self.cpo.Message())
            print(self.cpo.Order_Number())
            self.driver.save_screenshot(".//screenshots//order_placed_successfully.png")
        else:
            print('Order has not been confirmed')
            self.driver.save_screenshot(".//screenshots//order_not_placed.png")



