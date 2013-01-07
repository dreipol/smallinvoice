from smallinvoice import REQUEST_METHOD, BaseJsonEncodableObject

__author__ = 'dreimac1'

time_list = "time/list"
time_details = "time/get/id/%s"
add_time = "time/add"
delete_time = "time/delete/id/%s"
update_time = "time/edit/id/%s"

class Time(BaseJsonEncodableObject):

	def __init__(self, start, end, date):
		self.start = start
		self.end = end
		self.date = date


class TimeClient(object):

	def __init__(self, client):
		self.client  = client


	def all(self):
		""" returns all Times """
		return self.client.request_with_method(time_list)["items"]

	def details(self, client_id):
		""" returns the details to a specific time """
		return self.client.request_with_method(time_details%(client_id,))["item"]

	def add(self, client):
		return self.client.request_with_method(add_time, data=client)["id"]

	def delete(self, time_id):
		return self.client.request_with_method(delete_time%(time_id,), request_method=REQUEST_METHOD.POST)

	def update(self, time_id, time):
		return self.client.request_with_method(update_time%(time_id,), data=time)