from playwright.sync_api import Page

from utilities.logger import get_logger

logger = get_logger("pages")


class BasePage:
    """Base class for all page objects, providing shared utilities."""

    def __init__(self, page: Page) -> None:
        self.page = page
        logger.info("Initialized %s (url=%s)", type(self).__name__, page.url)

    def normalize_text(self, text: str) -> str:
        """Collapse whitespace and lowercase for comparison."""
        return "".join(text.split()).lower()

    def texts_equal(self, text1: str, text2: str) -> bool:
        """Compare two strings ignoring whitespace and case."""
        return self.normalize_text(text1) == self.normalize_text(text2)

    def scroll_to_bottom(self) -> None:
        """Scroll the page to the very bottom."""
        logger.debug("Scrolling to bottom")
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight);")

    def wait_until_stable(self) -> None:
        """Wait until there are no pending network requests."""
        logger.debug("Waiting for network idle")
        self.page.wait_for_load_state("networkidle")
