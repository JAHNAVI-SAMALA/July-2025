#sum of prime numbers in a given digit
"""def sumOfPrime(n):
    primes = [2,3,5,7]
    res = 0
    while n> 0:
        d = n% 10
        if d in primes:
            res+=d
        n = n//10
    return res
n = int(input())
print(sumOfPrime(n))"""



def checkPrime(n):
    c = 0
    for i in range (1,n+1):
        if n%i==0:
            c += 1
    if c==2:
        return True
    else:
        return False
n = int(input())
Sum = 0
while n> 0 :
    rem =n% 10
    if checkPrime(rem):
        Sum += rem
    n= n//10
print(Sum)
