n,k = map(int,input().split())
n= n&(~(1<<k))
print(n)
