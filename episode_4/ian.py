def num_circle(n): # returns list of all roations of n
    circle = []
    for i in range(len(str(n))): 
        circle.append(n);
        n = int(str(n)[1:] + str(n)[0]) # shifts each digit left
    return circle    

def sieve_of_Eratosthenes(n): # returns all primes under n
    A = [True]*n
    for i in range(2,int(n**(0.5))+1): 
        if A[i] == True:
            j = i**2
            while j < n:
                A[j] = False
                j += i                  
    return [i for i in range(len(A)) if A[i] == True][2:]

def circular_check(p): # returns True if prime p is a circular prime, False otherwise
    if p == 2 or p == 5: return True # only circular primes with digits 2 or 5
    else:
        str_p = str(p)
        no = ['0','2','4','5','6','8']
        no_chars = [1 for n in no if n in str_p]
        if len(no_chars) == 0: # primes with digits in 'no' cannot be circular
            circ_p = num_circle(p)
            check = [1 for i in circ_p if i not in primes]      
            if len(check) == 0: return True # check if each circulation of prime is prime
            else: return False
                
primes = sieve_of_Eratosthenes(1000000) # all primes under 1,000,000
circular_primes = [1 for p in primes if circular_check(p) == True] # number of circular primes under 1,000,000
print(f'Ans = {len(circular_primes)}')
