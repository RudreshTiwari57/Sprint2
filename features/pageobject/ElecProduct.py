import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.configreader import ConfigReader
from features.pageobject.Base import BaseSettingsPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import configreader
from selenium.webdriver import ActionChains
import random


class ELEC_Product(BaseSettingsPage):

    def __init__(self,driver):
        self.driver = driver
    #
    #
    # def OpenURl(self):
    #     self.driver.get(ConfigReader("base info","URL"))
    #     self.DynamicImplicitWait(40)
    #
    #
    #
    #
    # def Enter_Username(self,nunber):
    #     self.DynamicImplicitWait(40)
    #     self.TypeEditBox("USERNAME_XPATH", nunber)
    #
    #
    # def Enter_password(self,password):
    #     self.DynamicImplicitWait(40)
    #     self.TypeEditBox("PASSWORD_XPATH", password)
    #
    #
    #
    # def Click_login(self):
    #     self.DynamicImplicitWait(40)
    #     self.ClickButton("LOGINBUTTON_CSSSELECTOR")


    # def text_Searchbar(self,searchTEXT):
    #     global lk
    #     lk = searchTEXT
    #     self.DynamicImplicitWait(40)
    #     self.TypeEditBox("SEARCHBAR_XPATH",searchTEXT)
    #
    # def Click_SEARCHBUTTON(self):
    #     self.DynamicImplicitWait(40)
    #     self.ClickButton("SEARCHBUTTON_CSSSELECTOR")

    def Click_product(self):
        self.DynamicImplicitWait(40)
        #self.driver = webdriver.Chrome(ChromeDriverManager().install())
        AA = self.driver.find_elements(By.CLASS_NAME,"col-7-12")
        pp = random.choice(AA)
        pp.click()



    def SWITCHWINDOW(self):
        #self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.DynamicImplicitWait(40)
        self.SWITCH_WINDOW(1)



    def CLICK_IMAGES(self):
        self.DynamicImplicitWait(40)
        #self.driver = webdriver.Chrome(ChromeDriverManager().install())
        AA = self.driver.find_elements(By.CLASS_NAME,"_1AuMiq")
        count = 0
        if len(AA)>5:
            while count<=5:
                AA[count].click()
                time.sleep(2)
                count+= 1
        else:
            for i in AA:
                i.click()
                time.sleep(2)




    def Enter_PinCode(self,pincode):
        #self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.DynamicImplicitWait(40)
        self.driver.execute_script("window.scrollBy(0,400)")
        self.Clear_Text("PINCODE_CSSSELECTOR")
        self.TypeEditBox("PINCODE_CSSSELECTOR",pincode)


    def Click_oncheck(self,lk):
        if lk == "Mobile":
            self.DynamicImplicitWait(40)
            time.sleep(3)
            self.ClickButton("CHECKBUTTON_CSSSELECTOR")

        if lk == "tv":
            self.DynamicImplicitWait(40)
            time.sleep(3)
            self.ClickButton("CHECKBUTTONTV_CSSSELECTOR")

        if lk == "laptop":
            self.DynamicImplicitWait(40)
            time.sleep(3)
            self.ClickButton("CHECKBUTTONlaptop_CSSSELECTOR")


        if lk == "Mobile":
            self.DynamicImplicitWait(40)
            time.sleep(3)
            self.ClickButton("CHECKBUTTON_CSSSELECTOR")




    def CLick_WISHLIST(self):
        #self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.DynamicImplicitWait(40)
        self.driver.execute_script("window.scrollBy(0,-400)")
        time.sleep(5)
        move = ActionChains(self.driver)
        move.move_to_element(self.driver.find_element(By.XPATH,"//*[name()='svg']/*[name()='path' and @class='eX72wL']"))
        move.click(self.driver.find_element(By.XPATH,"//*[name()='svg']/*[name()='path' and @class='eX72wL']"))
        move.perform()


    def specifactions(self):
        self.driver.execute_script("window.scrollBy(0,2200)")
        A = ActionChains(self.driver)
        A.click(self.driver.find_element(By.CLASS_NAME, "_1FH0tX"))
        A.perform()
        time.sleep(3)













