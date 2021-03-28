from typing import List

g1=[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
g2=[[9,1,4,8]]

class Solution:
    #与120题类似，直接上优化过的动态规划
    def minPathSum(self, grid: List[List[int]]) -> int:
        stack = [grid[0][0]]
        for i in range(1,len(grid[0])):
            if i>0:stack.append(stack[-1]+grid[0][i])
        if len(grid)==1:return stack[-1]
        for i in range(1,len(grid)):
            for ii in range(len(grid[i])):
                if ii ==0:stack[0]=stack[0]+grid[i][0]
                else:
                    stack[ii] = min(stack[ii-1],stack[ii])+grid[i][ii]
            print(stack)
        return stack[-1]

s=Solution()
# print(s.minPathSum(g1))
print(s.minPathSum(g2))



