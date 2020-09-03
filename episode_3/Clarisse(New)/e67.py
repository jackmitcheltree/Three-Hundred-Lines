with open("67.txt", "r") as f: t = [line.split() for line in f]
while len(t) > 1:
  t[-2] = [int(t[-2][i]) + int(t[-1][i]) if t[-1][i] > t[-1][i+1] else int(t[-2][i]) + int(t[-1][i+1]) for i in range(len(t[-2]))]
  t.pop()
print(t[0][0])