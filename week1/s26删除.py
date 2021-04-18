class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        curr_p = 1; curr = nums[0]; count = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            else:
                nums[curr_p] = nums[i]
                curr_p += 1
                count += 1
        nums = nums[:count]
        return count