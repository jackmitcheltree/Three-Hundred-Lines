import time
start = time.time()



n = 1000000; m = 1; primes = [False]*2 + [True]*19
for i in range(2, n+1):
  if primes[i] is True and i*i <= n:
    m *= i
    for j in range(i*i, 19, i): primes[j] = False
  if m > n: 
    m = m/i; print(m); break



end = time.time()
print(end-start)




