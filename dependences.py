EPS = 1
SIGM = 2

def U(r):
    return 4 * EPS * ((SIGM/r)**12 - (SIGM/r)**6)

def F(r):
    return 4 * EPS * (-1 * SIGM**12/r**13 + SIGM**6/r**7)
