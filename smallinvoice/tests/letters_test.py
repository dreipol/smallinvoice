# coding=utf-8
import unittest
from smallinvoice.commons import Recipient, Mail, PREVIEW_SIZE
from smallinvoice.letters import Letter, LetterState
from smallinvoice.tests import get_smallinvoice, generate_address, \
    generate_customer


def generate_letter():
    return Letter(
        client_id='',
        client_address_id='',
        date='2013-07-03',
        title='Congratulations'
    )


class LetterTests(unittest.TestCase):
    def setUp(self):
        self.address = generate_address()
        self.client = generate_customer()
        self.client.add_address(self.address)
        self.letter = generate_letter()
        self.customer_id = get_smallinvoice().clients.add(self.client)

        self.letter.client_id = self.customer_id
        test = get_smallinvoice().clients.details(self.customer_id)
        self.letter.client_address_id = test['main_address_id']

        self.letter_id = get_smallinvoice().letters.add(self.letter)

    def tearDown(self):
        get_smallinvoice().clients.delete(self.customer_id)
        get_smallinvoice().letters.delete(self.letter_id)

    def test_letter(self):
        self.assertIsNotNone(self.letter_id)

    def test_letter_details(self):
        self.assertEqual(self.letter.title, 'Congratulations')

    def test_letter_update(self):
        self.assertEqual(self.letter.title, 'Congratulations')
        self.letter.title = 'Updated Title'
        self.assertEqual(self.letter.title, 'Updated Title')

    def test_letter_pdf(self):
        pdf = get_smallinvoice().letters.pdf(self.letter_id)
        self.assertTrue(len(pdf) > 0)

    def test_letter_preview(self):
        preview = get_smallinvoice().letters.preview(self.letter_id, 1,
                                                     PREVIEW_SIZE.SMALL)
        self.assertTrue(len(preview) > 0)

    def test_email_letter(self):
        r = Recipient(cc=False, email="philipp.laeubli@dreipol.ch",
                      name="Test Name")
        m = Mail(subject="Testsubject", body="Test email body", sendstatus=1,
                 afterstatus=1)
        m.add_recipient(r)
        m.id = self.letter_id
        get_smallinvoice().letters.email(m.id, m)
        self.assertEqual(m.id, self.letter_id)

    def test_status_letter(self):
        s = LetterState(status=LetterState.DRAFT)
        get_smallinvoice().letters.status(self.letter_id, data=s)
        self.assertTrue(get_smallinvoice().letters.details(self.letter_id)
                        ["status"] == 7)