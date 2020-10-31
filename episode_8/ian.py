import time
start = time.time()

#
#-
#~ Find the value of n <= m for which n/phi(n) is maximimized ~#
def sieve_of_Eratosthenes(n): # returns list of primes less than n
        A = [True]*n
        for i in range(2,int(n**(0.5))+1): 
            if A[i] == True:
                j = i**2
                while j < n:
                    A[j] = False
                    j += i                  
        return [i for i in range(len(A)) if A[i] == True][2:]

def max_calc(m):
    primes = sieve_of_Eratosthenes(m)
    
    n = 1
    while True:
        _n = 1
        for i in primes[0:n]:
            _n *= i
            
        _n_1 = 1
        for i in primes[0:(n+1)]:
            _n_1 *= i
            
        if (_n <= m) and (_n_1 > m):
            print(f'Ans = {_n}')
            break
        else:
            n += 1
            
max_calc(m:=1000000)
#-
#

end = time.time()
print(end-start)
