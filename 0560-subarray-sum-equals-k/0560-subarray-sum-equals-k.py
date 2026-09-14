class Solution(object):
    def subarraySum(self, nums, k):
        prefix = {0: 1}
        sum = 0
        count = 0

        for num in nums:
            sum += num

            if sum - k in prefix:
                count += prefix[sum - k]

            if sum in prefix:
                prefix[sum] += 1
            else:
                prefix[sum] = 1

        return count
        