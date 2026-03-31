import pytest
from jsonschema import validate
from tests.api.helpers.assertions import assert_method_not_supported
from tests.api.schemas.brand_schema import BRANDS_RESPONSE_SCHEMA, BRAND_SCHEMA

pytestmark = pytest.mark.regression


def test_get_all_brands_contract(brands_client):
    res = brands_client.get_all_brands()
    assert res.status == 200, f"Expected HTTP 200, got {res.status}"

    data = res.json()
    validate(instance=data, schema=BRANDS_RESPONSE_SCHEMA)

def test_get_all_brands_schema(brands_client):
    brands = brands_client.get_all_brands().json()["brands"]

    for b in brands:
        validate(instance=b, schema=BRAND_SCHEMA)

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
