# coding=utf-8
from smallinvoice.commons import Position, Recipient, Mail, PREVIEW_SIZE
from smallinvoice.receipts import Receipt, ReceiptState
from smallinvoice.tests import get_smallinvoice


def test_receipts():
    result = get_smallinvoice().receipts.all()
    assert len(result) > 0


def test_receipt_details():
    details = get_smallinvoice().receipts.details(44714)
    assert details["totalamount"] == 6000


def test_receipt_pdf():
    pdf = get_smallinvoice().receipts.pdf(44714)
    assert len(pdf) > 0


def test_receipt_preview():
    preview = get_smallinvoice().receipts.preview(44714, 1, PREVIEW_SIZE.SMALL)
    assert len(preview) > 0


def generate_position(description="Test"):
    return Position(position_type=1, number=2, name="Basisbeitrag", description=description,
                    cost=6000, unit=3, amount=1)


def generate_receipt():
    return Receipt(client_id=24401, client_address_id=24461, currency="CHF",
                   date="2013-01-03", language="de")


def test_add_receipt():
    p = generate_position()
    r = generate_receipt()
    r.add_position(p)
    client = get_smallinvoice()
    receipt_id = client.receipts.add(r)
    details = client.receipts.details(receipt_id)

    the_position = details["positions"][0]
    assert the_position["description"] == "Test"
    client.receipts.delete(receipt_id)


def test_update_receipt():
    p = generate_position(description="Update")
    p.id = 51090
    r = generate_receipt()
    r.add_position(p)
    r.id = 44714
    client = get_smallinvoice()
    client.receipts.update(r.id, r)
    details = client.receipts.details(r.id)
    the_position = details["positions"][0]
    assert the_position["description"] == "Update"


def test_email_receipt():
    r = Recipient(cc=False, email="wild.etienne@gmail.com", name="Test Name")
    m = Mail(subject="Testsubject", body="Test email body", sendstatus=1,
             afterstatus=1)
    m.add_recipient(r)
    m.id = 44714
    client = get_smallinvoice()
    client.receipts.email(m.id, m)
    assert True


def test_status_receipt():
    s = ReceiptState(status=ReceiptState.PAID)
    client = get_smallinvoice()
    client.receipts.status(44714, data=s)
    assert client.receipts.details(44714)["status"] == 10