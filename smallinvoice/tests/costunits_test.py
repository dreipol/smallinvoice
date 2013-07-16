# coding=utf-8
import unittest
from smallinvoice.costunits import Costunit
from smallinvoice.tests import get_smallinvoice


def generate_costunit():
    return Costunit(
        name="Dollares",
        status=1
    )


class CostunitTests(unittest.TestCase):
    def setUp(self):
        self.costunit = generate_costunit()
        self.costunit_id = get_smallinvoice().costunits.add(self.costunit)

    def tearDown(self):
        get_smallinvoice().costunits.delete(self.costunit_id)

    def test_costunit(self):
        self.assertIsNotNone(self.costunit_id)

    def test_costunit_details(self):
        self.assertEqual(self.costunit.name, 'Dollares')

    def test_costunit_update(self):
        self.assertEqual(self.costunit.name, 'Dollares')
        self.costunit.name = 'Lira'
        self.assertEqual(self.costunit.name, 'Lira')
