class Solution(object):
    def shuffle(self, nums, n):
        n=len(nums)//2
        result=[]
        
        for i in range(n):
            result.append(nums[i])
            result.append(nums[n+i])
        return result    
        