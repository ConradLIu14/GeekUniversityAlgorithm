i1=2;i2=10

class Solution:
    #4以上(大于等于5）必须继续拆分的价值
    #感觉就是拆3啊,没有用dp。。。
    def integerBreak(self, n: int) -> int:
        if n <2:
            return 0
        if n == 2:
            return 1
        if n==3:
            return 2

        div,mod=divmod(n,3)
        if mod == 0:
            return pow(3,div)
        if mod == 1:
            return pow(3,div-1)*4
        if mod == 2:
            return pow(3,div)*2

s=Solution()
print(s.integerBreak(i1))
print(s.integerBreak(i2))

