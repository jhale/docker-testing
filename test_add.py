import pytest
from add import add

@pytest.mark.parametrize("a,b,result", [(3, 5, 8), (-3, -4, -7), (0, 0, 0)])
def test_add(a, b, result):
    c = add(a, b)
    assert c == result
