#converting set bit into non set bit i.e. 1 -> 0
n,k = map(int,input().split())
n=n^1<<k
print(n)
