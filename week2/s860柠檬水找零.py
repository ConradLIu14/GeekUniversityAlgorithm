class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = dict(zip([5,10,],[0,0]))
        for i in bills:
            if i == 5:
                count[i] += 1
            elif i == 10:
                count[10] +=1
                count[5] -= 1
                if count[5] < 0:
                    return False
            elif i == 20:
                if count[10] > 0 and count[5] > 0:
                    count[10] -= 1; count[5] -= 1
                elif count[5] >=3:
                    count[5] -= 3
                else:
                    return False
        return True