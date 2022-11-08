from behave import *
from features.pageobject.ElecProduct import ELEC_Product
from features.pageobject.Login import LOGIN
from features.pageobject.search import SEARCH


@given(u'we navigate to Flipkart url')
def step_impl(context):
    context.login = LOGIN(context.driver)
    context.login.OpenURl()


@then(u'we type in the "{number}" edit box')
def step_impl(context,number):
    context.login.Enter_Username(number)


@then(u'we type in the "{password}" field')
def step_impl(context,password):
    context.login.Enter_password(password)


@then(u'we click on the login button')
def step_impl(context):
    context.login.Click_login()


@then(u'type "{searchTEXT}" in searchbox')
def step_impl(context,searchTEXT):
    global lk
    lk = searchTEXT
    context.SEARCH = SEARCH(context.driver)
    context.SEARCH.text_Searchbar(searchTEXT)


@then(u'click on search button')
def step_impl(context):
    context.SEARCH.Click_SEARCHBUTTON()


@then(u'click on product name')
def step_impl(context):
    context.ELEC_Product = ELEC_Product(context.driver)
    context.ELEC_Product.Click_product()



@then(u'switch to new window')
def step_impl(context):

    context.ELEC_Product.SWITCHWINDOW()


@then(u'check diffrent images of the product')
def step_impl(context):
    context.ELEC_Product.CLICK_IMAGES()



@then(u'Give "{pincode}"')
def step_impl(context,pincode):
    context.ELEC_Product.Enter_PinCode(pincode)


@then(u'click on check')
def step_impl(context):
    context.ELEC_Product.Click_oncheck(lk)

@then(u'click on wishlist')
def step_impl(context):
    context.ELEC_Product.CLick_WISHLIST()


@then(u'click on read more in specifactions')
def step_impl(context):
    context.ELEC_Product.specifactions()




