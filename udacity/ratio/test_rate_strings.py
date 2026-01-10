from rate_strings import rate_similarity
import pytest

@pytest.mark.parametrize("s1,s2,ratio,expected", [
    ("", "", 0.9, True),         # Identical empty strings (ratio = 1.0)
    ("a", "a", 0.9, True),       # Identical single character (ratio = 1.0)
    ("a", "b", 0.9, False),      # Completely different single characters (ratio = 0.0)
    ("abc", "abc", 0.9, True),   # Identical strings (ratio = 1.0)
    ("abc", "abd", 0.6, True),   # Similar strings (ratio ≈ 0.666...)
    ("abc", "abcde", 0.6, True), # One string is prefix of another (ratio = 0.6)
    ("abc", "xyz", 0.1, False),  # Completely different strings (ratio = 0.0)
])
def test_rate_similarity(s1, s2, ratio, expected):
    assert rate_similarity(s1, s2, ratio) == expected