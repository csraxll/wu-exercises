import unittest
from ladder.util import LadderCalculator

class TestLadderCalculator(unittest.TestCase):

	def test_calculate_with_positive_integer(self):
		self.assertEqual(LadderCalculator.calculate(1), 1)
		self.assertEqual(LadderCalculator.calculate(2), 2)
		self.assertEqual(LadderCalculator.calculate(3), 3)
		self.assertEqual(LadderCalculator.calculate(4), 5)
		self.assertEqual(LadderCalculator.calculate(5), 8)

	def test_calculate_with_zero(self):
		with self.assertRaises(ValueError):
			LadderCalculator.calculate(0)
            
	def test_calculate_with_negative_integer(self):
		with self.assertRaises(ValueError):
			LadderCalculator.calculate(-1)

	def test_calculate_with_negative_non_integer(self):
		with self.assertRaises(ValueError):
			LadderCalculator.calculate(-5.5)

	def test_calculate_with_positive_non_integer(self):
		with self.assertRaises(ValueError):
			LadderCalculator.calculate(5.5)

if __name__ == '__main__':
	unittest.main()