__author__ = 'dreimac1'

receipt_list = "receipt/list"
receipt_details = "receipt/get/id/%s"
receipt_pdf = "receipt/pdf/id/%s"
receipt_preview = "receipt/preview/id/%s/page/%s/size/%s"


class ReceiptClient(object):
	""" This class wraps all receipt related api
	"""
	def __init__(self, client):
		""" the ReceiptClient is only a wrapper of the real client, which must be passed in here"""
		self.client = client

	def all(self):
		""" returns all receipts"""
		return self.client.request_with_method(receipt_list)["items"]

	def details(self, receipt_id):
		""" returns the details to a specific receipt """
		return self.client.request_with_method(receipt_details%(receipt_id,))["item"]

	def pdf(self, receipt_id):
		""" returns the pdf from the receipt as binary data """
		return self.client.request_with_method(receipt_pdf%(receipt_id,))

	def preview(self, receipt_id, page_number,size):
		""" returns a preview from the receipt and the page with the specified size as binary data """
		return self.client.request_with_method(receipt_preview%(receipt_id, page_number,size,))