from behave import given, when, then
from playwright.sync_api import expect

from helpers.constants.framework_constants import FrameworkConstants
from utils.helper_utils import read_file
from tests.pages.homepage_page import Homepage
from tests.pages.login_page import LoginPage

details = read_file(FrameworkConstants.details_file)


@given("User navigates to login page")
def navigate_to_page(context):
    context.login_page = LoginPage(context.page)
    context.home_page = Homepage(context.page)
    context.login_page.navigate_to_page()


@when("User enters username as '{username}'")
def enter_username(context, username):
    context.login_page.enter_username(details["logins"][username]["username"])


@when("User enters password for '{username}'")
def enter_password(context, username):
    context.login_page.enter_password(details["logins"][username]["password"])


@when("User clicks on 'Login' button")
def click_login_button(context):
    context.login_page.click_login_button()


@then("Homepage is displayed")
def verify_homepage(context):
    assert context.login_page.get_page_tile() == "Swag Labs"


@then("Labels are present")
def verify_labels(context):
    for r in context.table:
        assert context.login_page.get_text_from_page() == r["label_name"]


@then("Product is displayed")
def verify_homepage(context):
    expect(context.login_page.get_page_tile()).is_equal_to("Products")
