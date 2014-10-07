from credit_card import CreditCard

class Person(object):
  objects = {}

  def __init__(self, name):
    self.name = name
    self.id   = len(Person.objects) + 1

    Person.objects[name] = self

  def credit_cards(self):
    credit_cards = []

    for credit_card in CreditCard.objects.values():
      if credit_card.person_id == self.id:
        credit_cards.append(credit_card)

    return credit_cards
