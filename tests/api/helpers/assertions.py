def assert_method_not_supported(res):
    """Assert that the API returns a 405 'method not supported' response."""
    assert res.status == 200, f"Expected HTTP 200, got {res.status}"
    data = res.json()
    assert data["responseCode"] == 405, f"Expected responseCode 405, got {data['responseCode']}"
    assert "not supported" in data["message"].lower(), f"Expected 'not supported' in message, got: {data['message']}"

def assert_missing_required_parameter(res):
    """Assert that the API returns a 400 'missing parameter' response."""
    assert res.status == 200, f"Expected HTTP 200, got {res.status}"
    data = res.json()
    assert data["responseCode"] == 400, f"Expected responseCode 400, got {data['responseCode']}"
    assert "missing" in data["message"].lower(), f"Expected 'missing' in message, got: {data['message']}"
