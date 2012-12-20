__author__ = 'dreimac1'

project_list = "project/list"
project_details = "project/get/id/%s"

class ProjectClient(object):

	def __init__(self, client):
		self.client  = client


	def all(self):
		""" returns all Projects """
		return self.client.request_with_method(project_list)["items"]

	def details(self, client_id):
		""" returns the details to a specific project """
		return self.client.request_with_method(project_details%(client_id,))["item"]