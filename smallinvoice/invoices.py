from smallinvoice import REQUEST_METHOD, BaseJsonEncodableObject

invoice_list = "invoice/list"
invoice_details = "invoice/get/id/%s"
invoice_pdf = "invoice/pdf/id/%s"
invoice_preview = "invoice/preview/id/%s/page/%s/size/%s"
add_invoice = "invoice/add"
delete_invoice = "invoice/delete/id/%s"
update_invoice = "invoice/edit/id/%s"
email_invoice = "invoice/email/id/%s"
status_invoice = "invoice/status/id/%s"
invoice_payment = "invoice/payment/is/%s"


class Position(BaseJsonEncodableObject):
    def __init__(self, type, number, description, cost, unit, amount, name="",
                 discount=None, vat=0):
        self.type = type
        self.number = number
        self.name = name
        self.description = description
        self.cost = cost
        self.unit = unit
        self.amount = amount
        self.discount = discount
        self.vat = vat


class Invoice(BaseJsonEncodableObject):
    def __init__(self, client_id, client_address_id, currency, date, due,
                 language, positions):
        self.client_id = client_id
        self.client_address_id = client_address_id
        self.currency = currency
        self.date = date
        self.due = due
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


class Payment(BaseJsonEncodableObject):
    def __init__(self, amount, date, type):
        self.amount = amount
        self.date = date
        self.type = type


class State(BaseJsonEncodableObject):
    DRAFT = 0
    SENT = 1
    PAID = 2
    REMINDER = 3

    def __init__(self, status):
        self.status = status


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
        return self.client.request_with_method(invoice_details % (invoice_id,))[
            "item"]

    def pdf(self, invoice_id):
        """ returns the pdf from the invoice as binary data """
        return self.client.request_with_method(invoice_pdf % (invoice_id,))

    def preview(self, invoice_id, page_number, size):
        """ returns a preview from the invoice and the page with the specified size as binary data """
        return self.client.request_with_method(
            invoice_preview % (invoice_id, page_number, size,))

    def add(self, client):
        """ returns the id of the new created invoice """
        return self.client.request_with_method(add_invoice, data=client)["id"]

    def delete(self, invoice_id):
        """ returns an error if the invoice couldn't be deleted """
        return self.client.request_with_method(delete_invoice % (invoice_id,),
                                               request_method=REQUEST_METHOD.POST)

    def update(self, invoice_id, invoice):
        """ returns an error if the invoice couldn't be updated """
        return self.client.request_with_method(update_invoice % (invoice_id,),
                                               data=invoice)

    def email(self, invoice_id, invoice):
        return self.client.request_with_method(email_invoice % (invoice_id,),
                                               data=invoice)

    def status(self, invoice_id, status):
        return self.client.request_with_method(status_invoice % (invoice_id,),
                                               data=status)

    def payment(self, invoice_id, payment):
        return self.client.request_with_method(invoice_payment % (invoice_id,),
                                               data=payment)