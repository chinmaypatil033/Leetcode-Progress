class Solution(object):
    def missingNumber(self, nums):
        m=len(nums)
        for i in range(0,m+1):
            if i not in nums:
                return i       


        