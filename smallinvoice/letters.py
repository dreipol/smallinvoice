from smallinvoice import REQUEST_METHOD, BaseJsonEncodableObject

__author__ = 'dreimac1'

letter_list = "letter/list"
letter_details = "letter/get/id/%s"
letter_pdf = "letter/pdf/id/%s"
letter_preview = "letter/preview/id/%s/page/%s/size/%s"
add_letter = "letter/add"
delete_letter = "letter/delete/id/%s"
update_letter = "letter/edit/id/%s"
email_letter = "letter/email/id/%s"
status_letter = "letter/status/id/%s"

class Letter(BaseJsonEncodableObject):
	def __init__(self, client_id, client_address_id, date, title):
		self.client_id = client_id
		self.client_address_id = client_address_id
		self.date = date
		self.title = title

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

	DRAFT = 7
	SENT = 1

	def __init__(self, status):
		self.status = status

class LetterClient(object):
	""" This class wraps all letter related api
	"""
	def __init__(self, client):
		""" the LetterClient is only a wrapper of the real client, which must be passed in here"""
		self.client = client

	def all(self):
		""" returns all letters"""
		return self.client.request_with_method(letter_list)["items"]

	def details(self, letter_id):
		""" returns the details to a specific letter """
		return self.client.request_with_method(letter_details%(letter_id,))["item"]

	def pdf(self, letter_id):
		""" returns the pdf from the letter as binary data """
		return self.client.request_with_method(letter_pdf%(letter_id,))

	def preview(self, letter_id, page_number,size):
		""" returns a preview from the letter and the page with the specified size as binary data """
		return self.client.request_with_method(letter_preview%(letter_id, page_number,size,))

	def add(self, client):
		return self.client.request_with_method(add_letter, data=client)["id"]

	def delete(self, letter_id):
		return self.client.request_with_method(delete_letter%(letter_id,), request_method=REQUEST_METHOD.POST)

	def update(self, letter_id, letter):
		return self.client.request_with_method(update_letter%(letter_id,), data=letter)

	def email(self, letter_id, letter):
		return self.client.request_with_method(email_letter%(letter_id,), data=letter)

	def status(self, letter_id, status):
		return self.client.request_with_method(status_letter%(letter_id,), data=status)