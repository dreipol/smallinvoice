__author__ = 'phil'

invoice_list = "invoice/list"
invoice_details = "invoice/get/id/%s"
invoice_pdf = "invoice/pdf/id/%s"
invoice_preview = "invoice/preview/id/%s/page/%s/size/%s"


class InvoiceClient(object):
	""" This class wraps all invoice related api
	"""
	def __init__(self, client):
		""" the InvoiceClient is only a wrapper of the real client, which must be passed in here"""
		self.client = client

	def all(self):
		""" returns all invoices"""
		return self.client.request_with_method(invoice_list)["items"]

	def details(self, invoice_id):
		""" returns the details to a specific invoice """
		return self.client.request_with_method(invoice_details%(invoice_id,))["item"]

	def pdf(self, invoice_id):
		""" returns the pdf from the invoice as binary data """
		return self.client.request_with_method(invoice_pdf%(invoice_id,))

	def preview(self, invoice_id, page_number,size):
		""" returns a preview from the invoice and the page with the specified size as binary data """
		return self.client.request_with_method(invoice_preview%(invoice_id, page_number,size,))
