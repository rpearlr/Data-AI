from employee import Employee
import pytest

@pytest.fixture
def emp() :
    return Employee(1,"Jane",70000)

@pytest.mark.parametrize("a,expected", [
    (30000 ,100000),
    (5000,75000),   
    (-20000, 90000)
])
def test_increase(emp ,a, expected):
    assert emp.increase_salary(a) == expected
    
@pytest.mark.parametrize("a,expected", [
    (30000 ,40000),
    (-5000,65000),   
    (200000, 50000)
])
def test_decrese(emp ,a, expected):
    assert emp.decrease_salary(a) == expected