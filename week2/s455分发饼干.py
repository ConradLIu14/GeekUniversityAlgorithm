class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g); s = sorted(s)
        res = 0; s_pointer = 0; g_pointer = 0
        while s_pointer < len(s) and g_pointer < len(g):
            if s[s_pointer] >= g[g_pointer]:
                res+=1; s_pointer += 1; g_pointer += 1
            else:
                s_pointer += 1
        return res