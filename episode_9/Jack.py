import time as t

start = t.time()

with open('p059_cipher.txt', 'r') as file:
    cipher_raw = file.read()

cipher1 = [int(k) for k in cipher_raw.split(',')]
flags = ['the', 'and', 'of', 'to', 'that', 'with', 'he', 'she', 'they', 'but']
potential_keys = []

for i in range(97, 123):
    for j in range(97, 123):
        for k in range(97, 123):
            potential_keys.append([i,j,k])

for key in potential_keys:

    text = [] ; asciis = []
    a = 0 ; b = '' ; hits = 0

    for num in cipher1:
        p = num ^ key[a]
        text.append(chr(p))
        asciis.append(p)
        a += 1
        if a == 3:
            a = 0

    for k in text:
        b = b + k

    text2 = b.split(' ')

    for k in text2:
        if k in flags:
            hits += 1

    if hits > 10:
        print(sum(asciis))
        break

end = t.time()
print()
print(end-start)
print()
