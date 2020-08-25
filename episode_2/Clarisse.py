f = lambda x: 1 if x == 0 else x * f(x-1)
print (sum([int(i) for i in str(f(100))]))
