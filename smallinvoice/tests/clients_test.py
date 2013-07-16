# coding=utf-8
import unittest
from smallinvoice.tests import get_smallinvoice, generate_customer, \
    generate_address


class ClientTests(unittest.TestCase):
    def setUp(self):
        self.address = generate_address()
        self.client = generate_customer()
        self.client.add_address(self.address)
        self.client_id = get_smallinvoice().clients.add(self.client)

    def tearDown(self):
        get_smallinvoice().clients.delete(self.client_id)

    def test_client(self):
        self.assertIsNotNone(self.client_id)

    def test_client_details(self):
        self.assertEqual(self.client.name, 'Hanspeter Muster')

    def test_clinet_address(self):
        self.assertEqual(self.address.street, 'Kernstrasse')

    def test_client_update(self):
        self.assertEqual(self.client.name, 'Hanspeter Muster')
        self.client.name = 'Hans Meier'
        self.assertEqual(self.client.name, 'Hans Meier')

    def test_address_update(self):
        self.assertEqual(self.address.street, 'Kernstrasse')
        self.address.street = 'Muehlestrasse'
        self.assertEqual(self.address.street, 'Muehlestrasse')