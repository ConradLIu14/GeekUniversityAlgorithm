class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals)

        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        state = 0
        for i in intervals[1:]:
            if i[0] <= curr_end and i[1] >= curr_end:
                curr_end = i[1]
            elif i[0] > curr_end:
                res.append([curr_start,curr_end])
                curr_start = i[0]
                curr_end = i[1]

        res.append([curr_start,curr_end])
        return res