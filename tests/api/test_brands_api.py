from tests.api.helpers.assertions import assert_method_not_supported


def test_get_all_brands_contract(brands_client):
    res = brands_client.get_all_brands()
    assert res.status == 200

    data = res.json()
    assert data["responseCode"] == 200
    assert isinstance(data.get("brands"), list)
    assert len(data["brands"]) > 0

def test_get_all_brands_schema(brands_client):
    data = brands_client.get_all_brands().json()
    brands = data["brands"]

    for b in brands:
        assert set(b.keys()) == {"id", "brand"}
        assert isinstance(b["id"], int)
        assert b["id"] > 0
        assert isinstance(b["brand"], str)
        assert b["brand"].strip() != ""

def test_get_all_brands_ids_unique(brands_client):
    brands = brands_client.get_all_brands().json()["brands"]
    ids = [b["id"] for b in brands]
    assert len(ids) == len(set(ids)), "Duplicate brand ids found"

def test_get_all_brands_contains_polo(brands_client):
    brands = brands_client.get_all_brands().json()["brands"]
    names = [b["brand"] for b in brands]
    assert "Polo" in names

def test_post_brands_list_not_supported(brands_client):
    res = brands_client.post_brands_list_not_supported()
    assert_method_not_supported(res)

def test_put_brands_list_not_supported(brands_client):
    res = brands_client.put_brands_list_not_supported()
    assert_method_not_supported(res)



