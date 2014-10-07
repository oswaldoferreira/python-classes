from transaction import Transaction
from should_dsl import should, should_not
from ludibrio import Stub
from datetime import datetime
import unittest

class TestTransaction(unittest.TestCase):
  def setUp(self):
    Transaction.objects = {}

    self.transaction = Transaction(datetime(2014, 10, 4, 20, 0), 33.50)

  def test_initial_attributes(self):
    self.transaction.date        |should| equal_to(datetime(2014, 10, 4, 20, 0))
    self.transaction.month       |should| equal_to(10)
    self.transaction.value       |should| equal_to(33.50)
    self.transaction.id          |should| equal_to(1)

  def test_persistence(self):
    Transaction.objects |should| equal_to({ 1: self.transaction })

  def test_associate_credit_card(self):
    with Stub() as credit_card: credit_card.id >> 1

    self.transaction.associate_credit_card(credit_card)

    self.transaction.credit_card_id |should| equal_to(credit_card.id)

  def test_associate_seller(self):
    with Stub() as seller: seller.id >> 1

    self.transaction.associate_seller(seller)

    self.transaction.seller_id |should| equal_to(seller.id)

if __name__ == '__main__':
  unittest.main()