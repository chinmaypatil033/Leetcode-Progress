class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        i=0
        count=0
        maxcount=0
        n=len(nums)
        for i in range(0,n):
            if nums[i]==1:
                count+=1
            else:
                maxcount=max(maxcount,count)
                count=0
        return max(maxcount,count)            
        