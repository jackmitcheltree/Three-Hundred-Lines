# Find the sum of all multiples of 5 and 3 below 1000
#Returns the sum of all the integers between l and L that are multiples
# of n and m.

def sum_ints(n,m,l,L):
    S = sum([x for x in range(l,L) if x%n==0 or x%m==0])
    return S

print (sum_ints(3,5,0,1000))
