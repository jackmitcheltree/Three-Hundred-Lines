import time
start = time.time()


from itertools import permutations
with open('cipher.txt') as f: l = [int(x) for x in f.read().strip().split(',')]
for code in permutations('abcdefghijklmnopqrstuvwxyz', 3):
	dcrypt = ''.join(chr(n ^ ord(c)) for n, c in zip(l, code*(len(l)//3)))
	if dcrypt.find(' the ') >= 0: print(sum(ord(d) for d in dcrypt)); break


end = time.time()
print(end-start)