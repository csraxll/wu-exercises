class LadderCalculator:
	"""Utility class to make calculations about ladders"""

	@classmethod
	def calculate(cls, n):
		"""Returns all possible combinations when climbing a ladder making 1 or 2 steps at time.

	    Parameters:
	        n (int):The number of steps that the ladder has.

	    Returns:
	        x(int):The number of possible combinations.
		"""
		if not float(n).is_integer() or n < 1:
			raise ValueError('Just positive integer numbers are supported')
		return cls.__calculate_impl(n)

	@classmethod
	def __calculate_impl(cls, n):
		if n < 0:
			return 0
		if n == 0:
			return 1
		else:
			return cls.__calculate_impl(n - 2) + cls.__calculate_impl(n - 1)