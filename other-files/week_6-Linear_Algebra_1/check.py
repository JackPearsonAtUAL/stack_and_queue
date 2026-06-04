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

def chk01(v):
    if abs(v - 5.0) >= 1e-9:
        raise AssertionError(f"got {v:.6f}, expected 5.0")

def chk06(v):
    length = math.sqrt(sum(x**2 for x in v))
    if abs(length - 1.0) >= 1e-9:
        raise AssertionError(f"|unit| = {length:.9f}, expected 1.0")

def chk07(t):
    v, p = [1, 2], [3, 6]
    if not all(abs(t * v[i] - p[i]) < 1e-9 for i in range(2)):
        raise AssertionError(f"t={t} gives t*[1,2]={[t*x for x in v]}, expected [3,6]")

def chk10(proj):
    if len(proj) != 2 or abs(proj[0]-4.0) >= 1e-9 or abs(proj[1]-0.0) >= 1e-9:
        raise AssertionError(f"got {proj}, expected [4.0, 0.0]")

print("\nLinear Algebra 1 — checking your answers\n")

check( 1, "Vectors          — magnitude of [3,4,0]",      ex.magnitude,    custom=chk01)
check( 2, "Addition         — [1,2,3] + [4,5,6]",         ex.result,       expected=[5,7,9])
check( 3, "Scalar mul       — -2 * [3,-1,4]",             ex.scaled,       expected=[-6,2,-8])
check( 4, "Dot product      — [1,2,3]·[4,-5,6]",          ex.dot,          expected=12)
check( 5, "Cross product    — [1,0,0]×[0,1,0]",           ex.cross,        expected=[0,0,1])
check( 6, "Normalisation    — unit([0,3,4]) has |v|=1",   ex.unit,         custom=chk06)
check( 7, "Span             — t such that t*[1,2]=[3,6]", ex.t,            custom=chk07)
check( 8, "Data vectors     — most similar to Alice",      ex.most_similar, expected='Charlie')
check( 9, "Linear transform — rotate90([1,0])",            ex.transformed,  expected=[0,1])
check(10, "Projection       — proj [4,3] onto [1,0]",      ex.proj,         custom=chk10)

total = passed + failed
print(f"\n  {passed}/{total} passed", end="")
if failed == 0:
    print("  \033[32m— all done!\033[0m\n")
else:
    print(f"  \033[33m— {failed} to go\033[0m\n")
