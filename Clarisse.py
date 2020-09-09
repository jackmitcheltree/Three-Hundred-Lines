n = 200
ways = [1] + [0]*n
for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
  for i in range(coin, n+1): ways[i] += ways[i-coin]
print (ways[n])