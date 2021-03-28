# 贪心也能做
from typing import List

a1=[ [1,2], [2,3], [3,4], [1,3] ] #output: 1
a2=[ [1,2], [1,2], [1,2] ] #output:2
a3= [ [1,2], [2,3] ] #output0

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int: