import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	real_matrix = np.array(matrix)
	result = real_matrix * scalar
	return result
	pass