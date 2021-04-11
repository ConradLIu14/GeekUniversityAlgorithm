class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            for ii in range(len(nums) - i):
                if nums[ii] > nums[ii+1]:
                    # temp = nums[ii]
                    # nums[ii] = nums[ii+1]
                    # nums[ii+1] = temp
                    nums[ii],nums[ii+1] = nums[ii+1],nums[ii]

        
        count = 0
        nums = nums[::-1]
        start = nums[0]
        for i in nums:
            if start == i:
                continue
            else:
                count += 1
                if count == 2:
                    return i
                start = i
        return nums[0]