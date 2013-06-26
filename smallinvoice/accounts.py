from smallinvoice import BaseJsonEncodableObject, REQUEST_METHOD

account_list = 'account/list'
add_account = "account/add"
account_details = 'account/get/id/%s'
update_account= 'account/edit/id/%s'
delete_account = "account/delete/id/%s"
class Account(BaseJsonEncodableObject):

    def __init__(self, title, institute, number, iban, swiftbic, clearing, postaccount,lsv,dd,esr):
        self.title = title
        self.institute = institute
        self.number = number
        self.iban = iban
        self.swiftbic = swiftbic
        self.clearing = clearing
        self.postaccount = postaccount
        self.lsv = lsv
        self.dd = dd
        self.esr = esr


class AccountClient(object):

    def __init__(self, client):
        self.client = client

    def all(self):
        return self.client.request_with_method(account_list)['items']

    def details(self, client_id):
        return self.client.request_with_method(account_details % (client_id,))

    def add(self, account):
        return self.client.request_with_method(add_account, data=account)["id"]

    def delete(self, account_id):
        return self.client.request_with_method(delete_account % (account_id,),
                                               request_method=REQUEST_METHOD.POST)

    def update(self, account_id, account):
        return self.client.request_with_method(update_account % (account_id,),
                                               data=account)