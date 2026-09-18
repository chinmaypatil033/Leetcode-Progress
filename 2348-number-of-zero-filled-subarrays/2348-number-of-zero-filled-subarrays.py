class Solution(object):
    def zeroFilledSubarray(self, nums):
       n=len(nums)
       count=0
       result=0

       for i in range(n):
        if nums[i]==0:
            count+=1
            result+=count
        else:
            count=0
       return result    