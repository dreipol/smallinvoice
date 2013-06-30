# coding=utf-8
from smallinvoice.commons import Recipient, Mail, PREVIEW_SIZE
from smallinvoice.letters import Letter, LetterState
from smallinvoice.tests import get_smallinvoice


def test_letters():
    result = get_smallinvoice().letters.all()
    assert len(result) > 0


def test_letter_details():
    details = get_smallinvoice().letters.details(32497)
    print details
    assert details["title"] == "Python-Update"


def test_letter_pdf():
    pdf = get_smallinvoice().letters.pdf(32497)
    assert len(pdf) > 0


def test_letter_preview():
    preview = get_smallinvoice().letters.preview(32497, 1, PREVIEW_SIZE.SMALL)
    assert len(preview) > 0


def test_add_letter():
    l = Letter(client_id=24124, client_address_id=24183, date="2013-01-04",
               title="Python-Test")
    client = get_smallinvoice()
    letter_id = client.letters.add(l)
    details = client.letters.details(letter_id)
    assert details["title"] == "Python-Test"
    client.letters.delete(letter_id)


def test_update_letter():
    l = Letter(client_id=24124, client_address_id=24183, date="2013-01-04",
               title="Python-Update")
    l.id = 32497
    client = get_smallinvoice()
    client.letters.update(l.id, l)
    details = client.letters.details(l.id)
    assert details["title"] == "Python-Update"


def test_email_letter():
    r = Recipient(cc=False, email="wild.etienne@gmail.com", name="Test Name")
    m = Mail(subject="Testsubject", body="Test email body", sendstatus=1,
             afterstatus=1)
    m.add_recipient(r)
    m.id = 32497
    client = get_smallinvoice()
    client.letters.email(m.id, m)
    assert True


def test_status_letter():
    s = LetterState(status=LetterState.DRAFT)
    client = get_smallinvoice()
    client.letters.status(32497, data=s)
    assert client.letters.details(32497)["status"] == 7