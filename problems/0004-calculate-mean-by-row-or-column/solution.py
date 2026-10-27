import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	real_matrix = np.array(matrix)
	if mode == 'column':
		means = np.mean(real_matrix,axis=0)
	elif mode == 'row':
		means = np.mean(real_matrix,axis=1)
	else:
		means = 0
	return means
