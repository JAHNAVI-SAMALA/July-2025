""" power of 2 problem
if  a num is power of 2 then in binary form the num is only one '1' """
def powerOf2(n):
    if n & n-1 == 0:
        return True
    return False
n = int(input())
print(powerOf2(n))
