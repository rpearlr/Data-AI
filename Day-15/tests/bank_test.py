import pytest
from bank import Bank

@pytest.fixture
def bank() :
    return Bank(1000)

def test_deposit(bank) :
    assert bank.deposit(500) == 1500

def test_withdraw(bank) :
    assert bank.withdraw(200) == 800

def test_withdraw_1(bank) :
    assert bank.withdraw(1000) == 0