from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from Utilities import configreader
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC


class BaseSettingsPage:

    def __init__(self, driver):
        self.driver = driver


    # KeyWord Driver approach
    def TypeEditBox(self, locator, typeValue):
        if str(locator).endswith("_ID"):
            time.sleep(3)
            WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.ID, configreader.ConfigReader("locators", locator))))
            self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).click()
            # time.sleep(5)
            WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.ID, configreader.ConfigReader("locators", locator))))
            self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).send_keys(typeValue)
        elif str(locator).endswith("_NAME"):
            time.sleep(3)
            WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.NAME, configreader.ConfigReader("locators", locator))))
            self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).click()
            # time.sleep(5)
            WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.NAME, configreader.ConfigReader("locators", locator))))

            self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).send_keys(typeValue)
        elif str(locator).endswith("_CLASS"):
            time.sleep(3)
            WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.CLASS_NAME, configreader.ConfigReader("locators", locator))))
            self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).click()
            # time.sleep(5)
            WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.CLASS_NAME, configreader.ConfigReader("locators", locator))))
            self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).send_keys(typeValue)
        elif str(locator).endswith("_XPATH"):
            time.sleep(3)
            WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.XPATH,configreader.ConfigReader("locators", locator ))))
            self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).click()
            # time.sleep(5)
            WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.XPATH, configreader.ConfigReader("locators", locator))))
            self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).send_keys(typeValue)
        elif str(locator).endswith("_CSSSELECTOR"):
            time.sleep(3)
            WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.CSS_SELECTOR, configreader.ConfigReader("locators", locator))))
            self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).click()
            # time.sleep(5)
            WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.CSS_SELECTOR, configreader.ConfigReader("locators", locator))))
            self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).send_keys(typeValue)

    # KeyWord Driver approach
    #  https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html?highlight=keys#module-selenium.webdriver.common.keys
    def EnterButtonEditBoxEmail(self, locator):
        if str(locator).endswith("_ID"):
            self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).send_keys(Keys.RETURN)
        elif str(locator).endswith("_NAME"):
            self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).send_keys(Keys.RETURN)
        elif str(locator).endswith("_CLASS"):
            self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).send_keys(Keys.RETURN)
        elif str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).send_keys(Keys.RETURN)
        elif str(locator).endswith("_CSSSELECTOR"):
            self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).send_keys(Keys.RETURN)


    # KeyWord Driver approach
    def ClickRadio(self, locator):
        global val
        if str(locator).endswith("_ID"):
            val = self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).is_selected()
            if val == False:
                self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).click()
        elif str(locator).endswith("_NAME"):
            val = self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).is_selected()
            if val == False:
                self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).click()

        elif str(locator).endswith("_CLASS"):
            val = self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).is_selected()
            if val == False:
                self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).click()

        elif str(locator).endswith("_XPATH"):
            val = self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).is_selected()
            if val == False:
                self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).click()

        elif str(locator).endswith("_CSSSELECTOR"):
            val = self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).is_selected()
            if val == False:
                self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).click()

    # KeyWord Driver approach
    def ClickCheckbox(self, locator):
        global val
        if str(locator).endswith("_ID"):
            val = self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).is_selected()
            if val == False:
                self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).click()
            elif val == True:
                pass
        elif str(locator).endswith("_NAME"):
            val = self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).is_selected()
            if val == False:
                self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).click()
            elif val == True:
                pass
        elif str(locator).endswith("_CLASS"):
            val = self.driver.find_element_by_class_name(
                configreader.ConfigReader("locators", locator)).is_selected()
            if val == False:
                self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).click()
            elif val == True:
                pass
        elif str(locator).endswith("_XPATH"):
            val = self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).is_selected()
            if val == False:
                self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).click()
            elif val == True:
                pass
        elif str(locator).endswith("_CSSSELECTOR"):
            val = self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).is_selected()
            if val == False:
                self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).click()
            elif val == True:
                pass

    # KeyWord Driver approach
    def ClickButton(self, locator):
        max = 5
        att =0
        while True:
            try:
                if str(locator).endswith("_ID"):
                    time.sleep(5)
                    WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.ID, configreader.ConfigReader("locators", locator))))
                    self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).click()
                    return
                elif str(locator).endswith("_NAME"):
                    time.sleep(5)
                    WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.NAME, configreader.ConfigReader("locators", locator))))
                    self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).click()
                    return
                elif str(locator).endswith("_CLASS"):
                    time.sleep(5)
                    WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.CLASS_NAME, configreader.ConfigReader("locators", locator))))
                    self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).click()
                    return
                elif str(locator).endswith("_XPATH"):
                    time.sleep(5)
                    WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.XPATH, configreader.ConfigReader("locators", locator))))
                    self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).click()
                    return
                elif str(locator).endswith("_CSSSELECTOR"):
                    time.sleep(5)
                    WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.CSS_SELECTOR, configreader.ConfigReader("locators", locator))))
                    self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).click()
                    return
            except StaleElementReferenceException:
                if att == max:
                    raise
                att+= 1


    # KeyWord Driver approach
    def ClickLinks(self, locator):
        if str(locator).endswith("_ID"):
            self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).click()
        elif str(locator).endswith("_NAME"):
            self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).click()

        elif str(locator).endswith("_CLASS"):
            self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).click()

        elif str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).click()

        elif str(locator).endswith("_CSSSELECTOR"):
            self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).click()

        elif str(locator).endswith("_LINKTEXT"):
            self.driver.find_element_by_link_text(configreader.ConfigReader("locators", locator)).click()

        elif str(locator).endswith("_PARTIALLINKTEXT"):
            self.driver.find_element_by_partial_link_text(configreader.ConfigReader("locators", locator)).click()



    # KeyWord Driver approach
    def SwitchFrameAddress(self, locator):
        global addressFrame
        if str(locator).endswith("_ID"):
            addressFrame = self.driver.find_element_by_id(configreader.ConfigReader("locators", locator))
            self.driver.switch_to.frame(addressFrame)
        elif str(locator).endswith("_NAME"):
            addressFrame = self.driver.find_element_by_name(configreader.ConfigReader("locators", locator))
            self.driver.switch_to.frame(addressFrame)
        elif str(locator).endswith("_CLASS"):
            addressFrame = self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator))
            self.driver.switch_to.frame(addressFrame)
        elif str(locator).endswith("_XPATH"):
            addressFrame = self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator))
            self.driver.switch_to.frame(addressFrame)
        elif str(locator).endswith("_CSSSELECTOR"):
            addressFrame = self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator))
            self.driver.switch_to.frame(addressFrame)

    # Switch out of frame to main page
    def SwitchOutFrameAddress(self):
        self.driver.switch_to.default_content()

    # Implicit wait
    def DynamicImplicitWait(self, timePeriod):
        self.driver.implicitly_wait(timePeriod)

    # Static Wait:
    def StaticWait(self, timePeriod):
        time.sleep(timePeriod)


    def AssertTitle(self, extectedTitle):
        valTitle = self.driver.title
        assert valTitle == extectedTitle

    def AssertText(self, locator, expectedTextVal):
        if str(locator).endswith("_ID"):
            actualTextVal = self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).text
            assert expectedTextVal in actualTextVal
        elif str(locator).endswith("_NAME"):
            actualTextVal = self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).text
            assert expectedTextVal in actualTextVal
        elif str(locator).endswith("_CLASS"):
            actualTextVal = self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).text
            assert expectedTextVal in actualTextVal
        elif str(locator).endswith("_XPATH"):
            actualTextVal = self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).text
            assert expectedTextVal in actualTextVal
        elif str(locator).endswith("_CSSSELECTOR"):
            actualTextVal = self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).text
            assert expectedTextVal in actualTextVal
        elif str(locator).endswith("_TAGNAME"):
            actualTextVal = self.driver.find_element_by_tag_name(configreader.ConfigReader("locators", locator)).text
            assert expectedTextVal in actualTextVal
        elif str(locator).endswith("_LINKTEXT"):
            actualTextVal = self.driver.find_element_by_link_text(configreader.ConfigReader("locators", locator)).text
            assert expectedTextVal in actualTextVal
        elif str(locator).endswith("_PARTIALLINKTEXT"):
            actualTextVal = self.driver.find_element_by_partial_link_text(configreader.ConfigReader("locators", locator)).text
            assert expectedTextVal in actualTextVal



    def SWITCH_WINDOW(self,index):
        changedwindow = self.driver.window_handles[index]
        self.driver.switch_to.window(changedwindow)


    def Clear_Text(self,locator):
        time.sleep(2)
        #self.driver = webdriver.Chrome(ChromeDriverManager().install())
        if str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configreader.ConfigReader("locators", locator)).click()
            self.driver.find_element(By.ID, configreader.ConfigReader("locators", locator)).send_keys(Keys.CONTROL,'a')
            self.driver.find_element(By.ID, configreader.ConfigReader("locators", locator)).send_keys(Keys.DELETE)
        elif str(locator).endswith("_NAME"):
            self.driver.find_element(By.NAME, configreader.ConfigReader("locators", locator)).click()
            self.driver.find_element(By.NAME, configreader.ConfigReader("locators", locator)).send_keys(Keys.CONTROL,'a')
            self.driver.find_element(By.NAME, configreader.ConfigReader("locators", locator)).send_keys(Keys.DELETE)
        elif str(locator).endswith("_CLASS"):
            self.driver.find_element(By.CLASS_NAME, configreader.ConfigReader("locators", locator)).click()
            self.driver.find_element(By.CLASS_NAME, configreader.ConfigReader("locators", locator)).send_keys(Keys.CONTROL,'a')
            self.driver.find_element(By.CLASS_NAME, configreader.ConfigReader("locators", locator)).send_keys(Keys.DELETE)
        elif str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configreader.ConfigReader("locators", locator)).click()
            self.driver.find_element(By.XPATH, configreader.ConfigReader("locators", locator)).send_keys(Keys.CONTROL,'a')
            self.driver.find_element(By.XPATH, configreader.ConfigReader("locators", locator)).send_keys(Keys.DELETE)
        elif str(locator).endswith("_CSSSELECTOR"):
            self.driver.find_element(By.CSS_SELECTOR, configreader.ConfigReader("locators", locator)).click()
            self.driver.find_element(By.CSS_SELECTOR, configreader.ConfigReader("locators", locator)).send_keys(Keys.CONTROL,'a')
            self.driver.find_element(By.CSS_SELECTOR, configreader.ConfigReader("locators", locator)).send_keys(Keys.DELETE)






