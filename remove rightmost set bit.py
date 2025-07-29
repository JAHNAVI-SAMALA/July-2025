"""  Remove rightmost set bit
here there's a functionality between n and n-1 i.e, from the rightmost set bit all values are inverted"""
n = int(input())
n= n &(n-1)
print (n)
