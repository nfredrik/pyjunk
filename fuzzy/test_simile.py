import pytest
from simile import compare_strings

s1 = {'test_adadas', 'test_sdfs', 'dsdsdfsfsdfs'}
s2 = {'test_adadas', 'test_sdfx', 'test_dsdsd', 'test_sdfsdfs'}


def test_compare_strings():
    common, similar, different = compare_strings(s1, s2)

    assert common == {'test_adadas'}

    assert similar == {'test_sdfsdfs', 'test_sdfx','test_dsdsd'}

    assert different == {'test_dsdsd', 'test_sdfsdfs', 'test_sdfx'}
