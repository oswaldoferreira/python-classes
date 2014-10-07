from datetime import datetime

class Transaction(object):
  objects = {}

  def __init__(self, date, value):
    self.date           = date
    self.value          = value
    self.month          = date.month
    self.id             = len(Transaction.objects) + 1
    self.credit_card_id = None

    Transaction.objects[self.id] = self

  def associate_credit_card(self, credit_card):
    self.credit_card_id = credit_card.id

  def associate_seller(self, seller):
    self.seller_id = seller.id

