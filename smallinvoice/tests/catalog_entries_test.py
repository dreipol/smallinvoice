# coding=utf-8
from smallinvoice.catalog import Catalog
from smallinvoice.tests import get_smallinvoice


def test_get_all_catalog_entries():
    result = get_smallinvoice().catalogs.all()
    assert len(result) > 0


def test_catalog_entry_details():
    details = get_smallinvoice().catalogs.details(1696)
    assert details["name"] == "Halbe Tage ohne Essen"


def test_add_catalog():
    c = Catalog(catalog_type=1, unit=2, name="Add_Test", cost_per_unit=50)
    client = get_smallinvoice()
    catalog_id = client.catalogs.add(c)
    details = client.catalogs.details(catalog_id)
    assert details["name"] == "Add_Test"
    client.catalogs.delete(catalog_id)


def test_update_catalog():
    c = Catalog(catalog_type=1, unit=2, name="Update", cost_per_unit=50)
    c.id = 178187
    client = get_smallinvoice()
    client.catalogs.update(c.id, c)
    details = client.catalogs.details(c.id)
    assert details["name"] == "Update"