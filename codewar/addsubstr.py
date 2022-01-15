s, t, n = input(), input(), int(input())
if len(s) > len(t): a, d, o = len(s)-len(t), 0, len(t)
if len(t) > len(s): d, a, o = len(t)-len(s), 0, len(s)
for c1, c2 in zip(s[:o], t[:o]):
    if c1 != c2: a += 1; d += 1
print('yes' if n == a+d else 'no')
