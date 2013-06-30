# coding=utf-8
from smallinvoice.tests import get_smallinvoice, generate_customer, generate_address


def test_get_all_clients():
    smallinvoice = get_smallinvoice()
    result = smallinvoice.clients.all()
    assert len(result) > 0


def test_client_details():
    details = get_smallinvoice().clients.details(24401)
    assert details["addition"] == "Andreas Graf"


def test_add_address():
    c = generate_customer()
    c.add_address(generate_address())
    client = get_smallinvoice()
    client_id = client.clients.add(c)
    details = client.clients.details(client_id)
    assert details["name"] == "Hanspeter Muster"
    client.clients.delete(client_id)


def test_update_client():
    a = generate_address()
    a.id = 50341
    c = generate_customer(name="Hans Muster")
    c.add_address(a)
    c.id = 49677
    client = get_smallinvoice()
    client.clients.update(c.id, c)
    details = client.clients.details(c.id)
    assert details["name"] == "Hans Muster"