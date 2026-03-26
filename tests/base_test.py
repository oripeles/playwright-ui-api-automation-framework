from utilities.logger import get_logger

logger = get_logger("tests")


class BaseTest:
    """Base class for all test classes, providing shared test logging."""

    def setup_method(self, method):
        """Log the test name before each test runs."""
        logger.info("STARTING: %s.%s", type(self).__name__, method.__name__)

    def teardown_method(self, method):
        """Log the test name after each test completes."""
        logger.info("FINISHED: %s.%s", type(self).__name__, method.__name__)
