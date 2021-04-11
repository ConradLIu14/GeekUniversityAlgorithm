class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(nums):
            if len(nums) <= 1: return nums,0
            mid = len(nums) >> 1
            m1, count1 = merge(nums[:mid])
            m2, count2 = merge(nums[mid:])
            p1 = 0; p2 = 0; temp = []; curr_count = count1 + count2
            while p1 < len(m1) and p2 < len(m2):
                if m2[p2] < m1[p1]:
                    curr_count += len(m1) - p1
                    temp.append(m2[p2])
                    p2 += 1
                else:
                    temp.append(m1[p1])
                    p1 += 1
            if p1 < len(m1):
                temp+= m1[p1:]
            if p2 < len(m2):
                temp += m2[p2:]
            return temp,curr_count
        sorted_nums, res = merge(nums)
        return res