# coding=utf-8
from smallinvoice import BaseJsonEncodableObject, REQUEST_METHOD, ObjectWithPositions

offer_list = "offer/list"
offer_details = "offer/get/id/%s"
offer_pdf = "offer/pdf/id/%s"
offer_preview = "offer/preview/id/%s/page/%s/size/%s"
add_offer = "offer/add"
delete_offer = "offer/delete/id/%s"
update_offer = "offer/edit/id/%s"
email_offer = "offer/email/id/%s"
status_offer = "offer/status/id/%s"


class Offer(ObjectWithPositions):
    def __init__(self, client_id, client_address_id, currency, date, due,
                 language):
        self.client_id = client_id
        self.client_address_id = client_address_id
        self.currency = currency
        self.date = date
        self.due = due
        self.language = language
        self.positions = []



class OfferState(BaseJsonEncodableObject):
    DRAFT = 0
    SENT = 1
    OK = 9
    REMINDER = 10

    def __init__(self, status):
        self.status = status


class OfferClient(object):
    """ This class wraps all offer related api
    """

    def __init__(self, client):
        """ the OfferClient is only a wrapper of the real client, which must be passed in here"""
        self.client = client

    def all(self):
        """ returns all offers"""
        return self.client.request_with_method(offer_list)["items"]

    def details(self, offer_id):
        """ returns the details to a specific offer """
        return self.client.request_with_method(offer_details % (offer_id,))[
            "item"]

    def pdf(self, offer_id):
        """ returns the pdf from the offer as binary data """
        return self.client.request_with_method(offer_pdf % (offer_id,))

    def preview(self, offer_id, page_number, size):
        """ returns a preview from the offer and the page with the specified size as binary data """
        return self.client.request_with_method(
            offer_preview % (offer_id, page_number, size,))

    def add(self, client):
        return self.client.request_with_method(add_offer, data=client)["id"]

    def delete(self, offer_id):
        return self.client.request_with_method(delete_offer % (offer_id,),
                                               request_method=REQUEST_METHOD.POST)

    def update(self, offer_id, offer):
        return self.client.request_with_method(update_offer % (offer_id,),
                                               data=offer)

    def email(self, offer_id, offer):
        return self.client.request_with_method(email_offer % (offer_id,),
                                               data=offer)

    def status(self, offer_id, status):
        return self.client.request_with_method(status_offer % (offer_id,),
                                               data=status)