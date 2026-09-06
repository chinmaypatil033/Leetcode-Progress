class Solution(object):
    def maximumCount(self, nums):
        n=len(nums)
        pos=0
        neg=0

        for i in range(n):
            if nums[i]>0:
                pos+=1
            if nums[i]<0:
                neg+=1
            maxi=max(pos,neg)
        return maxi            
        