class Solution(object):
    def merge(self, intervals):
       n=len(intervals)
       merged=[]

       intervals.sort()
       for i in range(n):
        if not merged:
            merged.append(intervals[i])
        else:
            if merged[-1][1]<intervals[i][0]:
                merged.append(intervals[i])
            else:
                merged[-1][1]=max( merged[-1][1],intervals[i][1])
       return merged                 


        