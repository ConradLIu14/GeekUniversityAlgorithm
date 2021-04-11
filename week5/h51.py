class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        dialogue1 = 0; dialogue2 = 0
        columns = set(); res = 0
        def check(c):
            r = len(columns)
            if r == n:
                res += 1
                return 
            for i in range(n):
                if i in columns or dialogue1 & (1<<(i+c)) or dialogue2 & (1<<(i-c)):
                    continue
                columns.add(i)
                dialogue1 += (1<<(i+c))
                dialogue2 += (1<<(i-c))
                check(c+1)
                dialogue1 -= (1<<(i+c))
                dialogue2 -= (1<<(i-c))
                columns.remove(i)
        check(0)
        return res