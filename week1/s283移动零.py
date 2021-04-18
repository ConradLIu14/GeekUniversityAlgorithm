from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 让 j 永远指向最左边的0
        j = None
        for i in range(len(nums)):
            print(nums,j)
            if nums[i] != 0:
                if j or j == 0:
                    nums[j] = nums[i]
                    nums[i] = 0
                    j+=1
            else:
                if j is None:
                    j = i
        print('nums',nums)

s = Solution()
s.moveZeroes([0,1,0,3,12])