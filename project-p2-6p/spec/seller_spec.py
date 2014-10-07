from seller import Seller
from should_dsl import should, should_not
from transaction import Transaction
from ludibrio import Stub, Mock
from datetime import datetime
import unittest

class TestSeller(unittest.TestCase):
  def setUp(self):
    self.seller = Seller('Oswaldo das Covi', '1234567')

  def test_initial_attributes(self):
    self.seller.name      |should| equal_to('Oswaldo das Covi')
    self.seller.document  |should| equal_to('1234567')
    self.seller.id        |should| equal_to(1)

  def test_transactions_list(self):
    with Stub() as first_transaction:
      first_transaction.seller_id >> 1
      first_transaction.month >> 10

    with Stub() as second_transaction:
      second_transaction.seller_id >> 1
      second_transaction.month >> 10

    with Stub() as third_transaction:
      third_transaction.seller_id >> 1
      third_transaction.month >> 11

    Transaction.objects = { 1: first_transaction,
                            2: second_transaction,
                            3: third_transaction }

    # October's transactions
    Seller.transactions_list(10) |should| equal_to(
      [first_transaction, second_transaction]
    )

if __name__ == '__main__':
  unittest.main()