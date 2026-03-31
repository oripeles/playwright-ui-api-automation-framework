BRAND_SCHEMA = {
    "type": "object",
    "required": ["id", "brand"],
    "properties": {
        "id": {"type": "integer", "minimum": 1},
        "brand": {"type": "string", "minLength": 1},
    },
    "additionalProperties": False,
}

BRANDS_RESPONSE_SCHEMA = {
    "type": "object",
    "required": ["responseCode", "brands"],
    "properties": {
        "responseCode": {"type": "integer", "enum": [200]},
        "brands": {
            "type": "array",
            "minItems": 1,
            "items": BRAND_SCHEMA,
        },
    },
}
