import math

def s01(v):
    return math.sqrt(sum(x**2 for x in v))

def s02(u, v):
    return [u[i] + v[i] for i in range(len(u))]

def s03(scalar, v):
    return [scalar * x for x in v]

def s04(a, b):
    return sum(a[i] * b[i] for i in range(len(a)))

def s05(u, v):
    return [
        u[1]*v[2] - u[2]*v[1],
        u[2]*v[0] - u[0]*v[2],
        u[0]*v[1] - u[1]*v[0],
    ]

def s06(v):
    mag = math.sqrt(sum(x**2 for x in v))
    return [x / mag for x in v]

def s07(v, p):
    return p[0] / v[0]

def s08(students):
    def dot(a, b): return sum(a[i]*b[i] for i in range(len(a)))
    alice = students['Alice']
    scores = {n: dot(alice, vec) for n, vec in students.items() if n != 'Alice'}
    return max(scores, key=scores.get)

def s09(M, v):
    return [sum(M[r][c] * v[c] for c in range(len(v))) for r in range(len(M))]

def s10(u, v):
    scale = sum(u[i]*v[i] for i in range(len(u))) / sum(x**2 for x in v)
    return [scale * x for x in v]
