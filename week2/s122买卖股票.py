class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr = prices[0]
        for i in prices[1:]:
            if i - curr >0:
                res += i-curr
            curr = i
        return res