# Project Euler Problem 20

def factorial(x):
    """returns factorial of x"""
    
    if type(x) != int:
        print("ERROR <- x in factorial(x) is not type int")
        return
    
    result = 1
    
    for i in range(1,x+1):
        result *= i
        
    return result

def digits(x): 
    """returns digits of x"""
    
    if type(x) != int: 
        print("ERROR <- x in factorial(x) is not type int")
        return
    
    return [int(i) for i in list(str(x))]

print(f'Ans = {sum(digits(factorial(100)))}')  
