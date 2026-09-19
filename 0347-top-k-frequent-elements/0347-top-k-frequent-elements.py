class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        count = {}

        

        result = []

      # Count frequency
        for i in range(n):
          if nums[i] in count:
           count[nums[i]] += 1
          else:
           count[nums[i]] = 1

      # Find top k
        for i in range(k):

           max_freq = 0
           max_num = 0

           for num in count:
                if count[num] > max_freq:
                 max_freq = count[num]
                 max_num = num

           result.append(max_num)

           del count[max_num]

        return result
