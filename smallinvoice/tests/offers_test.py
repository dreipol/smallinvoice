# coding=utf-8
from smallinvoice.commons import Position, Recipient, Mail, PREVIEW_SIZE
from smallinvoice.offers import Offer, OfferState
from smallinvoice.tests import get_smallinvoice


def test_offers():
    result = get_smallinvoice().offers.all()
    assert len(result) > 0


def test_offer_details():
    details = get_smallinvoice().offers.details(26193)
    assert details["totalamount"] == 1350


def test_offer_pdf():
    pdf = get_smallinvoice().offers.pdf(26193)
    assert len(pdf) > 0


def test_offer_preview():
    preview = get_smallinvoice().offers.preview(26193, 1, PREVIEW_SIZE.SMALL)
    assert len(preview) > 0


def test_add_offer():
    p = Position(position_type=1, number=2, name="Basisbeitrag", description="Test",
                 cost=6000, unit=3, amount=1)
    o = Offer(client_id=24401, client_address_id=24461, currency="CHF",
              date="2013-01-03", due="2013-01-24", language="de")

    o.add_position(p)
    client = get_smallinvoice()
    offer_id = client.offers.add(o)
    details = client.offers.details(offer_id)

    the_position = details["positions"][0]
    assert the_position["description"] == "Test"
    client.offers.delete(offer_id)


def test_update_offer():
    p = Position(position_type=1, number=2, name="Basisbeitrag", description="Update",
                 cost=1350, unit=3, amount=1)
    p.id = 51090
    o = Offer(client_id=24401, client_address_id=24461, currency="CHF",
              date="2013-01-03", due="2013-01-24", language="de")
    o.add_position(p)
    o.id = 26193
    client = get_smallinvoice()
    client.offers.update(o.id, o)
    details = client.offers.details(o.id)
    the_position = details["positions"][0]
    assert the_position["description"] == "Update"


def test_email_offer():
    r = Recipient(cc=False, email="wild.etienne@gmail.com", name="Test Name")
    m = Mail(subject="Testsubject", body="Test email body", sendstatus=1,
             afterstatus=1)
    m.add_recipient(r)
    m.id = 26193
    client = get_smallinvoice()
    client.offers.email(m.id, m)
    assert True


def test_status_invoice():
    s = OfferState(status=OfferState.OK)
    client = get_smallinvoice()
    client.offers.status(26193, data=s)
    assert client.offers.details(26193)["status"] == 9