from hamcrest import assert_that, equal_to
from pages.Actions import *

@given(u'I am on Home Page')
def step_impl(context):
    context.page_object = HomeActions(context.driver)
    context.page_object.open_application()

@when(u'I fill in the email field with the "{email}" who is not registered')
def step_when(context, email):
    context.home_page_object = HomeActions(context.driver)
    context.auth_page_object = AuthenticationActions(context.driver)

    context.home_page_object.click_on_sign_in()
    context.auth_page_object.email_in(email)
    context.auth_page_object.click_on_sign_in()

@then(u'system should display the message "{mensage}"')
def step_then(context, mensage):
    context.page_object = AuthenticationActions(context.driver)
    assert_that(context.page_object.get_alert(), equal_to(mensage))
