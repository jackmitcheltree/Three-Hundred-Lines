a = [1] + [0]*200
for c in [1, 2, 5, 10, 20, 50, 100, 200]:
  for i in range(c, len(a)): a[i] += a[i-c]
print (a[-1])
