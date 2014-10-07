from credit_card import CreditCard
from should_dsl import should, should_not
from ludibrio import Stub
import unittest

class TestCreditCard(unittest.TestCase):
  def setUp(self):
    self.credit_card = CreditCard('1111222233334444', '14/03/18', 1000.0)

  def test_initial_attributes(self):
    self.credit_card.number      |should| equal_to('1111222233334444')
    self.credit_card.expiry_date |should| equal_to('14/03/18')
    self.credit_card.limit       |should| equal_to(1000.0)
    self.credit_card.id          |should| equal_to(1)

  def test_list_from_person(self):
    with Stub() as person: person.id >> 1

    self.credit_card.person_id = person.id

    CreditCard.list_from_person(person) |should| equal_to([self.credit_card])

  def test_month_transactions(self):
    from transaction import Transaction

    with Stub() as first_transaction:
      first_transaction.month >> 10

    with Stub() as second_transaction:
      second_transaction.month >> 10

    with Stub() as third_transaction:
      third_transaction.month >> 11

    Transaction.objects = { 1: first_transaction,
                            2: second_transaction,
                            3: third_transaction }

    # October's transactions
    CreditCard.month_transactions(10) |should| equal_to(
      [first_transaction, second_transaction]
    )

  def test_month_invoice_from_person(self):
    from transaction import Transaction

    with Stub() as first_person: first_person.id >> 1

    # Credit card for first person only.
    self.credit_card.person_id = first_person.id

    with Stub() as first_transaction:
      first_transaction.credit_card_id >> self.credit_card.id
      first_transaction.value >> 100.50
      first_transaction.month >> 10

    with Stub() as second_transaction:
      second_transaction.credit_card_id >> self.credit_card.id
      second_transaction.value >> 200.10
      second_transaction.month >> 10

    Transaction.objects = { 1: first_transaction,
                            2: second_transaction }

    CreditCard.month_invoice_from_person(10, first_person) |should| equal_to(
      300.60
    )

if __name__ == '__main__':
  unittest.main()