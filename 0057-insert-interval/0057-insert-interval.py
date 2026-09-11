class Solution(object):
    def insert(self, intervals, newInterval):
        n=len(intervals)
        i=0
        result=[]

    #    adding intervls completly before newInterval
        while i<n and intervals[i][1]<newInterval[0]:
            result.append(intervals[i])
            i+=1
        #  merging overlap intervals 
        while i<n and intervals[i][0]<=newInterval[1]:
           newInterval[0] = min(newInterval[0], intervals[i][0])
           newInterval[1] = max(newInterval[1], intervals[i][1])
           i+=1
        result.append(newInterval)

        #  adding remaining intervals 
        while i<n :
            result.append(intervals[i])
            i+=1

        return result     

        