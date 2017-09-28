def countDs(n):
	"""
	Number of Diagonals of an n-sided polygon.
	"""
	return n * (n - 3) / 2 if n > 2 else 0