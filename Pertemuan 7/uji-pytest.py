import pytest

def tambah(a, b):
    return a + b

@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0)])
def test_tambah(a, b, expected):
    assert tambah(a, b) == expected
