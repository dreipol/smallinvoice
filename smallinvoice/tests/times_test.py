# coding=utf-8
import datetime
from smallinvoice.tests import get_smallinvoice
from smallinvoice.time import Time


def test_get_all_times():
    result = get_smallinvoice().times.all()
    assert len(result) > 0


def test_times_details():
    details = get_smallinvoice().times.details(7706)
    assert details["start"] == 900


def test_add_time():
    t = Time(start="0900", end="1200", date=datetime.date.today().strftime('%Y-%m-%d'))
    client = get_smallinvoice()
    time_id = client.times.add(t)
    details = client.times.details(time_id)
    assert details["start"] == 900
    client.times.delete(time_id)


def test_update_time():
    t = Time(start="0900", end="1200", date="2013-01-03")
    t.id = 7706
    client = get_smallinvoice()
    client.times.update(t.id, t)
    details = client.times.details(t.id)
    assert details["start"] == 900