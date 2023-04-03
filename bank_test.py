from apple import Bank, SavingsAccount, CurrentAccount


def test_open_account():
    bank = Bank()
    account_test = SavingsAccount("123", 1000, 1.5)
    bank.open_account(account_test)
    assert len(bank.accounts) == 1
    assert bank.accounts[0] == account_test
    assert account_test.balance == 1000


test_open_account()


def test_bank_upd():
    bank = Bank()
    account_test_2 = SavingsAccount("222", 1000, 1.5)
    account_test_3 = CurrentAccount("333", -500, 2000)
    bank.open_account(account_test_2)
    bank.open_account(account_test_3)
    bank.upd()
    assert account_test_2.balance == 1000 + 1000 * 1.5 / 100, 'account_test_2 balance should be 1015.0'
    assert account_test_3.balance == -500.0 and account_test_3.balance > -2000, 'account_test_3 balance should be -500'


test_bank_upd()
