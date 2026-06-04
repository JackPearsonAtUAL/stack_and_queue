"""
check.py — run this to test your exercises.py answers.

Usage:
    python check.py
"""

import math, sys

try:
    import exercises as ex
except Exception as e:
    print(f"\n  Could not import exercises.py: {e}\n")
    sys.exit(1)

passed = 0
failed = 0

def check(num, label, got, expected=None, custom=None):
    global passed, failed
    try:
        if got is None:
            raise AssertionError("still None — did you fill in the TODO?")
        if custom:
            custom(got)
        else:
            assert got == expected, f"got {got!r}, expected {expected!r}"
        print(f"\033[32m  ✓\033[0m  {num:02d} · {label}")
        passed += 1
    except AssertionError as e:
        print(f"\033[31m  ✗\033[0m  {num:02d} · {label}\n       {e}")
        failed += 1

def chk04(v):
    if len(v) != 2 or abs(v[0] - (-1.0)) >= 1e-9 or abs(v[1] - 0.0) >= 1e-9:
        raise AssertionError(f"got {v}, expected [-1.0, 0.0]")

def chk06(C):
    expected = [[19, 22], [43, 50]]
    if C != expected:
        raise AssertionError(f"got {C!r}, expected {expected!r}")

print("\nLinear Algebra 2 — checking your answers\n")

check( 1, "Matrix repr     — M[1][2]",                   ex.elem,       expected=6)
check( 2, "Mat-vec mul     — [[2,0],[1,3]] @ [4,2]",     ex.Mv,         expected=[8, 10])
check( 3, "Translation     — [3,1] + (tx=5, ty=-2)",     ex.translated, expected=[8, -1])
check( 4, "Rotation        — rotate90([0,1])",            ex.rotated,    custom=chk04)
check( 5, "Scaling         — scale(2,3) @ [3,2]",        ex.scaled,     expected=[6, 6])
check( 6, "Matrix mul      — A @ B",                      ex.C,          custom=chk06)

total = passed + failed
print(f"\n  {passed}/{total} passed", end="")
if failed == 0:
    print("  \033[32m— all done!\033[0m\n")
else:
    print(f"  \033[33m— {failed} to go\033[0m\n")
