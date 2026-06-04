"""
Linear Algebra 1 — Exercises
==============================
Fill in each TODO. When you're ready, run:

    python3 week_6-Linear_Algebra_1/check.py

No numpy — pure Python and the math module only.
"""

import math

# ─────────────────────────────────────────────────────────────────────────────
# 01 · VECTORS
# A vector is an ordered list of numbers encoding direction and magnitude.
# The magnitude (length) is the square root of the sum of squared components.
#
# Question: what is the magnitude of v = [3, 4, 0] ?
# ─────────────────────────────────────────────────────────────────────────────

v = [3, 4, 0]
magnitude = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)  # TODO: a single number
# ─────────────────────────────────────────────────────────────────────────────
# 02 · VECTOR ADDITION
# Add two vectors by adding each component independently.
#
# Question: what is u + v where u = [1, 2, 3] and v = [4, 5, 6] ?
# ─────────────────────────────────────────────────────────────────────────────

u, v = [1, 2, 3], [4, 5, 6]
result = [u[0] + v[0], u[1] + v[1], u[2] + v[2]]  # TODO: a list [?, ?, ?]

# ─────────────────────────────────────────────────────────────────────────────
# 03 · SCALAR MULTIPLICATION
# Multiply every component of a vector by a single number.
#
# Question: what is -2 * v where v = [3, -1, 4] ?
# ─────────────────────────────────────────────────────────────────────────────

v = [3, -1, 4]
for i in range(len(v)): 
    v[i] = v[i] * -2
scaled =  v # TODO: a list [?, ?, ?]

# ─────────────────────────────────────────────────────────────────────────────
# 04 · DOT PRODUCT
# Multiply matching components, then sum everything. Result is a scalar.
# Formula: a·b = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
#
# Question: what is the dot product of a = [1, 2, 3] and b = [4, -5, 6] ?
# ─────────────────────────────────────────────────────────────────────────────

a, b = [1, 2, 3], [4, -5, 6]
c = []
d = 0
if len(a) == len(b):
    for i in range(len(a)):
        c.append(a[i]*b[i])
d = sum(c)
dot = d  # TODO: a single number

# ─────────────────────────────────────────────────────────────────────────────
# 05 · CROSS PRODUCT
# Defined in 3D only. Produces a vector perpendicular to both inputs.
# Formula: w = [a[1]*b[2] - a[2]*b[1],
#               a[2]*b[0] - a[0]*b[2],
#               a[0]*b[1] - a[1]*b[0]]
#
# Question: what is u x v where u = [1, 0, 0] and v = [0, 1, 0] ?
# ─────────────────────────────────────────────────────────────────────────────

u, v = [1, 0, 0], [0, 1, 0]
w = [u[1]*v[2] - u[2]*v[1],
    u[2]*v[0] - u[0]*v[2],
    u[0]*v[1] - u[1]*v[0]]

cross = w  # TODO: a list [?, ?, ?]

# ─────────────────────────────────────────────────────────────────────────────
# 06 · UNIT VECTORS / NORMALISATION
# Divide every component by the vector's magnitude to get length = 1.
# Formula: v_hat = v / |v|
#
# Question: normalise v = [0, 3, 4]. What is the unit vector?
# ─────────────────────────────────────────────────────────────────────────────

v = [0, 3, 4]
length = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
unit = [v[0] / length, v[1] / length, v[2] / length]  # TODO: a list of three floats

# ─────────────────────────────────────────────────────────────────────────────
# 07 · SPAN
# The span of a vector v is every point reachable as t*v for any scalar t.
#
# Question: find the scalar t such that t * [1, 2] == [3, 6].
# ─────────────────────────────────────────────────────────────────────────────

v = [1, 2]
p = [3, 6]
t = p[0]/v[0] # TODO: a single number

# ─────────────────────────────────────────────────────────────────────────────
# 08 · VECTOR REPRESENTATION OF DATA
# Data points encoded as feature vectors — dot product measures similarity.
# Students described by [study_hrs, sleep_hrs, exercise_hrs].
#
# Question: which student has the highest dot-product similarity with Alice?
# ─────────────────────────────────────────────────────────────────────────────

students = {
    'Alice':   [8, 7, 5],
    'Bob':     [3, 5, 2],
    'Charlie': [7, 8, 6],
    'Diana':   [2, 4, 1],
}

most_similar = 'Charlie'  # TODO: a name string


# ─────────────────────────────────────────────────────────────────────────────
# 09 · LINEAR TRANSFORMATION
# Apply matrix M to vector v: each output row is the dot product of that
# matrix row with v.
#
# Question: apply the 90 degree anticlockwise rotation matrix to v = [1, 0].
# M = [[0, -1],
#      [1,  0]]
# ─────────────────────────────────────────────────────────────────────────────

M = [[0, -1],
     [1,  0]]
v = [1, 0]
transformed = [M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1]] # TODO: a list [?, ?]

# ─────────────────────────────────────────────────────────────────────────────
# 10 · PROJECTION
# Project u onto v: find the component of u that lies along v.
# Formula: proj = (u.v / v.v) * v
#
# Question: project u = [4, 3] onto v = [1, 0].
# ─────────────────────────────────────────────────────────────────────────────

u = [4, 3]
v = [1, 0]
proj = [4, 0]  # TODO: a list [?, ?]
