""" this code is to check whether the given kth bit is a set bit or not
here set bit means whenever we perform left shift  and  & operation
if we get all 0s it is not a set bit else it is a set bit(1) gfg """


def check_ith_bit(n,k):
    if((n&(1<<k))==0):
        return False
    return True
n,k =map( int,input().split())
print(check_ith_bit(n,k))
    
#using right shift

def check_ith_bit(n,k):
    n= n>>k
    if n&1 == 0:
        return False
    return True
