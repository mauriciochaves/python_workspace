import time
from hamcrest import assert_that, equal_to
from pages.HomePage import *
from pages.Authentication import *


@step(u'I am on Home Page')
def step_impl(context):
    context.page_object = HomeActions(context.driver)
    context.page_object.open_application(context.base_url)

@step(u'I fill in the email field with the "{email}" who is not registered')
def step_impl(context, email):
    context.page_object = AuthenticationActions(context.driver)
    context.page_object.email_in(email)
    context.page_object.click_on_sign_in()

@step(u'I click on sign in')
def step_impl(context):
    context.page_object.click_on_sign_in()

@step(u'system should display the message "{mensage}"')
def step_impl(context, mensage):
    assert_that(context.page_object.get_alert(), equal_to(mensage))

@step(u'I fill my email "{email}" on create an account field')
def step_impl(context, email):
    context.page_object = AuthenticationActions(context.driver)
    context.page_object.email_in_create_account(email)

@step(u'I click on create an account')
def step_impl(context):
    context.page_object.click_on_create_account()

@step(u'I click on register')
def step_impl(context):
    context.page_object.click_on_register()

@step(u'I should go to "{screen}" screen')
def step_impl(context,screen):
    assert_that(context.page_object.get_personal_info(), equal_to(screen))

@step(u'I click on Mr title')
def step_impl(context):
    context.page_object.click_on_mr_title()

@step(u'I type "{first_name}" on first name')
def step_impl(context, first_name):
    context.page_object.type_in_first_name(first_name)

@step(u'I type "{last_name}" on last name')
def step_impl(context, last_name):
    context.page_object.type_in_last_name(last_name)

@step(u'I type "{password}" on password')
def step_impl(context, password):
    context.page_object.type_in_password(password)

@step(u'I type "{address_fn}" on my address first name')
def step_impl(context, address_fn):
    context.page_object.type_in_address_first_name(address_fn)

@step(u'I type "{address_ln}" on my address last name')
def step_impl(context, address_ln):
    context.page_object.type_in_address_last_name(address_ln)

@step(u'I type "{address}" on address')
def step_impl(context, address):
    context.page_object.type_in_address(address)

@step(u'I type "{city}" on city')
def step_impl(context, city):
    context.page_object.type_in_city(city)
    time.sleep(10)
    
@step(u'I select "{state}" on state') 
def step_impl(context,state):
    context.page_object.select_in_combo_box(state)
    time.sleep(10)