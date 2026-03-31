PRODUCT_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "price", "brand", "category"],
    "properties": {
        "id": {"type": "integer", "minimum": 1},
        "name": {"type": "string", "minLength": 1},
        "price": {"type": "string"},
        "brand": {"type": "string", "minLength": 1},
        "category": {
            "type": "object",
            "required": ["category"],
            "properties": {
                "category": {"type": "string"},
            },
        },
    },
}

PRODUCTS_RESPONSE_SCHEMA = {
    "type": "object",
    "required": ["responseCode", "products"],
    "properties": {
        "responseCode": {"type": "integer", "enum": [200]},
        "products": {
            "type": "array",
            "minItems": 1,
            "items": PRODUCT_SCHEMA,
        },
    },
}
