"""Lemma B: f(n) = n^2 + n + 41 is prime for every integer 0 <= n <= 39, and not for n = 40.

Exact integer arithmetic, trial division. The checks are explicit `if ... raise SystemExit`, not
`assert`, so that `python -O` cannot remove them. The second check is a negative control: it makes
sure that is_prime can answer "composite" on a value of f.
"""


def is_prime(m: int) -> bool:
    if m < 2:
        return False
    d = 2
    while d * d <= m:
        if m % d == 0:
            return False
        d += 1
    return True


def f(n: int) -> int:
    return n * n + n + 41


if not all(is_prime(f(n)) for n in range(0, 40)):
    raise SystemExit("FAIL: some f(n), 0 <= n <= 39, is not prime")
if not (f(40) == 41 * 41 and not is_prime(f(40))):
    raise SystemExit("FAIL: negative control: f(40) must be 41^2 and composite")
print("ok: f(n) is prime for n = 0..39; f(40) = 1681 = 41^2 is not")
