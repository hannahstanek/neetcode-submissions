from collections import Counter
class Solution:
    def countBits(self, n: int) -> List[int]:
        new = []
        new2 = []
        i = 0
        t = n
        while t >= 0:
            new.append(i)
            i +=1
            t -= 1

        binary = [f"{x:01b}" for x in new]
        

        for i in binary:
            counts = Counter(i)
            nums = counts['1']
            new2.append(nums)

        return new2


