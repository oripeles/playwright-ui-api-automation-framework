import pytest
from jsonschema import validate
from tests.api.helpers.assertions import assert_method_not_supported
from tests.api.helpers.assertions import assert_missing_required_parameter
from tests.api.schemas.product_schema import PRODUCTS_RESPONSE_SCHEMA, PRODUCT_SCHEMA

pytestmark = pytest.mark.regression

@pytest.mark.smoke
def test_get_all_products_contract(products_client):
    res = products_client.get_all_products()
    assert res.status == 200, f"Expected HTTP 200, got {res.status}"

    data = res.json()
    validate(instance=data, schema=PRODUCTS_RESPONSE_SCHEMA)

def test_get_all_products_schema(products_client):
    products = products_client.get_all_products().json()["products"]

    for p in products:
        validate(instance=p, schema=PRODUCT_SCHEMA)

def test_get_all_products_contains_blue_top(products_client):
    products = products_client.get_all_products().json()["products"]

    blue_top = next((p for p in products if p.get("name") == "Blue Top"), None)
    assert blue_top is not None, "Product 'Blue Top' not found in products list"
    assert blue_top["brand"] == "Polo", f"Expected brand 'Polo', got '{blue_top['brand']}'"


def test_post_products_list_not_supported(products_client):
    res = products_client.post_products_list()
    assert_method_not_supported(res)

def test_search_product_success(products_client):
    response = products_client.search_product("top")
    assert response.status == 200, f"Expected HTTP 200, got {response.status}"

    data = response.json()
    assert data["responseCode"] == 200, f"Expected responseCode 200, got {data['responseCode']}"
    assert "products" in data, "Response missing 'products' key"
    assert len(data["products"]) > 0, "Search returned no products"

def test_search_product_results_match_term(products_client):
    term = "top"
    data = products_client.search_product(term).json()
    products = data["products"]
    for p in products[:3]:
        assert term in p["name"].lower(), f"Product '{p['name']}' does not contain '{term}'"

def test_search_product_no_results(products_client):
    data = products_client.search_product("zzzz_not_exist_123").json()
    assert data["responseCode"] in (200, 404, 400), f"Unexpected responseCode: {data['responseCode']}"
    if "products" in data:
        assert isinstance(data["products"], list), f"Expected list, got {type(data['products'])}"

def test_search_product_missing_required_parameter(products_client):
    res = products_client.search_product_without_param()
    assert_missing_required_parameter(res)
