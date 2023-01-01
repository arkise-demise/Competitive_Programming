class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result=[]
        start,end = intervals[0][0],intervals[0][1]
        for i in intervals:
            if i[0] > end:
                result.append([start,end])
                start,end = i[0],i[1]
            else:
                end = max(end,i[1])
        result.append([start,end])
        return result            