import time
start = time.time()



import math as m
n = 10000
primes = [True if i > 1 else False for i in range(n+1)] 
for p in range(2, n+1):
  if p >= 9 and p%2 == 1 and primes[p] is not True:
    a = [False, p]
    for j in range(3, p):
      if primes[j] is True and m.sqrt((p-j)/2).is_integer():
        a = [True, p]
        break
  if p >= 9 and a[0] is False: break
  if p*p <= n and primes[p] is True: 
    for i in range(p * p, n+1, p): primes[i] = False
print (a)




end = time.time()
print(end-start)