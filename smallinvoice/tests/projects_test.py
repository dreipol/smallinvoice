# coding=utf-8
from smallinvoice.projects import Project
from smallinvoice.tests import get_smallinvoice


def test_get_all_projects():
    result = get_smallinvoice().projects.all()
    assert len(result) > 0


def test_project_details():
    details = get_smallinvoice().projects.details(545)
    print(details)
    assert details["estimate"] == 20


def test_add_project():
    p = Project(name="Testprojekt", client_id=24401)
    client = get_smallinvoice()
    project_id = client.projects.add(p)
    details = client.projects.details(project_id)
    assert details["name"] == "Testprojekt"
    client.projects.delete(project_id)


def test_update_project():
    p = Project(name="Test Projekt", client_id=24124)
    p.id = 545
    client = get_smallinvoice()
    client.projects.update(p.id, p)
    details = client.projects.details(p.id)
    assert details["name"] == "Test Projekt"