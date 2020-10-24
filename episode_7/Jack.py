import time as t
s = t.time()

set = [a**b for a in range(2,101) for b in range(2,101)] ; set.sort()
for i in set:
    if set.count(i)>1:
        for j in range(set.count(i)-1): set.remove(i)
print(len(set))

e = t.time()
print(e-s)
