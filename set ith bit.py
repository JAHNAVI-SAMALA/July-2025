def setithbit(n,k):
    n= n | 1<<k
    return n
n,k = map(int,input().split())
print(setithbit(n,k))
