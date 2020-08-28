# Project Euler Problem 18

p = """75
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

p = [[int(j) for j in i.split()] for i in p.split('\n')]

def max_pyr_path_sum(p):
    """returns max adjacent path sum top->down through pyramid p"""

    f = [[0 for j in range(i)] for i in range(1,len(p)+1)]
        
    for i in range(len(p)): 
        for j in range(len(p[i])):
            sigma = [] 
            
            if i == 0:
                f[i][j] = p[i][j]
            
            else:
                
                if j == 0:
                    try:
                        sigma.append(f[i-1][j])
                    except:
                        pass
                    
                    if len(sigma) == 0:
                        f[i][j] = p[i][j]
                    
                    else:
                        f[i][j] = p[i][j] + max(sigma)
                
                else:
                    try:
                        sigma.append(f[i-1][j])
                    except:
                        pass
                    
                    try:
                        sigma.append(f[i-1][j-1])
                    except:
                        pass
                    
                    if len(sigma) == 0:
                        f[i][j] = p[i][j]
                    
                    else:
                        f[i][j] = p[i][j] + max(sigma)
                        
    return max(f[-1])

print(f'Ans = {max_pyr_path_sum(p)}')
