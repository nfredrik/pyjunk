import pytest

from is_functions.is_listening import is_listening


def test_is_listening():
    assert is_listening(host='example.com', port=80)

def test_is_listening_2():
    assert is_listening(host='172.66.147.243', port=80)



def test_is_not_listening():
    assert not is_listening(host='example.com', port=81)

def test_is_not_listening_2():
    with pytest.raises(Exception):
        assert not is_listening(host='example.co', port=81)

def test_is_listening_3():
    assert not is_listening(host='127.0.0.2', port=80)
