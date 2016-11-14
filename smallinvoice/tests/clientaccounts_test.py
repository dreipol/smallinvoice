# coding=utf-8
import unittest
from smallinvoice.accounts import Account
from smallinvoice.tests import get_smallinvoice, generate_address
from .clients_test import generate_customer


class ClientAccountTests(unittest.TestCase):
    def setUp(self):
        self.address = generate_address()
        self.client = generate_customer()
        self.client.add_address(self.address)
        self.client_id = get_smallinvoice().clients.add(self.client)
    
    def tearDown(self):
        get_smallinvoice().clients.delete(self.client_id)
    
    def test_list_client_accounts(self):
        data = get_smallinvoice().clientaccounts.all(self.client_id)
        self.assertEquals(0, data['count'])
        
        from smallinvoice.clientaccounts import ClientAccount
        ca = ClientAccount(number=121312313, swift='ABBCCHZZ', clearing='ATBLZ12345', name='tests')
        get_smallinvoice().clientaccounts.add(self.client_id, ca)
        
        data = get_smallinvoice().clientaccounts.all(self.client_id)
        self.assertEquals(1, data['count'])
    
    def test_delete_client_accounts(self):
        data = get_smallinvoice().clientaccounts.all(self.client_id)
        self.assertEquals(0, data['count'])
        
        from smallinvoice.clientaccounts import ClientAccount
        ca = ClientAccount(number=121312313, swift='ABBCCHZZ', clearing='ATBLZ12345', name='tests')
        client_account_id = get_smallinvoice().clientaccounts.add(self.client_id, ca)
        
        data = get_smallinvoice().clientaccounts.all(self.client_id)
        self.assertEquals(1, data['count'])
        
        get_smallinvoice().clientaccounts.delete(self.client_id, client_account_id)
        
        data = get_smallinvoice().clientaccounts.all(self.client_id)
        self.assertEquals(0, data['count'])
    
    def test_update_client_accounts(self):
        from smallinvoice.clientaccounts import ClientAccount
        ca = ClientAccount(number=121312313, swift='ABBCCHZZ', clearing='ATBLZ12345', name='tests')
        id = get_smallinvoice().clientaccounts.add(self.client_id, ca)
        client_account_data = get_smallinvoice().clientaccounts.get(self.client_id, id)
        self.assertEqual(ca.number, client_account_data['number'])
        ca.number = 000101010
        get_smallinvoice().clientaccounts.update(self.client_id, ca, id)
        client_account_data = get_smallinvoice().clientaccounts.get(self.client_id, id)
        self.assertEqual(ca.number, client_account_data['number'])
