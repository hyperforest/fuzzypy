import fuzzypy as fzp

def miu_R1(x, y):
	return (y - x - 6) / 5

def miu_R2(x, y):
	return (x - y) / 12
	
def t(a, b):
	return fzp.t(a, b, 'algebraic')

U = fzp.npa([1, 2, 3, 4])
V = fzp.npa([10, 11, 12])

R1 = fzp.relation(U, V, miu_R1)
R2 = fzp.relation(V, U, miu_R2)

R1 = fzp.as_matrix(R1, 4, 3)
R2 = fzp.as_matrix(R2, 3, 4)

R1oR2 = fzp.composition(R1, R2, t)

print(R1oR2)