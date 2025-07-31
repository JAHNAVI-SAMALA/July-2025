n = int(input())
def generate(curr,ans,Open,Close,n):
    if Open == Close and Open + Close == 2* n:
        ans.append(curr)
        return
    if Open > n:
        return
    if Close > Open:
        return
    generate(curr+"(",ans,Open+1,Close,n)
    generate(curr+")",ans,Open,Close+1,n)
    
def generateParenthesis(n):
    curr = ""
    ans = []
    Open = 0
    Close = 0
    generate(curr,ans,Open,Close,n)
    return ans
print(generateParenthesis(n))
