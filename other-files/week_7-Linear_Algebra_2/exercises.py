"""
Linear Algebra 2 — Exercises
==============================
Fill in each TODO. When you're ready, run:

    python3 week_7-Linear_Algebra_2/check.py

No numpy — pure Python and the math module only.
"""

import math

# ─────────────────────────────────────────────────────────────────────────────
# 01 · MATRIX REPRESENTATION
# A matrix is a rectangular grid of numbers stored as a list of rows.
# Element access: M[row][col]  (0-indexed)
#
# Question: what is the element at row 1, column 2 of M?
# ─────────────────────────────────────────────────────────────────────────────

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

elem = 6  # TODO: a single integer


# ─────────────────────────────────────────────────────────────────────────────
# 02 · MATRIX-VECTOR MULTIPLICATION
# Each row of M is dotted with v to produce one output component.
# Formula: (Mv)[i] = sum(M[i][j] * v[j] for j in range(n))
#
# Question: what is Mv where M = [[2, 0], [1, 3]] and v = [4, 2]?
# ─────────────────────────────────────────────────────────────────────────────

M = [[2, 0],
     [1, 3]]
v = [4, 2]

Mv = [8, 10]  # TODO: a list [?, ?]


# ─────────────────────────────────────────────────────────────────────────────
# 03 · TRANSLATION (homogeneous coordinates)
# Encode a 2D point as [x, y, 1] and multiply by the 3×3 matrix:
#   T = [[1, 0, tx],
#        [0, 1, ty],
#        [0, 0,  1]]
# The x, y components of the result give the translated point.
#
# Question: translate [3, 1] by tx = 5, ty = −2.
# ─────────────────────────────────────────────────────────────────────────────

point  = [3, 1]
tx, ty = 5, -2

translated = [8, -1]  # TODO: a list [?, ?]  (just the x, y result)


# ─────────────────────────────────────────────────────────────────────────────
# 04 · ROTATION
# Counter-clockwise rotation by angle θ:
#   R = [[cos θ, −sin θ],
#        [sin θ,  cos θ]]
#
# Question: rotate v = [0, 1] by 90° counter-clockwise.
#           (cos 90° = 0, sin 90° = 1)
# ─────────────────────────────────────────────────────────────────────────────

#R = [[0, −1],
#     [1,  0]]
v     = [0, 1]
theta = math.pi / 2  # 90 degrees

rotated = [-1, 0] # TODO: a list [?, ?]


# ─────────────────────────────────────────────────────────────────────────────
# 05 · SCALING
# Scale matrix: S = [[sx, 0], [0, sy]]
# Multiplying by S stretches or compresses each axis independently.
#
# Question: apply sx = 2, sy = 3 to v = [3, 2].
# ─────────────────────────────────────────────────────────────────────────────

v      = [3, 2]
sx, sy = 2, 3

scaled = [6, 6]  # TODO: a list [?, ?]


# ─────────────────────────────────────────────────────────────────────────────
# 06 · MATRIX MULTIPLICATION (combining transformations)
# Composing two linear maps A and B: C = A @ B
# C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
#
# Question: what is C = A @ B?
#   A = [[1, 2],    B = [[5, 6],
#        [3, 4]]         [7, 8]]
# ─────────────────────────────────────────────────────────────────────────────

A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]

C = [[19, 22],[43, 50]]  # TODO: a 2×2 list of lists  [[?, ?], [?, ?]]
