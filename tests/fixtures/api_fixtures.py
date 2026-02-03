import pytest
from api.clients.auth_client import AuthClient
from api.clients.brands_client import BrandsClient
from api.clients.products_client import ProductsClient


@pytest.fixture(scope="session")
def api_request_context(playwright, base_url):
    request_context = playwright.request.new_context(base_url=base_url)
    yield request_context
    request_context.dispose()


@pytest.fixture
def products_client(api_request_context):
    return ProductsClient(api_request_context)

@pytest.fixture
def brands_client(api_request_context):
    return BrandsClient(api_request_context)

@pytest.fixture
def auth_client(api_request_context):
    return AuthClient(api_request_context)
