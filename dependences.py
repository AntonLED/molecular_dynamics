k_b = 1.38064852e-23 
N_a = 6.02214086e23

EPS = 120.0 * k_b * N_a
SIGM = 3.38

def U(r):
    return 4 * EPS * ((SIGM/r)**12 - (SIGM/r)**6)

def F(r):
    return 4 * EPS * (-1 * SIGM**12/r**13 + SIGM**6/r**7)
