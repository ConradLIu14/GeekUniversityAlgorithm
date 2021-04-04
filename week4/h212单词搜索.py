from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = dict()
        end = '#'
        for i in words:
            curr_node = root
            for ii in i:
                if ii in curr_node:
                    curr_node = curr_node[ii]
                else:
                    curr_node[ii] = {}
                    curr_node = curr_node[ii]
            curr_node[end] = i
        print(root)

        rows = len(board)
        columns = len(board[0])
        res = []

        def find_word(pre,row, column, node): # 只能往前回溯，不能转圈。
            # print(row,column,board[row][column],node)
            if board[row][column] in node:
                letter = board[row][column]
                next_node = node[board[row][column]]
                board[row][column] = '.'
                if end in next_node:
                    res.append(next_node.pop(end))
                prer,prec = pre
                c1 = column + 1
                c2 = column - 1
                r1 = row + 1
                r2 = row - 1
                if r1 < rows and r1 != pre:
                    find_word((row,column), r1, column, next_node)
                if r2 >= 0 and r2 != pre:
                    find_word((row,column), r2, column, next_node)
                if c1 < columns and c1 != prec:
                    find_word((row,column), row, c1, next_node)
                if c2 >= 0 and c2 != prec:
                    find_word((row,column), row, c2, next_node)
                board[row][column] = letter

        for i in range(rows):
            for ii in range(columns):
                find_word((-1,-1),i, ii, root)
        return res
b1,w1 = [["a","b"]],["ba"]
b2,w2 = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]],["oa","oaa"]
b3,w3 = [["a","a"]],["aaa"]
b4,w4 = [["a","a"],["a","a"]],["aaaaa"]
b5,w5 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"]
s = Solution()
print(s.findWords(b1,w1))
print(s.findWords(b2,w2))
print(s.findWords(b3,w3))
print(s.findWords(b4,w4))
print(s.findWords(b5,w5))

