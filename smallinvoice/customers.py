from smallinvoice import BaseJsonEncodableObject, REQUEST_METHOD

__author__ = 'dreimac1'

all_clients = "client/list"
client_details = "client/get/id/%s"
add_client = "client/add"
delete_client = "client/delete/id/%s"
update_client = "client/edit/id/%s"

class Address(BaseJsonEncodableObject):

	def __init__(self, primary, street, streetno, city, code, country, street2=""):

		self.primary = primary
		self.street = street
		self.streetno = streetno
		self.street2 = street2
		self.city = city
		self.code = code
		self.country = country


class CUSTOMER_TYPE():
	COMPANY = 1
	PRIVATE = 2

class CUSTOMER_GENDER():
	MALE = 1
	FEMALE = 2


class Customer(BaseJsonEncodableObject):

	def __init__(self, type,gender,name,language,addresses):
		self.type = type
		self.gender = gender
		self.name = name
		self.language = language
		self.addresses = addresses



class CustomerClient(object):

	def __init__(self, client):
		self.client  = client

	def all(self):
		""" returns all Clients """
		return self.client.request_with_method(all_clients)["items"]

	def details(self, client_id):
		""" returns the details to a specific client """
		return self.client.request_with_method(client_details%(client_id,))["item"]

	def add(self, client):
		return self.client.request_with_method(add_client, data=client)["id"]

	def delete(self, client_id):
		return self.client.request_with_method(delete_client%(client_id,), request_method=REQUEST_METHOD.POST)

	def update(self, client_id, client):
		return self.client.request_with_method(update_client%(client_id,), data=client)