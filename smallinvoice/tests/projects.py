from smallinvoice.client import *
from smallinvoice.projects import *
from smallinvoice.tests import TEST_API_TOKEN

def test_get_all_projects():
	client = Client(TEST_API_TOKEN)
	result = client.projects.all()
	assert len(result)>0

def test_project_details():
	client =  Client(TEST_API_TOKEN)
	details = client.projects.details(545)
	print(details)
	assert details["estimate"] == "20"

def test_add_project():
	p = Project(name="Testprojekt", client_id=24401)
	client = Client(TEST_API_TOKEN)
	project_id = client.projects.add(p)
	details=client.projects.details(project_id)
	assert details["name"] == "Testprojekt"
	client.projects.delete(project_id)

def test_update_project():
	p = Project(name="Test Projekt", client_id=24124)
	p.id = 545
	client =  Client(TEST_API_TOKEN)
	client.projects.update(p.id,p)
	details = client.projects.details(p.id)
	assert details["name"] == "Test Projekt"