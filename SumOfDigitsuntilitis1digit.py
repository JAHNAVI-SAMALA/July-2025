#sum the digits of a number
n = int(input())

while n >= 10:
    Sum =0
    while n>0 :
        d = n%10
        Sum += d
        n = n//10
    n = Sum
    
print(Sum)
