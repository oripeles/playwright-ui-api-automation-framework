from playwright.sync_api import APIRequestContext, APIResponse

from utilities.exceptions import ApiResponseError
from utilities.logger import get_logger

logger = get_logger("api")


class BaseApiClient:
    """Base class for all API clients, providing HTTP methods with logging."""

    def __init__(self, request: APIRequestContext):
        self.request = request

    def _check_server_error(self, method: str, path: str, response: APIResponse) -> None:
        """Raise ApiResponseError on 5xx server errors."""
        if response.status >= 500:
            raise ApiResponseError(f"{method} {path} returned server error: {response.status}")

    def get(self, path: str, **kwargs) -> APIResponse:
        """Send a GET request and log the result."""
        response = self.request.get(path, **kwargs)
        logger.info("GET %s -> %d", path, response.status)
        self._check_server_error("GET", path, response)
        return response

    def post(self, path: str, **kwargs) -> APIResponse:
        """Send a POST request and log the result."""
        response = self.request.post(path, **kwargs)
        logger.info("POST %s -> %d", path, response.status)
        self._check_server_error("POST", path, response)
        return response

    def put(self, path: str, **kwargs) -> APIResponse:
        """Send a PUT request and log the result."""
        response = self.request.put(path, **kwargs)
        logger.info("PUT %s -> %d", path, response.status)
        self._check_server_error("PUT", path, response)
        return response

    def delete(self, path: str, **kwargs) -> APIResponse:
        """Send a DELETE request and log the result."""
        response = self.request.delete(path, **kwargs)
        logger.info("DELETE %s -> %d", path, response.status)
        self._check_server_error("DELETE", path, response)
        return response
