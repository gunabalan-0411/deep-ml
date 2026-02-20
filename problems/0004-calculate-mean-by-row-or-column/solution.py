import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	np_matrix = np.array(matrix)
	if mode == 'column':
		np_matrix  = np_matrix.T
	means = []
	for item in np_matrix:
		means.append(item.mean())
	return means