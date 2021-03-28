from typing import List
n1=2;n2=3;n3=4#ans =5

#这题其实就是斐波拉契数列
#数学 可以特别快速解决
class Solution:
    # 感觉递归直接作出来了,但是太耗时间了，所以要动态规划
    def climbStairs(self, n: int) -> int:
        if n <=0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        stack = [1,2]
        for i in range(0,n-2):
            stack.append(stack[0]+stack[1])
            stack.pop(0)
        return stack[1]

s=Solution()
print(n1,s.climbStairs(n1))
print(3,s.climbStairs(3))
print(4,s.climbStairs(4))
print(5,s.climbStairs(5))
print(6,s.climbStairs(6))


# # 感觉递归直接作出来了,但是太耗时间了 所以要动态规划
# def climbStairs(self, n: int) -> int:
#     if n <= 0:
#         return 0
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#
#     return self.climbStairs(n - 1) + self.climbStairs(n - 2)



