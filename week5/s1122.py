class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = dict(zip(arr2, [0 for i in arr2]))
        else1 = []
        for i in arr1:
            if i in count:
                count[i] += 1
            else:
                else1.append(i)

        res = []
        for i in arr2:
            res += [i] * count[i]
        res = res + sorted(else1)
        return res