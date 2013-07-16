# coding=utf-8
import unittest
from smallinvoice.commons import Recipient, Mail, PREVIEW_SIZE
from smallinvoice.receipts import Receipt, ReceiptState
from smallinvoice.tests import get_smallinvoice, generate_address, \
    generate_customer, generate_position


def generate_receipt():
    return Receipt(
        client_id='',
        client_address_id='',
        currency='CHF',
        date='2013-07-03',
        language='en'
    )


class ReceiptTests(unittest.TestCase):
    def setUp(self):
        self.address = generate_address()
        self.client = generate_customer()
        self.client.add_address(self.address)
        self.position = generate_position()
        self.receipt = generate_receipt()
        self.receipt.add_position(self.position)

        self.customer_id = get_smallinvoice().clients.add(self.client)

        self.receipt.client_id = self.customer_id
        test = get_smallinvoice().clients.details(self.customer_id)
        self.receipt.client_address_id = test['main_address_id']

        self.receipt_id = get_smallinvoice().receipts.add(self.receipt)

    def tearDown(self):
        get_smallinvoice().clients.delete(self.customer_id)
        get_smallinvoice().receipts.delete(self.receipt_id)

    def test_receipt(self):
        self.assertIsNotNone(self.receipt_id)

    def test_receipt_details(self):
        self.assertEqual(self.receipt.date, '2013-07-03')

    def test_receipt_update(self):
        self.assertEqual(self.receipt.date, '2013-07-03')
        self.receipt.date = '2013-07-08'
        self.assertEqual(self.receipt.date, '2013-07-08')

    def test_receipt_pdf(self):
        pdf = get_smallinvoice().receipts.pdf(self.receipt_id)
        self.assertTrue(len(pdf) > 0)

    def test_receipt_preview(self):
        preview = get_smallinvoice().receipts.preview(self.receipt_id, 1,
                                                      PREVIEW_SIZE.SMALL)
        self.assertTrue(len(preview) > 0)

    def test_email_receipt(self):
        r = Recipient(cc=False, email="philipp.laeubli@dreipol.ch",
                      name="Test Name")
        m = Mail(subject="Testsubject", body="Test email body", sendstatus=1,
                 afterstatus=1)
        m.add_recipient(r)
        m.id = self.receipt_id
        get_smallinvoice().receipts.email(m.id, m)
        self.assertEqual(m.id, self.receipt_id)

    def test_status_receipt(self):
        s = ReceiptState(status=ReceiptState.PAID)
        get_smallinvoice().receipts.status(self.receipt_id, data=s)
        self.assertTrue(get_smallinvoice().receipts.details(self.receipt_id)
                        ["status"] == 10)