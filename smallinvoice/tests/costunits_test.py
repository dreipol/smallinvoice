# coding=utf-8
from smallinvoice.costunits import Costunit
from smallinvoice.tests import get_client


def test_get_all_costunits():
    result = get_client().costunits.all()
    assert len(result) > 0


def test_costunits_details():
    details = get_client().costunits.details(234)
    assert details["name"] == "Kostenstellentest"


def test_add_costunit():
    c = Costunit(name="Testunit", status=1)
    client = get_client()
    costunit_id = client.costunits.add(c)
    details = client.costunits.details(costunit_id)
    assert details["name"] == "Testunit"
    client.costunits.delete(costunit_id)


def test_update_costunit():
    c = Costunit(name="Kostenstellentest", status=1)
    c.id = 234
    client = get_client()
    client.costunits.update(c.id, c)
    details = client.costunits.details(c.id)
    assert details["name"] == "Kostenstellentest"