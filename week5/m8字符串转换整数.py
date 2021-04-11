class Solution:
    def myAtoi(self, s: str) -> int:
        if s == '': return 0
        state = 0
        sign = 1
        nums = set([str(i) for i in range(10)])

        signs = {'+','-'}
        readin = ''
        for i in s:
            if state == 0:
                if i == ' ':
                    continue
                elif i in signs:
                    if i == '-':
                        sign = -1
                    state = 1
                elif i in nums:
                    state = 1
                    readin += i
                else:
                    return 0
            else:
                if i in nums:
                    if i == '0' and readin == '0':
                        continue
                    else:
                        readin += i
                # elif i in signs:
                #     return 0
                else:
                    if readin == '': return 0
                    res = sign * int(readin)
                    if res >= -pow(2,31) and res <= pow(2,31) - 1:
                        return res
                    else:
                        if sign == -1:
                            return -pow(2,31)
                        else:
                            return pow(2,31) - 1
        if readin == '': return 0
        res = sign * int(readin)
        if res >= -pow(2,31) and res <= pow(2,31) - 1:
            return res
        else:
            if sign == -1:
                return -pow(2,31)
            else:
                return pow(2,31) - 1