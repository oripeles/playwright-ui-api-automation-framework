from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def normalize_text(self, text: str) -> str:
        return "".join(text.split()).lower()

    def texts_equal(self, text1: str, text2: str) -> bool:
        return self.normalize_text(text1) == self.normalize_text(text2)

    def scroll_to_bottom(self) -> None:
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight);")

    def wait_until_stable(self) -> None:
        self.page.wait_for_load_state("networkidle")
