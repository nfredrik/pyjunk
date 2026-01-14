


s1 = {'test_adadas', 'test_sdfs', 'dsdsdfsfsdfs'}
s2 = {'test_adadas', 'test_sdfx', 'test_dsdsd', 'test_sdfsdfs'}

import pytest
from comparing import compare_strings

# Test data
s1 = {'test_adadas', 'test_sdfs', 'dsdsdfsfsdfs'}
s2 = {'test_adadas', 'test_sdfx', 'test_dsdsd', 'test_sdfsdfs'}


def test_compare_strings_exact_matches():
    exact_matches, similar_matches, others = compare_strings(s1, s2)
    assert exact_matches == ['test_adadas']  # Only exact match
    assert len(similar_matches) > 0  # Should find some similar matches
    assert len(others) > 0  # Should have some non-matching strings


def test_compare_strings_similarity():
    exact_matches, similar_matches, others = compare_strings(s1, s2)

    # Check that similar matches have score >= threshold
    for a, b, score in similar_matches:
        assert score >= 0.6  # Default threshold
        assert a in s1
        assert b in s2
        assert a not in exact_matches
        assert b not in exact_matches


def test_compare_strings_no_duplicates():
    exact_matches, similar_matches, others = compare_strings(s1, s2)

    # Check no string is used in multiple matches
    matched_s1 = {a for a, _, _ in similar_matches}
    matched_s2 = {b for _, b, _ in similar_matches}

    assert len(matched_s1) == len(similar_matches)  # No duplicates in s1
    assert len(matched_s2) == len(similar_matches)  # No duplicates in s2
    assert set(exact_matches).isdisjoint(matched_s1 | matched_s2)  # Exact matches not in similar


def test_compare_strings_with_custom_threshold():
    # With higher threshold, we should get fewer similar matches
    _, similar_high_threshold, others_high = compare_strings(s1, s2, threshold=0.8)
    _, similar_low_threshold, others_low = compare_strings(s1, s2, threshold=0.3)

    assert len(similar_high_threshold) <= len(similar_low_threshold)
    assert len(others_high) >= len(others_low)


def test_compare_strings_empty_input():
    # Test with empty sets
    exact, similar, others = compare_strings(set(), set())
    assert exact == []
    assert similar == []
    assert others == []

    # Test with one empty set
    exact, similar, others = compare_strings(s1, set())
    assert exact == []
    assert similar == []
    assert set(others) == s1