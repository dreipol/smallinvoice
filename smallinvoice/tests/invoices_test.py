# coding=utf-8
from smallinvoice import PREVIEW_SIZE
from smallinvoice.common import Position, Recipient, Mail
from smallinvoice.invoices import Invoice, InvoiceState, Payment
from smallinvoice.tests import get_client, generate_customer, generate_address


def test_invoices():
    invoices = get_client().invoices.all()
    assert len(invoices) > 0


def test_invoice_details():
    details = get_client().invoices.details(25676)
    assert details["totalamount"] == 1440


def test_invoice_pdf():
    pdf = get_client().invoices.pdf(25676)
    assert len(pdf) > 0


def test_invoice_preview():
    preview = get_client().invoices.preview(25676, 1, PREVIEW_SIZE.SMALL)
    assert len(preview) > 0


def test_add_invoice():

    customer = generate_customer()

    address = generate_address()

    customer.add_address(address)
    customer.iban = 'CH9300762011623852957'
    customer.clearing = '123123'
    customer.bic = 'BNPAFRPP'

    client = get_client()
    client_id = client.clients.add(customer)
    det = client.clients.details(client_id)
    p = Position(position_type=1, number=2, name="Basisbeitrag", description="Test",
                 cost=99099, unit=3, amount=1)
    i = Invoice(client_id=client_id, client_address_id=det['main_address_id'], currency="CHF",
                date="2013-01-03", due="2013-01-24", language="de",
                )
    i.add_position(p)
    i.dd = 1
    invoice_id = client.invoices.add(i)
    details = client.invoices.details(invoice_id)

    the_position = details["positions"][0]
    assert the_position["name"] == "Basisbeitrag"
    client.invoices.delete(invoice_id)

#
def test_update_invoice():
    p = Position(position_type=1, number=2, name="Basisbeitrag", description="Update",
                 cost=1440, unit=3, amount=1)
    p.id = 51090
    i = Invoice(client_id=24401, client_address_id=24461, currency="CHF",
                date="2013-01-03", due="2013-01-24", language="de")
    i.id = 25676
    i.add_position(p)
    client = get_client()
    client.invoices.update(i.id, i)
    details = client.invoices.details(i.id)
    the_position = details["positions"][0]
    assert the_position["description"] == "Update"


def test_email_invoice():
    r = Recipient(cc=False, email="wild.etienne@gmail.com", name="Test Name")
    m = Mail(subject="Testsubject", body="Test email body", sendstatus=1,
             afterstatus=1)
    m.add_recipient(r)
    m.id = 25676
    client = get_client()
    client.invoices.email(m.id, m)
    assert True


def test_status_invoice():
    s = InvoiceState(status=InvoiceState.REMINDER)
    client = get_client()
    client.invoices.status(25676, status=s)
    assert client.invoices.details(25676)["status"] == 3


def test_invoice_payment():
    client = get_client()
    p = Position(position_type=1, number=2, name="Basisbeitrag", description="Test",
                 cost=6000, unit=3, amount=1)
    i = Invoice(client_id=24401, client_address_id=24461, currency="CHF",
                date="2013-01-03", due="2013-08-24", language="de",)

    i.add_position(p)
    invoice_id = client.invoices.add(i)
    payment = Payment(amount=6000, date="2014-01-03", payment_type=1)

    client.invoices.payment(invoice_id, payment)
    assert client.invoices.details(invoice_id)["date"] == "2013-01-03"
