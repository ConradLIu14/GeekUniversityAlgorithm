class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set()
        for i in jewels:
            s.add(i)
        count = 0
        for i in stones:
            if i in s:
                count+=1
        return count