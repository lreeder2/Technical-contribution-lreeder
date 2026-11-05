import json
import re

def test_embedded_hover_data():
    with open("county_yield_dashboard.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Extract JSON dataset string from script tag
    match = re.search(r"const rows = (\[.*?\]);", html, re.DOTALL)
    assert match, "Rows dataset not found in HTML"

    data = json.loads(match.group(1))
    assert len(data) > 0, "Dataset is empty"

    # Verify required keys for map hover boxes exist for all records
    required_keys = {"c", "st", "p", "a", "sd"}  # county, state, predicted, actual, std dev
    for row in data:
        missing = required_keys - row.keys()
        assert not missing, f"Missing hover data keys {missing} in record {row}"

    print(f"Data integrity test passed: Validated hover data keys across {len(data)} records successfully.")

if __name__ == "__main__":
    test_embedded_hover_data()