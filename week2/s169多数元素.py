class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr_max = 1; res = nums[0]; a = {res:1}
        for i in nums[1:]:
            if i in a:
                a[i] += 1
                if a[i] > curr_max: curr_max = a[i]; res = i
            else:
                a[i] = 1
        return res
        