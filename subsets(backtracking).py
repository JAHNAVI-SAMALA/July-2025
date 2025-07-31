def generate(ind,curr,ans,nums):
    if(ind == len(nums)):
       ans.append(curr.copy())
       return
    curr .append(nums[ind])
    generate(ind+1,curr,ans,nums)
    curr.pop()
    generate(ind+1,curr,ans,nums)
       
def subsets(nums):
    ind = 0
    curr = []
    ans =[]
    generate(ind,curr,ans,nums)
    return ans
nums = list(map(int,input().split()))
print(subsets(nums))
