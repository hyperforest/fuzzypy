import numpy as np

def npa(x):
	return np.array(x)

def complement(x, mode = 'basic', lmbd = 0, w = 1):
	f = {
		'basic' : 1 - x,
		'sugeno' : (1 - x) / (1 + lmbd * x),
		'yager' : (1 - x ** w) ** (1 / w)
	}

	return f[mode]

def s(a, b, mode = 'basic', w = 1):
	f = {
		'basic' : np.minimum(a, b),
		'yager' : np.minimum(1, (a ** w + b ** w) ** (1 / w)),
		'algebraic' : a + b - a * b,
		'einstein' : (a + b) / (1 + a * b)
	}

	return f[mode]

def t(a, b, mode = 'basic', w = 1):
	f = {
		'basic' : np.minimum(a, b),
		'yager' : 1 - np.minimum(1, ((1 - a) ** w + (1 - b) ** w) ** (1 / w)),
		'algebraic' : a * b,
		'einstein' : (a * b) / (2 - (a + b - a * b))
	}

	return f[mode]

def set_dec(x, n):
	s = "%.{}f".format(n)
	return float(s % x)

# From now is code for fuzzy relation

def relation(fuzzy_set1, fuzzy_set2, miu, dec = 2):
	R = []

	for x in fuzzy_set1:
		for y in fuzzy_set2:
			R.append(set_dec(miu(x, y), dec))

	return npa(R)

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
