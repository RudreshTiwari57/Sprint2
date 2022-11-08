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





class SEARCH(BaseSettingsPage):


    def __init__(self,driver):
        super().__init__(driver)



    def text_Searchbar(self, searchTEXT):
        global lk
        lk = searchTEXT
        self.DynamicImplicitWait(40)
        self.TypeEditBox("SEARCHBAR_XPATH", searchTEXT)


    def Click_SEARCHBUTTON(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("SEARCHBUTTON_CSSSELECTOR")