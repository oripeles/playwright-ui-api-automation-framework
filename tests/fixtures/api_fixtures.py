import pytest
from api.clients.auth_client import AuthClient
from api.clients.brands_client import BrandsClient
from api.clients.products_client import ProductsClient
from utilities.logger import get_logger

logger = get_logger("fixtures")


@pytest.fixture(scope="session")
def api_request_context(playwright, base_url):
    """Create an API request context for the entire test session."""
    logger.info("Creating API request context (base_url=%s)", base_url)
    request_context = playwright.request.new_context(base_url=base_url)
    yield request_context
    logger.info("Disposing API request context")
    request_context.dispose()


@pytest.fixture
def products_client(api_request_context):
    """Return a ProductsClient instance."""
    return ProductsClient(api_request_context)

@pytest.fixture
def brands_client(api_request_context):
    """Return a BrandsClient instance."""
    return BrandsClient(api_request_context)

@pytest.fixture
def auth_client(api_request_context):
    """Return an AuthClient instance."""
    return AuthClient(api_request_context)
