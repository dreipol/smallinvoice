from smallinvoice import RESPONSE_TYPE

__author__ = 'phil'

invoice_list = "invoice"
invoice_details = "invoice/id/%s"
invoice_pdf = "invoice/id/%s/type/pdf"
invoice_preview = "invoice/id/%s/type/preview/page/%s/size/%s"


class InvoiceClient(object):
	""" This class wraps all invoice related api
	"""
	def __init__(self, client):
		""" the InvoiceClient is only a wrapper of the real client, which must be passed in here"""
		self.client = client

	def all(self):
		""" returns all invoices"""
		return self.client.request_with_method(invoice_list)

	def details(self, invoice_id):
		""" returns the details to a specific invoice """
		return self.client.request_with_method(invoice_details%(invoice_id,))

	def pdf(self, invoice_id):
		""" returns the pdf from the invoice as binary data """
		return self.client.request_with_method(invoice_pdf%(invoice_id,), type=RESPONSE_TYPE.RAW)

	def preview(self, invoice_id, page_number,size):
		""" returns a preview from the invoice and the page with the specified size as binary data """
		return self.client.request_with_method(invoice_preview%(invoice_id, page_number,size,), type=RESPONSE_TYPE.RAW)
