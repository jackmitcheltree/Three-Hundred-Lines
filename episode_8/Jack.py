import time as t
start = t.time()


import math ; M = 1000001 ; n = list(range(2,M)) ; m = list(map(lambda x: 1 + len( [i for i in range(2,x) if math.gcd(x,i) == 1]) , n )) ; l = list( map( lambda x,y: x/y, n, m ) ) ; o = list(map( lambda x,y: (x,y), n, l )) ; print(max(  [x for (x,y) in o if y == max( [k for (j,k) in o] )]  ))


end = t.time()
print(end - start)
