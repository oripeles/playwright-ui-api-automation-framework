from tests.api.helpers.assertions import assert_method_not_supported
from tests.api.helpers.assertions import assert_missing_required_parameter

def test_get_all_products_contract(products_client):
    res = products_client.get_all_products()
    assert res.status == 200

    data = res.json()
    assert data["responseCode"] == 200
    assert "products" in data
    assert isinstance(data["products"], list)
    assert len(data["products"]) > 0

def test_get_all_products_schema(products_client):
    products = products_client.get_all_products().json()["products"]

    for p in products:
        assert "id" in p
        assert "name" in p
        assert "price" in p
        assert "brand" in p

        assert isinstance(p["id"], int)
        assert p["id"] > 0
        assert isinstance(p["name"], str)
        assert p["name"].strip() != ""

def test_get_all_products_contains_blue_top(products_client):
    products = products_client.get_all_products().json()["products"]

    blue_top = next((p for p in products if p.get("name") == "Blue Top"), None)
    assert blue_top is not None
    assert blue_top["brand"] == "Polo"


def test_post_products_list_not_supported(products_client):
    res = products_client.post_products_list()
    assert_method_not_supported(res)

def test_search_product_success(products_client):
    response = products_client.search_product("top")
    assert response.status == 200

    data = response.json()
    assert data["responseCode"] == 200
    assert "products" in data
    assert len(data["products"]) > 0

def test_search_product_results_match_term(products_client):
    term = "top"
    data = products_client.search_product(term).json()
    products = data["products"]
    for p in products[:3]:
        assert term in p["name"].lower()

def test_search_product_no_results(products_client):
    data = products_client.search_product("zzzz_not_exist_123").json()
    assert data["responseCode"] in (200, 404, 400)
    if "products" in data:
        assert isinstance(data["products"], list)

def test_search_product_missing_required_parameter(products_client):
    res = products_client.search_product_without_param()
    assert_missing_required_parameter(res)
