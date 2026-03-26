class TestDataError(Exception):
    """Raised when test data cannot be loaded or is invalid."""
    pass


class ApiResponseError(Exception):
    """Raised when an API response has an unexpected status code."""
    pass
