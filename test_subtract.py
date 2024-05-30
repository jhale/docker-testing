import pytest
from subtract import subtract

@pytest.mark.parametrize("a,b,result", [(1, -1, 2), (3, 4, -1), (0, 0, 0)])
def test_subtract(a, b, result):
    c = subtract(a, b)
    assert c == result

def test_subtract_2():
    c = subtract(-10, 0)
    assert c == -10

def test_subtract_type_error():
    with pytest.raises(TypeError):
        c = subtract(4, "b")
