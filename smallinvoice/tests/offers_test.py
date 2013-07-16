# coding=utf-8
import unittest
from smallinvoice.commons import Recipient, Mail, PREVIEW_SIZE
from smallinvoice.offers import Offer, OfferState
from smallinvoice.tests import get_smallinvoice, generate_address, \
    generate_customer, generate_position


def generate_offer():
    return Offer(
        client_id='',
        client_address_id='',
        currency='CHF',
        date='2013-07-03',
        due='2013-07-28',
        language='en'
    )


class OfferTests(unittest.TestCase):
    def setUp(self):
        self.address = generate_address()
        self.client = generate_customer()
        self.client.add_address(self.address)
        self.position = generate_position()
        self.offer = generate_offer()
        self.offer.add_position(self.position)

        self.customer_id = get_smallinvoice().clients.add(self.client)

        self.offer.client_id = self.customer_id
        test = get_smallinvoice().clients.details(self.customer_id)
        self.offer.client_address_id = test['main_address_id']

        self.offer_id = get_smallinvoice().offers.add(self.offer)

    def tearDown(self):
        get_smallinvoice().clients.delete(self.customer_id)
        get_smallinvoice().offers.delete(self.offer_id)

    def test_offer(self):
        self.assertIsNotNone(self.offer_id)

    def test_offer_details(self):
        self.assertEqual(self.offer.language, 'en')

    def test_offer_update(self):
        self.assertEqual(self.offer.language, 'en')
        self.offer.language = 'de'
        self.assertEqual(self.offer.language, 'de')

    def test_offer_pdf(self):
        pdf = get_smallinvoice().offers.pdf(self.offer_id)
        self.assertTrue(len(pdf) > 0)

    def test_offer_preview(self):
        preview = get_smallinvoice().offers.preview(self.offer_id, 1,
                                                    PREVIEW_SIZE.SMALL)
        self.assertTrue(len(preview) > 0)

    def test_email_offer(self):
        r = Recipient(cc=False, email="philipp.laeubli@dreipol.ch",
                      name="Test Name")
        m = Mail(subject="Testsubject", body="Test email body", sendstatus=1,
                 afterstatus=1)
        m.add_recipient(r)
        m.id = self.offer_id
        get_smallinvoice().offers.email(m.id, m)
        self.assertEqual(m.id, self.offer_id)

    def test_status_offer(self):
        s = OfferState(status=OfferState.OK)
        get_smallinvoice().offers.status(self.offer_id, data=s)
        self.assertTrue(get_smallinvoice().offers.details(self.offer_id)
                        ["status"] == 9)