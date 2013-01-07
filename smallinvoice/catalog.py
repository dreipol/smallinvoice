from smallinvoice import REQUEST_METHOD, BaseJsonEncodableObject

__author__ = 'dreimac1'

all_cataloge_entries = "catalog/list"
catalog_entry_details = "catalog/get/id/%s"
add_catalog = "catalog/add"
delete_catalog = "catalog/delete/id/%s"
update_catalog = "catalog/edit/id/%s"

class Catalog(BaseJsonEncodableObject):
	def __init__(self, type, unit, name, cost_per_unit, vat=0):


		self.type = type
		self.unit = unit
		self.name = name
		self. cost_per_unit = cost_per_unit
		self.vat = vat



class CatalogClient(object):

	def __init__(self, client):
		self.client  = client


	def all(self):
		""" returns all Catalog entries """
		return self.client.request_with_method(all_cataloge_entries)["items"]

	def details(self, catalog_id):
		""" returns the details to a specific catalog entry """
		return self.client.request_with_method(catalog_entry_details%(catalog_id,))["item"]

	def add(self, client):
		return self.client.request_with_method(add_catalog, data=client)["id"]

	def delete(self, catalog_id):
		return self.client.request_with_method(delete_catalog%(catalog_id,), request_method=REQUEST_METHOD.POST)

	def update(self, catalog_id, catalog):
		return self.client.request_with_method(update_catalog%(catalog_id,), data=catalog)