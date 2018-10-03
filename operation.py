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
