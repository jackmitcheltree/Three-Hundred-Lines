c = [1] + [0 for i in range(201)]
for k in [1,2,5,10,20,50,100,200]:
    for i in range(201-k): c[i+k] += c[i] 
print(f'Ans = {c[200]}')    
