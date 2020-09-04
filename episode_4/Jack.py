import time
S = time.time()

def primesL_than(n):
    primes = []
    check = [True for n in range(0, n+1)]
    for i in range(2, n+1):
        if check[i] == True:
            primes.append(str(i))
            for j in range((i)**2,n+1,(i)):
                try: check[j] = False
                except: pass
    return primes
def Num_CprimesL_than(n):
    delete = ['0','2','4','6','8','5']
    primes = [x for x in primesL_than(n) if not any(y in delete for y in x)]
    primes.extend(['2','5'])
    circular_primes = []
    for prime in primes:
        rotations = []
        for index in prime:
            rotations.append(prime)
            prime = prime[-1] + prime[:-1]
        circular = True
        for number in rotations:
            if not number in primes:
                circular = False
        if circular == True:
            for number in rotations:
                if int(number) in circular_primes: pass
                else: circular_primes.append(int(number))
    return print(len(circular_primes))
Num_CprimesL_than(1000000)

E = time.time()
print(E-S)
