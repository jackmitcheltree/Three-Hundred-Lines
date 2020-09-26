import time
start = time.time()

A = [True]*(n:=5778)
for i in range(2,int(n**(0.5))+1): 
    if A[i] == True:
        j = i**2
        while j < n:
            A[j] = False
            j += i    
no_gos = [i for i in range(len(A)) if A[i] == True][2:] + [p+(2*(s)**2) for s in range(1,int(n**0.5)+2) for p in [i for i in range(len(A)) if A[i] == True][2:]] + [i for i in range(2,n+1) if i%2==0]
print(f'Ans = {[i for i in range(9,n+1) if i not in no_gos][0]}')

end = time.time()
print(end - start)
