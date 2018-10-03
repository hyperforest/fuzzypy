import numpy as np
import operation as op

def set_dec(x, n):
	s = "%.{}f".format(n)
	return float(s % x)

def relation(fuzzy_set1, fuzzy_set2, miu):
	R = []

	for x in fuzzy_set1:
		for y in fuzzy_set2:
			R.append(set_dec(miu(x, y), 2))

	return op.npa(R)

def as_matrix(relation, row, col):
	return relation.reshape((row, col))

def composition(relation_matrix1, relation_matrix2, t):
	r1, c1 = relation_matrix1.shape
	r2, c2 = relation_matrix2.shape

	if c1 != r2:
		return None

	res = np.zeros((r1, c2))

	for i in range(r1):
		for j in range(c2):
			res[i][j] = (t(relation_matrix1[i], relation_matrix2[:, j])).max()

	return res
