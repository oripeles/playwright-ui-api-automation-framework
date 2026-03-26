import pytest
from tests.api.helpers.assertions import assert_method_not_supported

pytestmark = pytest.mark.regression


def test_get_all_brands_contract(brands_client):
    res = brands_client.get_all_brands()
    assert res.status == 200, f"Expected HTTP 200, got {res.status}"

    data = res.json()
    assert data["responseCode"] == 200, f"Expected responseCode 200, got {data['responseCode']}"
    assert isinstance(data.get("brands"), list), "Response missing 'brands' list"
    assert len(data["brands"]) > 0, "Brands list is empty"

def test_get_all_brands_schema(brands_client):
    data = brands_client.get_all_brands().json()
    brands = data["brands"]

    for b in brands:
        assert set(b.keys()) == {"id", "brand"}, f"Unexpected keys: {b.keys()}"
        assert isinstance(b["id"], int), f"Expected int id, got {type(b['id'])}"
        assert b["id"] > 0, f"Expected positive id, got {b['id']}"
        assert isinstance(b["brand"], str), f"Expected str brand, got {type(b['brand'])}"
        assert b["brand"].strip() != "", f"Brand name is empty for id={b['id']}"

def test_get_all_brands_ids_unique(brands_client):
    brands = brands_client.get_all_brands().json()["brands"]
    ids = [b["id"] for b in brands]
    assert len(ids) == len(set(ids)), "Duplicate brand ids found"

def test_get_all_brands_contains_polo(brands_client):
    brands = brands_client.get_all_brands().json()["brands"]
    names = [b["brand"] for b in brands]
    assert "Polo" in names, f"Brand 'Polo' not found. Available: {names}"

def test_post_brands_list_not_supported(brands_client):
    res = brands_client.post_brands_list_not_supported()
    assert_method_not_supported(res)

def test_put_brands_list_not_supported(brands_client):
    res = brands_client.put_brands_list_not_supported()
    assert_method_not_supported(res)
