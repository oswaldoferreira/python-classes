from transaction import Transaction

class Seller(object):
  objects = {}

  def __init__(self, name, document):
    self.name     = name
    self.document = document
    self.id       = len(Seller.objects) + 1

  @classmethod
  def transactions_list(self, month):
    transactions = []

    for transaction in Transaction.objects.values():
      if transaction.month == month:
        transactions.append(transaction)

    return transactions