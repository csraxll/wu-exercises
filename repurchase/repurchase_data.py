import json
import math
from datetime import datetime, timedelta

class Purchase:
	"""Stores information about a client's purchase"""

	def __init__(self, id: int, date: datetime):
		self.id = id
		self.date = date

	@staticmethod
	def decode(purchase_map):
		return Purchase(purchase_map['product_id'], datetime.strptime(purchase_map['purchase_date'], '%Y-%m-%dT%H:%M:%S'))

class Client:
	"""Stores information about a client, including previous purchases and future ones"""

	def __init__(self, id, purchases = []):
		self.id = id
		self.previous_purchases = purchases
		self.estimated_repurchases = []

	@staticmethod
	def decode(client_map):
		if not isinstance(client_map['id'], int):
			raise ValueError("Id is not of type int")
		purchases = [Purchase.decode(p) for p in client_map['purchases']]
		return Client(client_map['id'], purchases)

	def estimate_repurchases(self):
		"""Executes the calculation possible future purchases based on the previous purchases stored in the previous_purchases attribute

		The result of this calculation is stored as a list of purchases in the attribute estimated_repuchases
		"""
		products_ids = [p.id for p in self.previous_purchases]
		non_unique_purchases = [p for p in self.previous_purchases if products_ids.count(p.id) > 1]
		sorted_non_unique_purchases = sorted(non_unique_purchases, key=lambda p: (p.id, p.date))
		self.estimated_repurchases = []
		index = 0
		while index < len(sorted_non_unique_purchases):
			current_id = sorted_non_unique_purchases[index].id
			next_id = current_id
			times_bought = 0
			days_delta = timedelta(days = 0)
			while index < len(sorted_non_unique_purchases) and current_id == next_id:
				if times_bought > 0:
					delta = sorted_non_unique_purchases[index].date - sorted_non_unique_purchases[index - 1].date
					days_delta = days_delta + delta
				times_bought +=1
				index += 1
				if index < len(sorted_non_unique_purchases):
					next_id = sorted_non_unique_purchases[index].id
			repurchase_average_delta = math.ceil(days_delta.days/(times_bought - 1))
			estimated_repurchase_date = sorted_non_unique_purchases[index - 1].date + timedelta(days = repurchase_average_delta)
			self.estimated_repurchases.append(Purchase(current_id, estimated_repurchase_date))

	def	print_purchases(self):
		for p in self.estimated_repurchases:
			print('{0} - {1}'.format(p.id, p.date))