
class BasePage:
    def __init__(self, page):
        self.page = page

    def open_page(self, url):
        self.page.goto(url)

    def send_keys(self, locator, text):
        self.page.locator(locator).fill(text)

    def click(self, locator):
        self.page.locator(locator).click()

    def get_title(self):
        return self.page.title().strip()

    def get_text(self, locator):
        return self.page.locator(locator).text_content().strip()
