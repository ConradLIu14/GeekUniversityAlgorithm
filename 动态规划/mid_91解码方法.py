s1="12"
s2="226"
s3="110"
s4="1010"
s5="1212"
s6="101"
s7="230"
s8="301" #0
s9="611"#2
s10="301"#0
#已经解决，但是希望重新分析做一遍
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        if len(s) == 1:
                return 1
        if len(s) == 2:
            if s[1] == "0":
                if s[0]=="1" or s[0]=="2":return 1
                else: return 0
            elif int(s) < 27:
                return 2
            else:
                return 1
        if int(s[:2]) < 27 and s[1] != "0":
            counts = [1, 2]
        else:
            if s[1]=="0":
                if s[0]=="1" or s[0]=="2":
                    counts = [1, 1]
                else:
                    return 0
            else:counts = [1, 1]
        for i in range(2, len(s)):
            if int(s[i - 1:i + 1]) < 27:
                if s[i] == "0":
                    if s[i-1] =="1" or s[i-1] =="2":
                        counts[1] = counts[0]
                    else:
                        return 0
                elif s[i-1]=="0":
                    counts[0]=counts[1]

s=Solution()
print(s.numDecodings(s1))
print(s.numDecodings(s2))
print(s.numDecodings(s3))
print(s.numDecodings(s4))
print(s.numDecodings(s5))
print(s.numDecodings(s6))
print(s.numDecodings(s7))
print(s.numDecodings(s8))
print(s.numDecodings(s9))
print(s.numDecodings(s10))

# def numDecodings(self, s: str) -> int:
        # if s[0] == "0": return 0
        # if len(s) == 1:
        #         return 1
        # if len(s) == 2:
        #     if s[1] == "0":
        #         if s[0]=="1" or s[0]=="2":return 1
        #         else: return 0
        #     elif int(s) < 27:
        #         return 2
        #     else:
        #         return 1
        # if int(s[:2]) < 27 and s[1] != "0":
        #     counts = [1, 2]
        # else:
        #     if s[1]=="0":
        #         if s[0]=="1" or s[0]=="2":
        #             counts = [1, 1]
        #         else:
        #             return 0
        #     else:counts = [1, 1]
        # for i in range(2, len(s)):
        #     if int(s[i - 1:i + 1]) < 27:
        #         if s[i] == "0":
        #             if s[i-1] =="1" or s[i-1] =="2":
        #                 counts[1] = counts[0]
        #             else:
        #                 return 0
        #         elif s[i-1]=="0":
        #             counts[0]=counts[1]
        #         else:
        #             helper = counts[1]
        #             counts[1] = counts[0] + counts[1]
        #             counts[0] = helper
        #     else:
        #         if s[i]=="0":return 0
        #         counts[0]=counts[1]
        # return counts.pop()



