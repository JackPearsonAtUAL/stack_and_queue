import math

def s01(M):
    return M[1][2]

def s02(M, v):
    return [sum(M[r][c] * v[c] for c in range(len(v))) for r in range(len(M))]

def s03(point, tx, ty):
    return [point[0] + tx, point[1] + ty]

def s04(v, theta):
    c, s = math.cos(theta), math.sin(theta)
    return [c * v[0] - s * v[1], s * v[0] + c * v[1]]

def s05(v, sx, sy):
    return [sx * v[0], sy * v[1]]

def s06(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
