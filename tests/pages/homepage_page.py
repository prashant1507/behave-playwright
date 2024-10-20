from tests.pages.base_page import BasePage


class Homepage:

    _products_label = "//span[normalize-space()='Products']"

    def __init__(self, page):
        self.bp = BasePage(page)

    def get_text_from_page(self):
        self.bp.get_text(self.products_label)
