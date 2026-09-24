class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        count={}
        for i in range(n):
            if nums[i]  not in count:
                count[nums[i]]=1
            else:
                count[nums[i]]+=1
        max_count=0
        ans=0

        for num in count:
            if count[num]>max_count:
                max_count=count[num]
                ans=num

        return ans                     
        