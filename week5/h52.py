class Solution:
    def check(self,dialogue1,dialogue2,columns,row):
        if row >= self.n:
            self.count +=1
        available_positions = (~(dialogue1 | dialogue2 | columns)) & ((1 << self.n) - 1)
        while available_positions:
            p = available_positions & (-available_positions)
            available_positions = available_positions & (available_positions - 1)
            self.check((dialogue1 + p) << 1,(dialogue2 + p) >> 1, columns + p, row + 1)

    def totalNQueens(self, n: int) -> int:
        self.count = 0
        self.n = n
        self.check(0,0,0,0)
        return self.count