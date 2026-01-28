import json

def load_json(filename):
    with open(f"data/{filename}.json", "r", encoding="utf-8") as f:
        return json.load(f)
