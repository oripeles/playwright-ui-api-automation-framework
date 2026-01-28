from pages.base_page import BasePage

class CasesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.cases_title = page.get_by_text("Test Cases")

