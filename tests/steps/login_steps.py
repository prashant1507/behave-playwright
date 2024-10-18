from behave import given, when, then
from helpers.constants.framework_constants import FrameworkConstants
from utils.helper_utils import read_file
from tests.pages.homepage_page import Homepage
from tests.pages.login_page import LoginPage

details = read_file(FrameworkConstants.details_file)


@given("User navigates to login page")
def navigate_to_page(context):
    LoginPage(context.page).navigate_to_page()


@when("User enters username as '{username}'")
def enter_username(context, username):
    LoginPage(context.page).enter_username(details["logins"][username]["username"])


@when("User enters password for '{username}'")
def enter_password(context, username):
    LoginPage(context.page).enter_password(details["logins"][username]["password"])


@when("User clicks on 'Login' button")
def click_login_button(context):
    LoginPage(context.page).click_login_button()


@then("Homepage is displayed")
def verify_homepage(context):
    assert LoginPage(context.page).get_page_tile() == "Swag Labs"


@then("Labels are present")
def verify_labels(context):
    for r in context.table:
        assert Homepage(context.page).get_text_from_page() == r["label_name"]


@then("Product is displayed")
def verify_homepage(context):
    assert LoginPage(context.page).get_page_tile() == "Products"
