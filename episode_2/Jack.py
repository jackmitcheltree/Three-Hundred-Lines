#Find the sum of the digits in the number 100!
import time
import math

start = time.time()

def F(n):
    F = str(math.prod(list(range(1,n+1))))
    S = 0
    for x in range(len(F)):
        S = int(F[x]) + S
    return S
print(F(100))

end = time.time()
print(end-start)
