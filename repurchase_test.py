import unittest
import math
from datetime import datetime, timedelta
from repurchase.repurchase_data import Client, Purchase

class TestRepurchaseEstimation(unittest.TestCase):

	def setUp(self):
		self.sample_date = datetime(2020, 8, 14)

	def test_when_not_exists_previous_purchases_estimation_gives_empty_list(self):
		c = Client(0, [])
		c.estimate_repurchases()
		# Empty lists/dicts evaluate to False
		self.assertFalse(c.estimated_repurchases)

	def test_when_not_exists_repeated_purchases_estimation_gives_empty_list(self):
		c = Client(0, [Purchase('0', datetime.now()), Purchase('1', datetime.now())])
		c.estimate_repurchases()
		# Empty lists/dicts evaluate to False
		self.assertFalse(c.estimated_repurchases)

	def test_when_exists_repeated_purchases_estimation_gives_correct_result(self):
		delta = timedelta(days = 10)
		c = Client(0, [Purchase(0, self.sample_date - delta), \
						Purchase(0, self.sample_date)])
		c.estimate_repurchases()
		self.assertEqual(datetime(2020, 8, 14) + delta, c.estimated_repurchases[0].date)

	def test_when_exists_more_than_two_purchases_estimation_gives_correct_result(self):
		delta1 = timedelta(days = 30)
		delta2 = timedelta(days = 10)
		c = Client(0, [Purchase(0, self.sample_date - delta1), \
						Purchase(0, self.sample_date - delta2), \
						Purchase(0, self.sample_date)])
		c.estimate_repurchases()
		average_delta = timedelta(days = math.ceil(delta1.days/2))
		self.assertEqual(datetime(2020, 8, 14) + average_delta, c.estimated_repurchases[0].date)

	def test_when_purchases_are_unordered_estimation_gives_correct_result(self):
		delta1 = timedelta(days = 30)
		delta2 = timedelta(days = 10)
		c = Client(0, [Purchase(0, self.sample_date), \
						Purchase(0, self.sample_date - delta1), \
						Purchase(0, self.sample_date - delta2)])
		c.estimate_repurchases()
		average_delta = timedelta(days = math.ceil(delta1.days/2))
		self.assertEqual(datetime(2020, 8, 14) + average_delta, c.estimated_repurchases[0].date)

	def test_when_exists_multiple_repeated_purchases_estimation_gives_correct_result(self):
		delta1 = timedelta(days = 30)
		delta2 = timedelta(days = 10)
		c = Client(0, [Purchase(0, self.sample_date), \
						Purchase(0, self.sample_date - delta1), \
						Purchase(1, self.sample_date), \
						Purchase(1, self.sample_date - delta2)])
		c.estimate_repurchases()
		self.assertEqual(self.sample_date + delta1, c.estimated_repurchases[0].date)
		self.assertEqual(self.sample_date + delta2, c.estimated_repurchases[1].date)

class TestJsonDecoding(unittest.TestCase):

	def test_when_client_id_is_not_integer_exception_is_raised(self):
		data = { 'id': 'asd', 'purchases' : []}
		with self.assertRaises(ValueError):
			Client.decode(data)

	def test_when_client_id_is_missing_exception_is_raised(self):
		data = { 'purchases' : []}
		with self.assertRaises(KeyError):
			Client.decode(data)

	def test_when_client_purchases_is_missing_exception_is_raised(self):
		data = { 'id': 0}
		with self.assertRaises(KeyError):
			Client.decode(data)

	def test_when_product_id_is_missing_exception_is_raised(self):
		data = { 'purchase_date': '2017-05-21T05:13:36'}
		with self.assertRaises(KeyError):
			Purchase.decode(data)

	def test_when_purchase_date_is_missing_exception_is_raised(self):
		data = { 'product_id': 0 }
		with self.assertRaises(KeyError):
			Purchase.decode(data)

if __name__ == '__main__':
	unittest.main()