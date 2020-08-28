#Find the maximum path sum from the top to the bottom of the triangle.
import time
start = time.time()

triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

def max_path(triangle):
    triangle = [int(x) for x in triangle.split()]
    n = int( (2 * len(triangle) + (0.25))**(1/2) - 0.5 + 1)
    tri = lambda n: (n * (n+1)) // 2
    X = list(map(tri, list(range(n-1))))
    Y = list(map(tri, list(range(1,n))))
    condense = lambda x,y : (x,y)
    rows = [triangle[a:b] for a,b in list(map(condense, X, Y))]
    while len(rows) > 1:
        for x in range(len(rows[-1])-1):
            if rows[-1][x] >= rows[-1][x+1]:
                rows[-2][x] += rows[-1][x]
            else:
                rows[-2][x] += rows[-1][x+1]
        del rows[-1]
    return rows

print(max_path(triangle))
end = time.time()
print(end-start)
