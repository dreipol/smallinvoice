# coding=utf-8
import unittest
from smallinvoice.tests import get_smallinvoice
from smallinvoice.time import Time


def generate_time():
    return Time(
        start='0900',
        end='2100',
        date='2013-07-03'
    )


class TimeTests(unittest.TestCase):
    def setUp(self):
        self.time = generate_time()
        self.time_id = get_smallinvoice().times.add(self.time)

    def tearDown(self):
        get_smallinvoice().times.delete(self.time_id)

    def test_time(self):
        self.assertIsNotNone(self.time_id)

    def test_time_details(self):
        self.assertEqual(self.time.date, '2013-07-03')

    def test_time_update(self):
        self.assertEqual(self.time.start, '0900')
        self.time.start = '1100'
        self.assertEqual(self.time.start, '1100')
