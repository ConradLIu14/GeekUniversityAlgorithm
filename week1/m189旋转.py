from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums = nums[-k:] + nums[:len(nums) - k]
        return nums

s = Solution()
print(s.rotate([1,2,3,4,5,6,7],3))