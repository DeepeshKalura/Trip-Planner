import pytest
from app.gmap import extract_locations


@pytest.mark.parametrize("text, expected_result", [
    ("Bye", {}),
    ("I am planning a trip to New York", {"New York": (40.7127753, -74.0059728)}),
    ("I am going to London and Paris", {"London": (51.5072178, -0.1275862), "Paris": (48.8575475, 2.3513765)})
])
def test_extract_locations(text, expected_result):
    result = extract_locations(text)
    assert result == expected_result

