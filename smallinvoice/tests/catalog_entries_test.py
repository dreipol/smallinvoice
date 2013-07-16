# coding=utf-8
import unittest
from smallinvoice.catalog import Catalog
from smallinvoice.tests import get_smallinvoice


def generate_catalog():
    return Catalog(catalog_type='1',
                   unit='2',
                   name='Unit Test',
                   cost_per_unit=100)


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.c = generate_catalog()
        self.catalog_id = get_smallinvoice().catalogs.add(self.c)

    def tearDown(self):
        get_smallinvoice().catalogs.delete(self.catalog_id)

    def test_catalog(self):
        self.assertIsNotNone(self.catalog_id)

    def test_catalog_details(self):
        self.assertEqual(self.c.name, 'Unit Test')

    def test_catalog_add(self):
        self.assertTrue(self.catalog_id)

    def test_catalog_update(self):
        self.assertEqual(self.c.name, 'Unit Test')
        self.c.name = 'Test Change'
        self.assertEqual(self.c.name, 'Test Change')