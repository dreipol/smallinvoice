# coding=utf-8
import unittest
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


class AccountTests(unittest.TestCase):
    def setUp(self):
        self.a = generate_account()
        self.account_id = get_smallinvoice().accounts.add(self.a)

    def tearDown(self):
        get_smallinvoice().accounts.delete(self.account_id)

    def test_account_tests(self):
        self.assertIsNotNone(self.account_id)

    def test_account_add(self):
        self.assertTrue(self.account_id)

    def test_account_details(self):
        self.assertEqual(self.a.institute, 'Familie Test')

    def test_account_update(self):
        self.assertEqual(self.a.institute, 'Familie Test')
        self.a.institute = 'Test Change'
        self.assertEqual(self.a.institute, 'Test Change')
