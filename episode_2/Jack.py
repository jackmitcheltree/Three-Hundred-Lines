#Find the sum of the digits in the number 100!
import time
import math

start = time.time()

def F(n):
    F = str(math.prod(list(range(1,n+1))))
    S = sum([int(F[x]) for x in range(len(F))])
    return S
print(F(100))

end = time.time()
print(end-start)
