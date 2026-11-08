# Lemma B (a prime-generating polynomial)

**Claim (computed, 0 <= n <= 39).** For every integer n with 0 <= n <= 39, the number
n^2 + n + 41 is prime. The claim for all n >= 1 is false: at n = 40, n^2 + n + 41 = 41^2.
(n = 0 is included here, unlike kb/conventions.md, where n is positive; f(0) = 41.)

**Evidence.** scripts/check_lemma_b.py tests every n in 0..39 by exact trial division and,
as a negative control, checks that n = 40 gives the composite number 1681 = 41^2. No proof
for all n is claimed.
