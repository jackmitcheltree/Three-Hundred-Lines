n = 1000000
primes = [True if i > 1 else False for i in range(n+1)] 
for p in range(2, n+1):
  if p*p <= n and primes[p] is True: 
    for i in range(p * p, n+1, p): primes[i] = False
for p in range(2, n+1):
  if primes[p] is True:
    _i, s = [p], str(p)
    for i in range(len(s)-1):
      s = s[1:] + s[0]
      if s[0] != '0': _i.append(int(s))
    if all([primes[i] for i in _i]) is False:
      for i in _i: primes[i] = False
print(sum(primes))
