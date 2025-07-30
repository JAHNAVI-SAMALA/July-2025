""" divide by  10  technique
if we divide a number by 10 then we get the last digit as remainder
this code is count no.of digits in a given number."""
n = int (input())
c =0
while n > 0:
    n= n//10
    c+=1
print(c)
        
