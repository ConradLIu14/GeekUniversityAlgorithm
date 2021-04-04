from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generateStr(n, list_p):
            res = []
            for i in list_p:
                s = '.' * i + 'Q' + '.' * (n - i - 1)
                res.append(s)
            return res

        # def judge(a,row):
        #     list_p,n,column,d1,d2 = a
        #     if len(list_p) == n:
        #         res.append(generateStr(list_p))
        #         return False
        #     else:
        #         if d1[column+row] or d2[row-column]:
        #             return False
        #         else:
        #             d1[column+row] = 1
        #             d2[row - column] = 1
        #             list_p.append(row)
        #             return list_p,column+1,d1,d2
        def judge(list_p, n, row, d1, d2):
            if len(list_p) == n:
                res.append(generateStr(n, list_p))
            else:
                for i in range(n):
                    if d1[i + row] or d2[i - row] or i in list_p:
                        continue
                    else:
                        d1[i + row] = 1
                        d2[i - row] = 1
                        list_p.append(i)
                        judge(list_p, n, row + 1, d1, d2)
                        d1[i + row] = 0
                        d2[i - row] = 0
                        list_p.pop()

        res = list()
        d1 = [0] * (2 * n - 1)
        d2 = [0] * (2 * n - 1)
        judge([], n, 0, d1, d2)
        return res


