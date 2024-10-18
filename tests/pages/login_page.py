from helpers.constants.framework_constants import FrameworkConstants as Fc
from tests.pages.base_page import BasePage
from utils.helper_utils import read_file

details = read_file(Fc.details_file)


class LoginPage:
    username_text_box = "#user-name"
    password_text_box = "#password"
    login_button = "#login-button"

    def __init__(self, page):
        self.url = details["url"]
        self.bp = BasePage(page)

    def navigate_to_page(self):
        self.bp.open_page(self.url)

    def enter_username(self, username):
        self.bp.send_keys(self.username_text_box, username)

    def enter_password(self, password):
        self.bp.send_keys(self.password_text_box, password)

    def click_login_button(self):
        self.bp.click(self.login_button)

    def get_page_tile(self):
        return self.bp.get_title()
