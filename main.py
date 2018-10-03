import operation as op
import relation as rel

def miu_R1(x, y):
	return (y - x - 6) / 5

def miu_R2(x, y):
	return (x - y) / 12
	
def t(a, b):
	return op.t(a, b, 'algebraic')

U = op.npa([1, 2, 3, 4])
V = op.npa([10, 11, 12])

R1 = rel.relation(U, V, miu_R1)
R2 = rel.relation(V, U, miu_R2)

R1 = rel.as_matrix(R1, 4, 3)
R2 = rel.as_matrix(R2, 3, 4)

R1oR2 = rel.composition(R1, R2, t)

print(R1oR2)