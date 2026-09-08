class Solution(object):
    def getConcatenation(self, nums):
        n=len(nums)
        result=[]
        for i in range(n):
            result.append(nums[i])
        for i in range(n):
            result.append(nums[i])

        return result     

        