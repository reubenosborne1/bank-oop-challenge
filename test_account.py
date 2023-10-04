from account import BankAccount
import pytest

@pytest.fixture
def account1():
    """
    Create an account to be used across the tests.
    """
    return BankAccount(100.00)

@pytest.fixture
def account2():
    """
    Create an account to be used across the tests.
    """
    return BankAccount(500.00)

def test_account_creation(account1, account2):
    """
    Test the accounts were intialised correctly.
    """
    assert account1.balance == 100.00
    assert account1.transaction_history == []
    assert account2.balance == 500.00
    assert account2.transaction_history == []

def test_deposit():
    """
    Test that deposits add to the account balance.
    """
    account1.deposit(50.00)
    assert account1.balance == 150.00

def test_withdraw(account1):
    """
    Test that withdrawls are taken from the account balance.
    """
    account1.withdraw(50.00)
    assert account1.balance == 50.00

def test_withdraw_more_than_balance(account1):
    """
    Test that an error is raised if you withdraw more than the balance.
    """
    try:
        account1.withdraw(150.00)
    except ValueError as e:
        assert str(e) == "Insufficient funds to withdraw £150.00"

def test_transfer(account1, account2):
    """
    Test balances after an amount is transfered from one account to another.
    """
    account1.transfer(100.00, account2)
    assert account1.balance == 0
    assert account2.balance == 600.00

def test_transfer_more_than_balance(account1, account2):
    """
    Test that an error is raised if you transfer more than the balance.
    """
    try:
        account1.transfer(150.00, account2)
    except ValueError as e:
        assert str(e) == "Insufficient funds to transfer £150.00"

def test_transaction_history(account1, account2):
    """
    Test that the transaction history keeps account of the amounts in / out
    and changes to the balance.
    """
    account1.deposit(50.0)
    assert len(account1.transaction_history) == 1 
    assert account1.transaction_history[0]['amount'] == 50.0
    assert account1.transaction_history[0]['balance'] == 150.0

    account1.withdraw(50.0)
    assert len(account1.transaction_history) == 2
    assert account1.transaction_history[1]['amount'] == -50.0
    assert account1.transaction_history[1]['balance'] == 100.0

    account1.transfer(50.0, account2)
    assert len(account1.transaction_history) == 3
    assert account1.transaction_history[2]['amount'] == -50.0
    assert account1.transaction_history[2]['balance'] == 50.0
    assert len(account2.transaction_history) == 1
    assert account2.transaction_history[0]['amount'] == 50.0
    assert account2.transaction_history[0]['balance'] == 550.0    