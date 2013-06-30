# coding=utf-8
from smallinvoice.accounts import Account
from smallinvoice.tests import get_smallinvoice


def generate_account():
    return Account(title='Testaccount',
                   institute='Familie Test',
                   number='Number123',
                   iban='Iban123',
                   swiftbic='Swift123',
                   clearing='clearing123',
                   postaccount='postaccount123',
                   lsv=0,
                   dd=0,
                   esr=1)


def test_list_accounts():
    client = get_smallinvoice()
    a = generate_account()
    account_id = client.accounts.add(a)
    assert len(client.accounts.all()) > 0
    client.accounts.delete(account_id)


def test_add_accounts():
    client = get_smallinvoice()
    a = generate_account()
    account_id = client.accounts.add(a)
    assert account_id
    client.accounts.delete(account_id)


def test_get_accounts_details():
    client = get_smallinvoice()
    a = generate_account()
    account_id = client.accounts.add(a)
    details = client.accounts.details(account_id)
    assert details['institute'] == 'Familie Test'
    client.accounts.delete(account_id)


def test_delete_account():
    client = get_smallinvoice()
    amount = len(client.accounts.all())
    a = generate_account()
    a_id = client.accounts.add(a)
    assert len(client.accounts.all()) == amount + 1
    client.accounts.delete(a_id)
    assert len(client.accounts.all()) == amount


def test_account_update():
    client = get_smallinvoice()
    a = generate_account()
    a_id = client.accounts.add(a)
    a.institute = 'Test Change'
    client.accounts.update(a_id, a)
    details = client.accounts.details(a_id)
    assert details['institute'] == a.institute
    client.accounts.delete(a_id)

