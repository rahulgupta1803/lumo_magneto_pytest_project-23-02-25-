import time

from page_objects.amount_verification_pageobjects import Amount_Verification
from page_objects.checkout_pageobject import Checkout
from page_objects.login_pageobject import Login
from utilities.readconfig import ReadConfig


class Test_Amount_Verification():
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_amount_verification(self,setup):
        self.driver = setup
        self.lpo = Login(self.driver)
        self.cpo = Checkout(self.driver)
        self.avo = Amount_Verification(self.driver)
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
        self.avo.Click_View_Edit_Cart()
        time.sleep(3)
        lm = self.avo.Length_Amount()
        print('length amount',lm)
        time.sleep(2)
        lc = self.avo.Length_Category()
        print('length category',lc)
        cat_list=[]
        amount_list =[]
        time.sleep(3)
        for l in range(1,lm+1):
            amount = self.avo.Amount_iteration(l)
            up_amount = float(amount.replace("$","").replace(",","").replace("-",""))
            amount_list.append(up_amount)
        time.sleep(3)
        for c in range(1,lc+1):
            category = self.avo.Category_iteration(c)
            cat_list.append(category)
        time.sleep(2)
        total_value =self.avo.Text_Order_Total()
        up_total_value = float(total_value.replace("$","").replace(",",""))
        amount_list.append(up_total_value)
        dictionary = dict(zip(cat_list, amount_list))
        print('cat_list',cat_list)
        print('amount_list',amount_list)
        print('dictionary',dictionary)
        exp_total = amount_list[0]-amount_list[1]+amount_list[2]
        if exp_total==up_total_value:
            print("Total is matched")
            assert True
        else:
            print("Total is not matched")
            assert False


