def setithbit(n,k):
    n= n or 1<<k
    return n
n,k = map(int,input().split())
print(setithbit(n,k))
