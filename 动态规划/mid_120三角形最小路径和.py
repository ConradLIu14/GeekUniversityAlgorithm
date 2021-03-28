from typing import List

t1=[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

#stack2 的空间 是可以优化掉的
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        stack1 = triangle[0]
        stack2 = []
        for i in range(1,len(triangle)):
            for ii in range(len(triangle[i])):
                if ii == 0:
                    stack2.append(stack1[0]+triangle[i][0])
                elif ii == len(triangle[i])-1:
                    stack2.append(stack1[-1]+triangle[i][-1])
                else:
                    stack2.append(min(stack1[ii],stack1[ii-1])+triangle[i][ii])
            stack1 = stack2
            stack2 = []
            print(stack1)
        return min(stack1)
#优化一下 空间复杂度
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        stack1 = triangle[0]
        for i in range(1, len(triangle)):
            if i>0: stack2=stack1[0]
            for ii in range(len(triangle[i])):
                # print(len(triangle[i]),ii)
                if ii == 0:
                    stack1[0]=stack1[0] + triangle[i][0]
                elif ii == len(triangle[i]) - 1:
                    stack1.append(stack2 + triangle[i][-1])
                else:
                    curr = stack2
                    stack2=stack1[ii]
                    stack1[ii]=min(stack1[ii],curr) + triangle[i][ii]
        return min(stack1)


s=Solution()
print(s.minimumTotal(t1))
print(s.minimumTotal2(t1))

