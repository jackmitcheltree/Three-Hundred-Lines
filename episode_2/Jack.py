#Find the sum of the digits in the number 100!
def factorial(n):
    L = list(range(1,n))
    v = 1
    for x in range(n-1):
        v = v * L[x]
    return v

def make_digits(n):
    digits = []
    temp = n
    while temp > 0:
        hold = temp % 10
        digits.append(hold)
        temp = temp - hold
        temp = temp // 10
    digits.reverse()
    return digits

print(sum(make_digits(factorial(100))))
