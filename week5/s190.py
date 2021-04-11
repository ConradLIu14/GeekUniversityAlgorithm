class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        curr = 1
        for i in range(32):
            if curr & n > 0:
                res += 1 << (32 - i-1)
            curr = curr << 1
        return res