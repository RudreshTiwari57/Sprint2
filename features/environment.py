import time
import pandas as pd
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Utilities import configreader


# This will contain HOOKS - HOOKS in BEHAVE are like PYTEST DECORATERS/ANNOTATION - @pytest


# Hooks to run before scenario and after scenario.
# Hooks to run before step and after step.
# Hooks to run before all and after all

# After step hook
def after_step(context, step):
    print()
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)


# Before step hook
def before_step(context, step):
    pass


# Before Scenario Hook
def before_scenario(context,driver):
    if configreader.ConfigReader("base info", "browser") == "chrome":
        context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        context.driver.maximize_window()
        context.driver.set_page_load_timeout(500)
    if configreader.ConfigReader("base info", "browser") == "firefox":
        context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        context.driver.maximize_window()
        context.driver.set_page_load_timeout(500)


# After Scenario Hook
def after_scenario(context, driver):
    time.sleep(3)
    context.driver.quit()



