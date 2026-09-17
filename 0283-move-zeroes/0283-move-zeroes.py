class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        i=0
        count=0
        while count<n:
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
            else:
                i+=1
            count+=1    
                
            
        