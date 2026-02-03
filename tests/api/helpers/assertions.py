def assert_method_not_supported(res):
    assert res.status == 200
    data = res.json()
    assert data["responseCode"] == 405
    assert "not supported" in data["message"].lower()

def assert_missing_required_parameter(res):
    assert res.status == 200
    data = res.json()
    assert data["responseCode"] == 400
    assert "missing" in data["message"].lower()
