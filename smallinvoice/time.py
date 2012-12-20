__author__ = 'dreimac1'

time_list = "time/list"
time_details = "time/get/id/%s"

class TimeClient(object):

	def __init__(self, client):
		self.client  = client


	def all(self):
		""" returns all Times """
		return self.client.request_with_method(time_list)["items"]

	def details(self, client_id):
		""" returns the details to a specific time """
		return self.client.request_with_method(time_details%(client_id,))["item"]