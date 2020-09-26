import time as t
S = t.time()

def Sieve_Erato(n):
    primes = []
    check = [True for n in range(0, n+1)]
    for i in range(2, n+1):
        if check[i] == True:
            primes.append(i)
            for j in range((i)**2,n+1,(i)):
                try: check[j] = False
                except: pass
    return primes

conjecture = True
i,j = 1,1
while conjecture == True:
    satisfies = False
    composite = 4 * i * j + 2 * (i + j) + 1
    twice_sqr = [2*(x**2) for x in range(1,composite+1) if 2*(x**2) < composite]
    n = composite - twice_sqr[0]
    primes = Sieve_Erato(n)
    for p in primes:
        for sqr in twice_sqr:
            if p + sqr == composite:
                satisfies = True
    if j == i:
        i += 1
        j = 1
    else:
        j += 1

    if satisfies == False:
        print(composite)
        conjecture = False

E = t.time()
print(E-S)
