from test import add,sub,multiply,divide,calcc
import pytest
def test_add() :
    result =  add(2,3)
    assert result == 5

def test_sub() :
    result =  sub(2,3)
    assert result == -1

def test_mul() :
    result =  multiply(2,3)
    assert result == 6

def test_div() :
    result =  divide(3,3)
    assert result == 1

def test_calc() :
    assert add(1,2) == 3
    assert sub(9,1) == 8
    assert multiply(3,4) == 12
    
@pytest.fixture
def calc() :
    return calcc()

def test_calcc(calc) :
    assert calc.add(2,6) == 8

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (9, 1, 10),   
    (3, 4, 7)
])
def test_calc_parameter(calc, a, b, expected):
    assert calc.add(a, b) == expected

def test_divide_zero() :
    with pytest.raises(ValueError) :
        divide(10,0)