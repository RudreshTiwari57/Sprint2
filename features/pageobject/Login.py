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




class LOGIN(BaseSettingsPage):

    def __init__(self,driver):
        self.driver = driver


    def OpenURl(self):
        self.driver.get(ConfigReader("base info","URL"))
        self.DynamicImplicitWait(40)




    def Enter_Username(self,nunber):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("USERNAME_XPATH", nunber)


    def Enter_password(self,password):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("PASSWORD_XPATH", password)



    def Click_login(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("LOGINBUTTON_CSSSELECTOR")

