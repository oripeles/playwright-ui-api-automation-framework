class BasePage:
    def __init__(self, page):
        self.page = page

    def normalize_text(self, text):
        return "".join(text.split()).lower()

    def texts_equal(self, text1, text2):
        return self.normalize_text(text1) == self.normalize_text(text2)

    def scroll_to_bottom(self):
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight);")

    def wait_until_stable(self):
        self.page.wait_for_load_state("networkidle")
