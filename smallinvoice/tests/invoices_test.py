# coding=utf-8
import unittest
from smallinvoice.commons import Recipient, Mail, PREVIEW_SIZE
from smallinvoice.invoices import Invoice, InvoiceState
from smallinvoice.tests import get_smallinvoice, generate_customer, \
    generate_address, generate_position


def generate_invoice():
    return Invoice(
        client_id='',
        client_address_id='',
        currency="CHF",
        date="2013-07-02",
        due="2013-07-04",
        language="en"
    )


class InvoiceTests(unittest.TestCase):
    def setUp(self):
        self.address = generate_address()
        self.client = generate_customer()
        self.client.add_address(self.address)
        self.position = generate_position()
        self.invoice = generate_invoice()
        self.invoice.add_position(self.position)

        self.customer_id = get_smallinvoice().clients.add(self.client)

        self.invoice.client_id = self.customer_id
        test = get_smallinvoice().clients.details(self.customer_id)
        self.invoice.client_address_id = test['main_address_id']

        self.invoice_id = get_smallinvoice().invoices.add(self.invoice)

    def tearDown(self):
        get_smallinvoice().clients.delete(self.customer_id)
        get_smallinvoice().invoices.delete(self.invoice_id)

    def test_invoice(self):
        self.assertIsNotNone(self.invoice_id)

    def test_invoice_details(self):
        self.assertEqual(self.invoice.currency, 'CHF')

    def test_invoice_update(self):
        self.assertEqual(self.invoice.currency, 'CHF')
        self.invoice.currency = 'Dollar'
        self.assertEqual(self.invoice.currency, 'Dollar')

    def test_invoice_pdf(self):
        pdf = get_smallinvoice().invoices.pdf(self.invoice_id)
        self.assertTrue(len(pdf) > 0)

    def test_invoice_preview(self):
        preview = get_smallinvoice().invoices.preview(self.invoice_id, 1,
                                                      PREVIEW_SIZE.SMALL)
        self.assertTrue(len(preview) > 0)

    def test_email_invoice(self):
        r = Recipient(cc=False, email="philipp.laeubli@dreipol.ch",
                      name="Test Name")
        m = Mail(subject="Testsubject", body="Test email body", sendstatus=1,
                 afterstatus=1)
        m.add_recipient(r)
        m.id = self.invoice_id
        client = get_smallinvoice()
        client.invoices.email(m.id, m)
        self.assertEqual(m.id, self.invoice_id)

    def test_status_invoice(self):
        s = InvoiceState(status=InvoiceState.REMINDER)
        get_smallinvoice().invoices.status(self.invoice_id, data=s)
        self.assertTrue(get_smallinvoice().invoices.details(self.invoice_id)
                        ["status"] == 3)