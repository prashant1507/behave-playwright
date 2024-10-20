from tests.pages.base_page import BasePage


class Homepage:

    _products_label = "//span[normalize-space()='Products']"

    def __init__(self, context):
        self.bp = BasePage(context.page)

    def get_text_from_page(self):
        self.bp.get_text(self._products_label)
