from transaction import Transaction

class CreditCard(object):
  objects = {}

  def __init__(self, number, expiry_date, limit):
    self.number      = number
    self.expiry_date = expiry_date
    self.limit       = limit
    self.id          = len(CreditCard.objects) + 1
    self.person_id   = None

    CreditCard.objects[number] = self

  @classmethod
  def list_from_person(cls, person):
    credit_cards = []

    for credit_card in cls.objects.values():
      if credit_card.person_id == person.id:
        credit_cards.append(credit_card)

    return credit_cards

  @classmethod
  def month_transactions(cls, month):
    transactions = []

    for transaction in Transaction.objects.values():
      if transaction.month == month:
        transactions.append(transaction)

    return transactions

  @classmethod
  def month_invoice_from_person(cls, month, person):
    total = 0

    for credit_card in cls.list_from_person(person):
      for transaction in Transaction.objects.values():
        if transaction.credit_card_id == credit_card.id:
          total += transaction.value

    return total