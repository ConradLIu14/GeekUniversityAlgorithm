class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = dict()
        for i in s:
            if i in a:
                a[i] +=1
            else:
                a[i] = 1
        for i in range(len(s)):
            if a[s[i]] == 1:
                return i
        return -1