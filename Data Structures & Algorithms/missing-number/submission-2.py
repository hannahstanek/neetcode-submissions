class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cat = False
        new = len(nums)
        for i in range(len(nums)):
            if i in nums:
                cat = True
            else:
                 new = i
        return new

