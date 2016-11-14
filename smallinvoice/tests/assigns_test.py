# coding=utf-8
import unittest
from smallinvoice.assigns import Assign
from smallinvoice.tests import get_smallinvoice


def generate_assign(date="2013-02-03"):
    return Assign(assign_type=1, type_id=545, hours="6.00", date=date)


class AssignTests(unittest.TestCase):
    def setUp(self):
        self.a = generate_assign()
        self.assign_id = get_smallinvoice().assigns.add(self.a)

    def tearDown(self):
        get_smallinvoice().assigns.delete(self.assign_id)

    def test_assign(self):
        self.assertIsNotNone(self.assign_id)

    def test_update_assign(self):
        self.assertEqual(self.a.hours, "6.00")
        self.a.hours = "4.00"
        self.assertEqual(self.a.hours, "4.00")

    def test_add_assign(self):
        self.assertTrue(self.assign_id)

    def test_detail_assign(self):
        self.assertEqual(self.a.hours, "6.00")
