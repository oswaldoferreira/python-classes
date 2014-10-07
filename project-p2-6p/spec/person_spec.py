from person import Person
from should_dsl import should, should_not
from ludibrio import Stub
import unittest

class TestPerson(unittest.TestCase):
  def setUp(self):
    Person.objects = {}
    self.person = Person('Oswaldo')

  def test_initial_attributes(self):
    self.person.name |should| equal_to('Oswaldo')
    self.person.id   |should| equal_to(1)

  def test_persistence(self):
    Person.objects |should| equal_to({ 'Oswaldo': self.person })

  def test_credit_cards(self):
    with Stub() as first_credit_card:
      first_credit_card.person_id >> self.person.id
      first_credit_card.id >> 1

    # Another person credit card
    with Stub() as second_credit_card:
      second_credit_card.person_id >> 'another-id'
      second_credit_card.id >> 2

    from credit_card import CreditCard
    CreditCard.objects = { 1: first_credit_card, 2: second_credit_card }

    self.person.credit_cards() |should| equal_to([first_credit_card])

if __name__ == '__main__':
  unittest.main()