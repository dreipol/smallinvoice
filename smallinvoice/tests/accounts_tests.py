from smallinvoice.accounts import Account
from smallinvoice.client import Client
from smallinvoice.tests import TEST_API_TOKEN




def generate_account():
    return Account(title='Testaccount', institute='Familie Test',
                number='Number123', iban='Iban123',
                swiftbic='Swift123', clearing='clearing123', postaccount='postaccount123', lsv=1, dd=1, esr=0)

def test_list_accounts():
    client = Client(TEST_API_TOKEN)
    a = generate_account()
    account_id = client.accounts.add(a)
    assert len(client.accounts.all()) > 0
    client.accounts.delete(account_id)


def test_add_accounts():
    client = Client(TEST_API_TOKEN)
    a = generate_account()
    account_id = client.accounts.add(a)
    assert account_id
    client.accounts.delete(account_id)



def test_get_accounts_details():
    client = Client(TEST_API_TOKEN)
    a = generate_account()
    account_id = client.accounts.add(a)
    details = client.accounts.details(account_id)
    assert details['institute'] == 'Familie Test'
    client.accounts.delete(account_id)


def test_delete_account():
    client = Client(TEST_API_TOKEN)
    amount = len(client.accounts.all())
    a = generate_account()
    a_id = client.accounts.add(a)
    assert len(client.accounts.all()) == amount +1
    client.accounts.delete(a_id)
    assert len(client.accounts.all()) == amount


def test_account_update():
    client = Client(TEST_API_TOKEN)
    a = generate_account()
    a_id =client.accounts.add(a)
    a.institute = 'Test Change'
    client.accounts.update(a_id, a)
    details = client.accounts.details(a_id)
    assert details['institute'] == a.institute
    client.accounts.delete(a_id)


