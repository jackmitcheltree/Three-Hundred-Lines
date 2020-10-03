import time
start = time.time()



n = 10000
primes = [True if i > 1 else False for i in range(n+1)] 
for i in range(2, n+1):
  if i >= 9 and i%2 == 1 and primes[i] is not True:
    a = [False, i]
    for j in range(3, i):
      if primes[j] is True and ((i-j)/2)^.5.is_integer():
        a = [True, i]
        break
  if i >= 9 and a[0] is False: break
  if i*i <= n and primes[i] is True: 
    for p in range(i*i, n+1, i): primes[p] = False
print (a)




end = time.time()
print(end-start)
