from tests.pages.base_page import BasePage

class LoginPage:
    _username_text_box = "#user-name"
    _password_text_box = "#password"
    _login_button = "#login-button"

    def __init__(self, context):
        self.url = context.details.get("general", "url")
        self.bp = BasePage(context.page)

    def navigate_to_page(self):
        self.bp.open_page(self.url)

    def enter_username(self, username):
        self.bp.send_keys(self._username_text_box, username)

    def enter_password(self, password):
        self.bp.send_keys(self._password_text_box, password)

    def click_login_button(self):
        self.bp.click(self._login_button)

    def get_page_tile(self):
        return self.bp.get_title()
