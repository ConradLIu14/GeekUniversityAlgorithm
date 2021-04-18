from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return nums1
        if m == 0: nums1[:] = nums2

        curr = m+n - 1; n_p = n - 1; m_p = m - 1
        while curr >= 0 and  n_p >= 0 and m_p >= 0:
            if nums2[n_p] > nums1[m_p]:
                nums1[curr] = nums2[n_p]
                n_p -=1
            else:
                nums1[curr] = nums1[m_p]
                m_p -= 1
            curr -= 1
        if n_p >= 0: nums1[:n_p+1] = nums2[:n_p+1]
        return nums1

s = Solution()
print(s.merge([2,0],1,[1],1))