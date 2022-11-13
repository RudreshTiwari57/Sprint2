from behave import *
import logging
from Utilities.LogUtil import Logger
from features.pageobject.ElecProduct import ELEC_Product
from features.pageobject.Login import LOGIN
from features.pageobject.search import SEARCH


log = Logger(__name__,logging.INFO)

@given(u'we navigate to Flipkart url')
def step_impl(context):
    context.login = LOGIN(context.driver)
    context.login.OpenURl()
    log.logger.info("opening filpkart home page")



@then(u'we type in the "{number}" edit box')
def step_impl(context,number):
    context.login.Enter_Username(number)
    log.logger.info("Entering number")


@then(u'we type in the "{password}" field')
def step_impl(context,password):
    context.login.Enter_password(password)
    log.logger.info("Entering password")


@then(u'we click on the login button')
def step_impl(context):
    context.login.Click_login()
    log.logger.info("Click login")


@then(u'type "{searchTEXT}" in searchbox')
def step_impl(context,searchTEXT):
    global lk
    lk = searchTEXT
    context.SEARCH = SEARCH(context.driver)
    context.SEARCH.text_Searchbar(searchTEXT)
    log.logger.info("Enter text on search bar")



@then(u'click on search button')
def step_impl(context):
    context.SEARCH.Click_SEARCHBUTTON()
    log.logger.info("Click search button")



@then(u'click on product name')
def step_impl(context):
    context.ELEC_Product = ELEC_Product(context.driver)
    context.ELEC_Product.Click_product()
    log.logger.info("Click on product")



@then(u'switch to new window')
def step_impl(context):

    context.ELEC_Product.SWITCHWINDOW()
    log.logger.info("switching window")


@then(u'check diffrent images of the product')
def step_impl(context):
    context.ELEC_Product.CLICK_IMAGES()
    log.logger.info("verifing images")



@then(u'Give "{pincode}"')
def step_impl(context,pincode):
    context.ELEC_Product.Enter_PinCode(pincode)
    log.logger.info("Entering pincode")


@then(u'click on check')
def step_impl(context):
    context.ELEC_Product.Click_oncheck(lk)
    log.logger.info("Click on check")

@then(u'click on wishlist')
def step_impl(context):
    context.ELEC_Product.CLick_WISHLIST()
    log.logger.info("Click on wishlist icon")


@then(u'click on read more in specifactions')
def step_impl(context):
    context.ELEC_Product.specifactions()
    log.logger.info("click read more in specification")




