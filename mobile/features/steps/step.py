from hamcrest import assert_that, equal_to
from pages.Actions import *

@given(u'I am on Home Page')
def step_impl(context):
    context.page_object = DeviceHomeActions(context.driver)
    context.page_object.open_application()

@when(u'I click login without informing a user or password')
def step_when(context):
    context.home_page_object = HomeActions(context.driver)
    context.home_page_object.click_on_login()

@then(u'system should display the message regarding the user "{mensage}"')
def step_then(context, mensage):
    context.page_object = HomeActions(context.driver)
    assert_that(context.page_object.get_error_user(), equal_to(mensage))

@then(u'system should display the message regarding the password "{mensage}"')
def step_and(context, mensage):
    context.page_object = HomeActions(context.driver)
    assert_that(context.page_object.get_error_password(), equal_to(mensage))

@given(u'I clicked on the option I forgot my password')
def step_impl2(context):
    context.page_object = HomeActions(context.driver)
    context.page_object.click_on_forgot_password()

@when(u'I click send without informing a user')
def step_when2(context):
    context.page_object = ForgotPasswordActions(context.driver)
    context.page_object.click_on_send_button()

@then(u'system should display the message "{mensage}"')
def step_then2(context, mensage):
    context.page_object = ForgotPasswordActions(context.driver)
    assert_that(context.page_object.get_error_user(), equal_to(mensage))

@then(u'the title of the page should be "{mensage}"')
def step_when3(context, mensage):
    context.page_object = ForgotPasswordActions(context.driver)
    assert_that(context.page_object.get_title(), equal_to(mensage))

@then(u'Help information "{mensage}" should be displayed')
def step_when4(context, mensage):
    context.page_object = ForgotPasswordActions(context.driver)
    assert_that(context.page_object.get_help_mensage(), equal_to(mensage))
