from smallinvoice import REQUEST_METHOD, BaseJsonEncodableObject

__author__ = 'dreimac1'

project_list = "project/list"
project_details = "project/get/id/%s"
add_project = "project/add"
delete_project = "project/delete/id/%s"
update_project = "project/edit/id/%s"

class Project(BaseJsonEncodableObject):
	def __init__(self, name, client_id):


		self.name = name
		self.client_id = client_id

class ProjectClient(object):

	def __init__(self, client):
		self.client  = client


	def all(self):
		""" returns all Projects """
		return self.client.request_with_method(project_list)["items"]

	def details(self, client_id):
		""" returns the details to a specific project """
		return self.client.request_with_method(project_details%(client_id,))["item"]

	def add(self, client):
		return self.client.request_with_method(add_project, data=client)["id"]

	def delete(self, project_id):
		return self.client.request_with_method(delete_project%(project_id,), request_method=REQUEST_METHOD.POST)

	def update(self, project_id, project):
		return self.client.request_with_method(update_project%(project_id,), data=project)