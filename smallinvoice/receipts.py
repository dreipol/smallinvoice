from smallinvoice import REQUEST_METHOD, BaseJsonEncodableObject

__author__ = 'dreimac1'

receipt_list = "receipt/list"
receipt_details = "receipt/get/id/%s"
receipt_pdf = "receipt/pdf/id/%s"
receipt_preview = "receipt/preview/id/%s/page/%s/size/%s"
add_receipt = "receipt/add"
delete_receipt = "receipt/delete/id/%s"
update_receipt = "receipt/edit/id/%s"
email_receipt = "receipt/email/id/%s"
status_receipt = "receipt/status/id/%s"

class Position(BaseJsonEncodableObject):

	def __init__(self, type, number, description, cost, unit, amount, name="", discount=None, vat=0):


		self.type = type
		self.number = number
		self.name = name
		self.description = description
		self.cost = cost
		self.unit = unit
		self.amount = amount
		self.discount = discount
		self.vat = vat

class Receipt(BaseJsonEncodableObject):

	def __init__(self, client_id, client_address_id, currency, date, language, positions):

		self.client_id = client_id
		self.client_address_id = client_address_id
		self.currency = currency
		self.date = date
		self.language = language
		self.positions = positions

class Recipient(BaseJsonEncodableObject):

	def __init__(self, cc, email, name):

		self.cc = cc
		self.email = email
		self.name = name

class Mail(BaseJsonEncodableObject):

	def __init__(self, subject, body, sendstatus, afterstatus, recipients):

		self.subject = subject
		self.body = body
		self.sendstatus = sendstatus
		self.afterstatus = afterstatus
		self.recipients = recipients

class State(BaseJsonEncodableObject):

	DRAFT = 0
	SENT = 1
	PAID = 10

	def __init__(self, status):
		self.status = status

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

	def add(self, client):
		return self.client.request_with_method(add_receipt, data=client)["id"]

	def delete(self, receipt_id):
		return self.client.request_with_method(delete_receipt%(receipt_id,), request_method=REQUEST_METHOD.POST)

	def update(self, receipt_id, receipt):
		return self.client.request_with_method(update_receipt%(receipt_id,), data=receipt)

	def email(self, receipt_id, receipt):
		return self.client.request_with_method(email_receipt%(receipt_id,), data=receipt)

	def status(self, receipt_id, status):
		return self.client.request_with_method(status_receipt%(receipt_id,), data=status)