# coding=utf-8
from smallinvoice.assigns import Assign
from smallinvoice.tests import get_client


def generate_assign(date="2013-02-03"):
    return Assign(assign_type=1, type_id=545, hours="8.00", date=date)


def test_get_all_assigns():
    result = get_client().assigns.all()
    print result
    assert len(result) > 0


def test_assigns_details():
    details = get_client().assigns.details(12542)
    print(details)
    assert details["employee"] == "Andreas Graf"


def test_add_assign():
    a = generate_assign()
    client = get_client()
    assign_id = client.assigns.add(a)
    details = client.assigns.details(assign_id)
    assert details["date"] == "2013-02-03"
    client.assigns.delete(assign_id)


def test_update_assign():
    a = generate_assign(date="2013-03-03")
    a.id = 12542
    client = get_client()
    client.assigns.update(a.id, a)
    details = client.assigns.details(a.id)
    assert details["date"] == "2013-03-03"