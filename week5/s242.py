class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = dict()
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        for i in t:
            if not i in count:
                return False
            else:
                count[i] -= 1
                if count[i] == -1:
                    return False

        return len(s) == len(t)