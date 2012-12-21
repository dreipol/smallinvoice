from json import JSONEncoder

__author__ = 'phil'

class PREVIEW_SIZE:
	SMALL = 240
	MEDIUM = 600
	BIG = 825
	HUGE = 1240

class REQUEST_METHOD:
	AUTO = 0
	POST = 1
	GET = 2

class SmallInvoiceException(Exception):
	""" Base class for all exceptions raised by smallinvoice """
	def __init__(self, message):
		final_message = "smallinvoice-client exception: %s" % (message)
		super(Exception, self).__init__(final_message)

class SmallInvoiceConfigurationException(SmallInvoiceException):
	""" Thrown when the client is not properl configurated"""
	def __init__(self, client):
		message = "Wrong configuration.: "\
				  "token: %s" % (client.api_token,)
		super(SmallInvoiceException, self).__init__(message)

class SmallInvoiceConnectionException(SmallInvoiceException):
	""" The client could not connect for any reason. """
	def __init__(self, status_code, remote_message):
		message = "Failed to Connect, Status %s; Message: %s" % (status_code, remote_message)
		super(SmallInvoiceException, self).__init__(message)

class BaseEncoder(JSONEncoder):
	def default(self,o):
		return o.__dict__

class BaseJsonEncodableObject():
	""" This class can be easily encode into a json string by calling encode
	"""
	def encode(self):
		return BaseEncoder().encode(self)
